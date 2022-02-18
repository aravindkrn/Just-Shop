from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'category', 'price')
    list_filter = ('is_available', 'category')
    ordering = ('-created_date', )


admin.site.register(Product, ProductAdmin)
