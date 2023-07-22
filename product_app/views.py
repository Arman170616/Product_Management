from django.http import JsonResponse
from .models import Product, ProductVariantPrice, ProductVariant, ProductImage
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSummarySerializer, ProductSerializer, ProductVariantSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.db import models
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductVariantPriceSerializer

from django.utils.dateparse import parse_date
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView
from rest_framework.generics import DestroyAPIView



@api_view(['GET'])
def product_summary(request):
    total_products = Product.objects.count()
    average_price = ProductVariantPrice.objects.aggregate(avg_price=models.Avg('price'))
    products_in_stock = ProductVariantPrice.objects.filter(stock__gt=0).count()
    latest_products = list(Product.objects.order_by('-created_at')[:5].values_list('title', flat=True))
    top_products_by_price = list(ProductVariantPrice.objects.order_by('-price')[:5].values_list('product__title', 'price'))


    data_summary = {
        'total_products': total_products,
        'average_price': average_price['avg_price'],
        'products_in_stock': products_in_stock,
        'latest_products': latest_products,
        'top_products_by_price': top_products_by_price,
        
    }

    return Response(data_summary)



class ProductEditAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductVariantEditAPIView(RetrieveUpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class ProductVariantPriceListCreateAPIView(ListCreateAPIView):
    queryset = ProductVariantPrice.objects.all()
    serializer_class = ProductVariantPriceSerializer

class ProductVariantPriceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductVariantPrice.objects.all()
    serializer_class = ProductVariantPriceSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# class ProductListAPIView(APIView):
#     def get(self, request):
#         paginator = PageNumberPagination()
#         paginator.page_size = 10
#         products = Product.objects.all()
#         paginated_products = paginator.paginate_queryset(products, request)
#         serializer = ProductSerializer(paginated_products, many=True)
#         return paginator.get_paginated_response(serializer.data)
    

class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='lte')
    start_date = filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Product
        fields = []

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer