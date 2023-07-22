from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product.title}"
    

class ProductVariant(models.Model):
    variant = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.variant
    

class ProductVariantPrice(models.Model):
    product_variant_one = models.ForeignKey('ProductVariant', related_name='variant_one_prices', on_delete=models.CASCADE)
    product_variant_two = models.ForeignKey('ProductVariant', related_name='variant_two_prices', on_delete=models.CASCADE, blank=True, null=True)
    product_variant_three = models.ForeignKey('ProductVariant', related_name='variant_three_prices', on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Price for {self.product.title}: {self.price}"
    


class Variant(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title