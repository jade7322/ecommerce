from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Product(models.Model):
    prdtname=models.CharField(max_length=20)
    prdtdescription=models.TextField()
    prdtimage=models.ImageField(upload_to='image',default='')
    prdtprice=models.IntegerField()
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    stock=models.IntegerField(default=1)
    def __str__(self):
        return self.prdtname
class Cartuser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user
class Item(models.Model):
    user=models.ForeignKey(Cartuser,on_delete=models.CASCADE,default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def total(self):
        return self.product.prdtprice * self.quantity
    def __str__(self):
        return self.product
class Orderdetails(models.Model):
    country=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    address=models.TextField()
    state=models.CharField(max_length=20)
    postal=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    subtotal=models.IntegerField(default=1)
    def __str__(self):
        return self.first_name
class Orderitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_details=models.ForeignKey(Orderdetails,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    def __str__(self):
        return self.product


