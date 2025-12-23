from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

    class Meta:
       verbose_name_plural = "Categories"

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_No = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,default=0, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.TextField(max_length=500, default='', blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True,default=0, blank=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name}"