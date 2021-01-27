from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.

class MyProduct(models.Model):
    ProductThumb = models.ImageField(default='default.jpg', blank=True)
    ProductName = models.CharField(max_length=100)
    ProductDescription = models.TextField(null=True, blank=True)
    ProductPrice = models.IntegerField()
    ProductContact=models.CharField(max_length=14)
    date_posted = models.DateTimeField(default=timezone.now)
    Producer = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.ProductName

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk':self.pk})


