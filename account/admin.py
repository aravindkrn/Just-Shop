from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'is_active', )
    list_display_links = ('email', 'first_name', )
    search_fields = ('email', 'first_name', 'last_name', 'username', )
    list_filter = ('is_active', )
    readonly_fields = ('date_joined', 'last_login', )
    ordering = ('-date_joined', )

    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
