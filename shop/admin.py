from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
