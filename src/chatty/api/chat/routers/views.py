from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from api.chat.models import Session, Message
from api.chat.domain.serializers.serializers import SessionSerializer, MessageSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ChatMessage(ListAPIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = MessageSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        session_id = self.kwargs.get('session_id')
        return Message.objects.filter(session_id_id=session_id).order_by('-created_at')