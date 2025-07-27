from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status
from utils.common import API_RESPONSE

ALLOWED_PATHS = [
    '/api/auth/login/',
    '/api/auth/register/',
    '/api/token/refresh/',
]

class JWTAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.authenticator = JWTAuthentication()

    def __call__(self, request):
        path = request.path

        if path.startswith('/api/') and path not in ALLOWED_PATHS:
            try:
                user_auth_tuple = self.authenticator.authenticate(request)
                if user_auth_tuple is None:
                    raise InvalidToken("Authentication credentials were not provided.")

                request.user, _ = user_auth_tuple

            except (InvalidToken, TokenError) as e:
                return API_RESPONSE(False,"nvalid or expired token",{"details": str(e)},status.HTTP_401_UNAUTHORIZED)

        return self.get_response(request)
