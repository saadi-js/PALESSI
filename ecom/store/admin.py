from django.contrib import admin
from .models import Category, Customer, product, Order
from django.utils.html import format_html

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_count')
    search_fields = ('name',)
    ordering = ('name',)
    
    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Products'

# Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_No')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name',)
    ordering = ('last_name', 'first_name')

# Product Admin
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'sale_price', 'is_sale', 'image_preview')
    list_filter = ('category', 'is_sale')
    search_fields = ('name', 'description')
    list_editable = ('is_sale', 'price', 'sale_price')
    ordering = ('-id',)
    list_per_page = 20
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'category', 'description')
        }),
        ('Pricing', {
            'fields': ('price', 'is_sale', 'sale_price')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Image'

# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'quantity', 'price', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')
    list_editable = ('status',)
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_per_page = 25

# Customize Admin Site
admin.site.site_header = 'PALESSI Administration'
admin.site.site_title = 'PALESSI Admin'
admin.site.index_title = 'Welcome to PALESSI Admin Panel'