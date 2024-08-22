from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here

class Post(models.Model):
    
    title = models.CharField(max_length=45)
    description = models.TextField()
    author = models.CharField(max_length=20)
    gmail = models.EmailField(max_length=50)
    created_at = models.DateField(default = datetime.now(), blank = True)
    is_published = models.BooleanField(default = False)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

