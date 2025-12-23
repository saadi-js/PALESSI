from django.contrib import admin
from .models import Category, Customer, product, Order
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(product)
admin.site.register(Order)