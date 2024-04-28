from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer   
from api.user.domain.models.models import User as UserModel
from api.user.domain.serializers.entities import RegisterUserSerializer, LoginSerializer, UserSerializer

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_description="Register a simple user based on django.contrib.auth.models.User."
))
class RegisterUser(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = UserModel.objects.all()


@method_decorator(name='post', decorator=swagger_auto_schema(
    operation_description="Logout django.contrib.auth.models.User and clear signed session cookies."
))
class LogoutUser(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]  


    def post(self, request):
        request.session.flush()
        return Response({'logout': 'success'}, status=200)


class LoginUser(APIView):

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    # parser_classes = [JSONParser]
    # renderer_classes = [JSONRenderer]


    @swagger_auto_schema(request_body=LoginSerializer, operation_description="Login an existing django.contrib.auth.models.User and create a signed session cookie on the client side.")
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data.get("username"), 
                                password=serializer.validated_data.get("password")
                                )
            if user is not None:   
                login(request, user)
                print(request.session)
                user_serializer = UserSerializer(user)
                
                return Response({'login': 'success', 'user': user_serializer.data}, status=200)


        
        return Response(serializer.errors, status=400)
    

class GetCookies(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        return Response(request.COOKIES, status=200)