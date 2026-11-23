from django.contrib import admin
from .models import Sweet,Cake,Namkeen

@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price_per_kg',
        'stock',
        'is_available'
    )
    list_filter = ('category', 'is_available')
    search_fields = ('name',)
    

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price_per_kg',
        'stock',
        'is_available'
    )
    list_filter = ('category', 'is_available')
    search_fields = ('name',)

@admin.register(Namkeen)
class NamkeenAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_kg', 'stock', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)