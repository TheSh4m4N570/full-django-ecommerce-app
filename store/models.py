from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default='default.jpg', upload_to='images/product/%Y/%m/%d/')
    stock = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.category.slug, 'product_slug': self.slug})