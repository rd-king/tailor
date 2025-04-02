from django.db import models
from customer.models import Customer
from PIL import Image


# Create your models here.

class Measurement(models.Model):
    lambai_pent = models.CharField(max_length=10, null=True)
    kamar_pent = models.CharField(max_length=10, null=True)
    seet_pent = models.CharField(max_length=10, null=True)
    mori_pent = models.CharField(max_length=10, null=True)
    jangh_pent = models.CharField(max_length=10, null=True)
    jolo_pent = models.CharField(max_length=10, null=True)
    gothan_pent = models.CharField(max_length=10, null=True)
    lees_pent = models.CharField(max_length=10, null=True)
    lambai_shirt = models.CharField(max_length=10, null=True)
    chati_shirt = models.CharField(max_length=10, null=True)
    bay_shirt = models.CharField(max_length=10, null=True)
    solder_shirt = models.CharField(max_length=10, null=True)
    kamar_shirt = models.CharField(max_length=10, null=True)
    pech_shirt = models.CharField(max_length=10, null=True)
    kolar_shirt = models.CharField(max_length=10, null=True)
    kaf_shirt = models.CharField(max_length=10, null=True)
    measurement_CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='measurement_CustomerId')


class Order(models.Model):
    lambai_pent = models.CharField(max_length=10, null=True)
    kamar_pent = models.CharField(max_length=10, null=True)
    seet_pent = models.CharField(max_length=10, null=True)
    mori_pent = models.CharField(max_length=10, null=True)
    jangh_pent = models.CharField(max_length=10, null=True)
    jolo_pent = models.CharField(max_length=10, null=True)
    gothan_pent = models.CharField(max_length=10, null=True)
    lees_pent = models.CharField(max_length=10, null=True)
    vigat_pent = models.CharField(max_length=200, null=True)
    lambai_shirt = models.CharField(max_length=10, null=True)
    chati_shirt = models.CharField(max_length=10, null=True)
    bay_shirt = models.CharField(max_length=10, null=True)
    solder_shirt = models.CharField(max_length=10, null=True)
    kamar_shirt = models.CharField(max_length=10, null=True)
    pech_shirt = models.CharField(max_length=10, null=True)
    kolar_shirt = models.CharField(max_length=10, null=True)
    kaf_shirt = models.CharField(max_length=10, null=True)
    vigat_shirt = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to="photo", editable=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=10, default='pending')
    order_CustomerId = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='order_CustomerId')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.photo.path)
    #     print(img.size)
    #
    #     if img.height > 480 or img.weight > 480:
    #         output_size = (720, 720)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)
    #
    #         print(img.size)
