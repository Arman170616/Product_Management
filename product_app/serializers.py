from rest_framework import serializers
from .models import Product, ProductVariantPrice, ProductImage, ProductVariant, Variant


class ProductSummarySerializer(serializers.Serializer):
    total_products = serializers.IntegerField()
    average_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    products_in_stock = serializers.IntegerField()
    latest_products = serializers.ListField(child=serializers.CharField())
    top_products_by_price = serializers.ListField(child=serializers.CharField())
    category_counts = serializers.ListField(child=serializers.DictField(child=serializers.IntegerField()))



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'description', 'created_at', 'updated_at')



class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductVariantPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrice
        fields = '__all__'