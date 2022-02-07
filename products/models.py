from django.db import models
import uuid
import PIL

# Create your models here.
class Brand(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True)
    name = models.CharField(max_length=45, null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return (str(self.name))



class Product_packed(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True)
    name = models.CharField(max_length=50, null=False)
    weight = models.CharField(max_length=40, null=False)
    image = models.ImageField(null=True, blank=True)
    mrp = models.CharField(max_length=40, null=False)
    price = models.CharField(max_length=40, null=False)
    hsn_code = models.CharField(max_length=45, null=False)
    cgst = models.CharField(max_length=40, null=False)
    sgst = models.CharField(max_length=40, null=False)
    igst = models.CharField(max_length=40, null=False)
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    catagory = models.CharField(max_length=45,null=True,blank=True, choices = (('grocery', 'Grocery'), ('beverage', 'Beverage'), ('snacks', 'Snacks'), ('household', 'Household'), ('personalcare', 'Personal Care')))

    def __str__(self):
        return ('product: ' + str(self.name) )


class Product_unpacked(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, unique=True)
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(null=True, blank=True)
    price = models.CharField(max_length=40, null=False)
    hsn_code = models.CharField(max_length=45, null=False)
    cgst = models.CharField(max_length=40, null=False)
    sgst = models.CharField(max_length=40, null=False)
    igst = models.CharField(max_length=40, null=False)
    description = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=40,choices = (('kg','kg'),('dozen', 'dozen'), ('gm', 'gm'), ('litre', 'litre'), ('ml', 'ml'), ('inch', 'inch'), ('meter', 'meter'), ('feet', 'feet'), ('nag', 'nag')))
    rate = models.CharField(max_length=40, null=False)

    def __str__(self):
        return (str(self.name))









