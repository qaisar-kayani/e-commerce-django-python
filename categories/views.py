from rest_framework.views import APIView
from rest_framework import status
from utils.common import API_RESPONSE
from.models import Category
from .serializers import CategorySerializer

import logging

logger = logging.getLogger(__name__)

class CategoryTestView(APIView):
    def post(self, request):
        logger.info("POST /api/category called.")
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return API_RESPONSE(True, "Category created", None, status.HTTP_201_CREATED)
        return API_RESPONSE(False, "Validation error", serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        logger.info("GET /api/product called.")
        category = Category.objects()
        serializer = CategorySerializer(category, many=True)
        return API_RESPONSE(True, "Category fetched", serializer.data, status.HTTP_200_OK)
