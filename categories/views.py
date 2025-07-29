from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryTestView(APIView):
    def get(self, request):
        # return Response({"message": "Category test working!"}, status=status.HTTP_200_OK)
        return Response({"test": "ok"})
