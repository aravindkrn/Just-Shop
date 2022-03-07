from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    readonly_fields = ('modified_date',)
    fields = ('product', 'product_quantity', 'modified_date')
    # can_delete = False
    ordering = ('-modified_date',)
    extra = 0

    # def has_add_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemInline,)
    readonly_fields = ('created_date',)

    class Media:
        css = {"all": ("css/hide_admin_object_name.css",)}


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
