from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from utils.common import API_RESPONSE
import json

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                tokens = get_tokens_for_user(user)
                return API_RESPONSE(True,"",tokens,status.HTTP_201_CREATED)
            except DuplicateKeyError as e:
                return API_RESPONSE(False,"",{'detail': 'Email or username already exists.'},status.HTTP_400_BAD_REQUEST)
            
        return API_RESPONSE(False,"",serializer.errors, status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            tokens = get_tokens_for_user(user)
            return API_RESPONSE(True,'',tokens,status.HTTP_200_OK)
        return API_RESPONSE(False,'Login Faild',serializer.errors,status.HTTP_400_BAD_REQUEST)
