from django.contrib import admin
from .models import Order


@admin.register(Order)
class AdminProduct(admin.ModelAdmin):
    list_display = ('number_order', 'date_order', 'contractor', 'description', 'price_order',)
    list_filter = ('number_order', 'date_order', 'contractor',)
