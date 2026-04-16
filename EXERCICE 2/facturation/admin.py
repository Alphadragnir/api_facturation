from django.contrib import admin
from .models import Product, Invoice, InvoiceItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'expiration_date', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'expiration_date')
    ordering = ('-created_at',)

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total', 'get_item_count')
    list_filter = ('created_at',)
    inlines = [InvoiceItemInline]
    readonly_fields = ('total', 'created_at', 'updated_at')

    def get_item_count(self, obj):
        return obj.get_total_quantity()
    get_item_count.short_description = 'Nombre de produits'

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity', 'unit_price', 'get_subtotal')
    list_filter = ('invoice', 'created_at')
    search_fields = ('product__name',)

    def get_subtotal(self, obj):
        return obj.get_subtotal()
    get_subtotal.short_description = 'Sous-total'
