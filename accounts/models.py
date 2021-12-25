from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.CharField(max_length=50,)
