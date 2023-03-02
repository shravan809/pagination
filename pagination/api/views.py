from .serializers import ProductSerializer
from .models import Product
from rest_framework.generics import ListAPIView
from .pagination import *
# Create your views here.

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPageNumberPagination
    #pagination_class = MyLimitOffsetPagination
    #pagination_class = MyCursorPagination