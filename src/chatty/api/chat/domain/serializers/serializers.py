from rest_framework import serializers
from api.chat.models import Session, Message
from api.user.domain.serializers.entities import UserSerializer

class SessionSerializer(serializers.ModelSerializer):
    
    members = UserSerializer(many=True, read_only=True)
    users = serializers.ListField(write_only=True)


    class Meta:
        model = Session
        exclude = ['id']

    def create(self, validated_data):
        member = validated_data.pop('members')
        session = Session.objects.create(**validated_data)
        session.members.set(member)

        return session
    
class MessageSerializer(serializers.ModelSerializer):
    
    sender_firstname = serializers.SerializerMethodField()

    class Meta:
        model = Message
        exclude = ['id', 'session_id']

    def get_sender_firstname(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"