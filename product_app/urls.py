from django.urls import path
from .views import product_summary, ProductListAPIView, ProductEditAPIView, ProductVariantEditAPIView, ProductVariantPriceListCreateAPIView, ProductVariantPriceRetrieveUpdateDestroyAPIView, ProductDeleteAPIView

urlpatterns = [
    path('product_summary/', product_summary, name='product_summary'),
    path('api/products/', ProductListAPIView.as_view(), name='product_list_api'),
    path('api/products-delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product_delete_api'),
    path('api/products/<int:pk>/', ProductEditAPIView.as_view(), name='product_edit_api'),
    path('api/product_variants/<int:pk>/', ProductVariantEditAPIView.as_view(), name='product_variant_edit_api'),
    path('api/product_variant_prices/', ProductVariantPriceListCreateAPIView.as_view(), name='product_variant_price_list_create_api'),
    path('api/product_variant_prices/<int:pk>/', ProductVariantPriceRetrieveUpdateDestroyAPIView.as_view(), name='product_variant_price_retrieve_update_destroy_api'),
   
    
    
]
