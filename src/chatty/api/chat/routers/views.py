from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas import AutoSchema
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from api.chat.models import Session, Message
from api.chat.domain.serializers.serializers import SessionSerializer, MessageSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ChatMessageView(ListAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        session_id = self.kwargs.get('session_id')
        return Message.objects.filter(session_id_id=session_id)
    

class ChatSessionGetView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]    

    def get(self, request, user_id):
        session = Session.objects.filter(members=user_id)
        serializer = SessionSerializer(session, many=True, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ChatSessionPostView(APIView):    

    
    parser_classes = [JSONParser]
    # queryset = Session.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]  
    serializer_class = SessionSerializer
    
    @swagger_auto_schema(request_body=SessionSerializer)
    def post(self, request):

        serializer = SessionSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)