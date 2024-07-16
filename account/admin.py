from django.contrib import admin
from .models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'is_active')
    ordering = ('-created_at',)
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('password', 'created_at', 'updated_at')


admin.site.register(Account, AccountAdmin)