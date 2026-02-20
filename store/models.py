from django.db import models

# Create your models here.
class Product(models.Model):
    code=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=50,unique=True)
    stock=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='products/')

    def __str__(self):
           return f"{self.code}-{self.name}"


