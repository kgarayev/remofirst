from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from src.chatty.api.user.domain.models.models import User as UserModel
from src.chatty.api.user.domain.serializers.entities import RegisterUserSerializer, LoginSerializer, UserSerializer


class RegisterUser(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = UserModel.objects.all()

class LoginUser(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer


    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = authenticate(request, username=serializer.validated_data.get("username"), 
                                password=serializer.validated_data.get("password")
                                )
            if user is not None:   
                login(request, user)
                
                # user_serializer = UserSerializer(user)
                
                return Response("user_serializer.data", status=200)


        
        return Response(serializer.errors, status=400)