from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from utils.common import API_RESPONSE
import logging

logger = logging.getLogger(__name__)

class ProductView(APIView):
    def post(self, request):
        logger.info("POST /api/product called.")
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return API_RESPONSE(True, "Product created", None, status.HTTP_201_CREATED)
        return API_RESPONSE(False, "Validation error", serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        logger.info("GET /api/product called.")
        products = Product.objects()
        serializer = ProductSerializer(products, many=True)
        return API_RESPONSE(True, "Products fetched", serializer.data, status.HTTP_200_OK)




