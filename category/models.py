from django.db import models
from django.urls import reverse


# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    category_image = models.ImageField(upload_to='images/categories/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('product_by_category', kwargs={'slug': self.slug})

