from rest_framework import serializers


class WSMessageSerializer(serializers.Serializer):

    sender_user_id = serializers.UUIDField(required=True)
    message_body = serializers.CharField(required=True)
    chat_session_id = serializers.UUIDField(required=True)
    SENDER_CLIENT_COOKIES = serializers.DictField(required=True)
