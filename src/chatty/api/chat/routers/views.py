import os
from api.chat.domain.serializers.serializers import MessageSerializer, SendMessageSerializer, SessionSerializer
from api.chat.models import Message, Session
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(
    name="get",
    decorator=swagger_auto_schema(operation_description="Get all messages for the provided chat session for authenticated user only."),
)
class ChatMessageView(ListAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination

    # def filter_queryset(self, queryset):
    #     # # filter queryset to exclude messages that are not sent by the authenticated user
    #     # exclude = []

    #     # for i, message in enumerate(queryset):
    #     #     if message.sender != self.request.user:
    #     #         exclude.append(i)

    def get_queryset(self):
        session_id = self.kwargs.get("session_id")
        q = Message.objects.filter(session_id_id=session_id).filter(sender=self.request.user)
        return q

    def handle_exception(self, exc):
        return Response(super().handle_exception(exc), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):

        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": f"An error occurred while fetching messages. {e}"}, status=status.HTTP_400_BAD_REQUEST)


class ChatSessionGetView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    @swagger_auto_schema(
        operation_description="Get all chat sessions for the authenticated user. Can get only authenticated user's chat sessions."
    )
    def get(self, request, user_id):

        if user_id != str(request.user.id):
            return Response({"error": "You can only get your own chat sessions."}, status=status.HTTP_403_FORBIDDEN)

        session = Session.objects.filter(members=request.user.id)
        serializer = SessionSerializer(session, many=True, context={"request": request})

        try:
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"An error occurred while fetching chat sessions. {e}"}, status=status.HTTP_400_BAD_REQUEST)


class ChatSessionPostView(APIView):

    parser_classes = [JSONParser]
    # queryset = Session.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = SessionSerializer

    @swagger_auto_schema(
        request_body=SessionSerializer,
        operation_description="Create a new chat session and Assing provided users (User-Ids) to the newly created chat session.",
    )
    def post(self, request):

        serializer = SessionSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendMessageView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = SendMessageSerializer

    @swagger_auto_schema(request_body=SendMessageSerializer, operation_description="Send a message to a chat session asynchronously... ")
    def post(self, request):
        serializer = SendMessageSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            print(serializer.data)
            print(type(serializer.data))
            try:
                request.kafka_producer.send(
                    os.getenv("KAFKA_TOPIC"),
                    value={
                        "sender_user_id": str(request.user.id),
                        "message_body": serializer.data["message"],
                        "chat_session_id": str(serializer.data["session_id"]),
                        "SENDER_CLIENT_COOKIES": request.COOKIES,
                    },
                )

            except Exception as e:
                return Response({"error": f"An error occurred while sending message. {e}"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"status": "sucsess", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
