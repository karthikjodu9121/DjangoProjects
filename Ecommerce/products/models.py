from django.db import models
from django.urls import reverse
from base.models import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null = True, blank=True)
    category_image = models.ImageField(upload_to = 'categories')

    
    class Meta:
            verbose_name =("Category") # type: ignore
        verbose_name_plural =("Categories") # type: ignore

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})



class Product(BaseModel):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null = True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_description = models.TextField()



class ProductImage(BaseModel):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to = 'product')
