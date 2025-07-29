import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status

ALLOWED_PATHS = [
    '/api/auth/login/',
    '/api/auth/register/',
    '/api/token/refresh/',
]

class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if path.startswith('/api/') and path not in ALLOWED_PATHS:
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return JsonResponse({
                    "success": False,
                    "message": "Authentication credentials were not provided.",
                }, status=status.HTTP_401_UNAUTHORIZED)

            token = auth_header.split(' ')[1]

            try:
                # Validate signature & expiry
                UntypedToken(token)

                # Decode token payload without DB hit
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                print(payload)

                # Attach user info to request (or wherever you want)
                request.user_info = payload

            except (InvalidToken, TokenError, jwt.ExpiredSignatureError, jwt.DecodeError) as e:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid or expired token",
                    "data": {"details": str(e)}
                }, status=status.HTTP_401_UNAUTHORIZED)

        response = self.get_response(request)
        return response
