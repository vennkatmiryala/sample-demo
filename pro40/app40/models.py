from django.db import models

class ProductModel(models.Model):
    pno = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=30)
    pprice = models.FloatField()
    pquatity = models.IntegerField()
    pimage = models.ImageField(upload_to='product/')
