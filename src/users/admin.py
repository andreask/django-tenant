from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from users.models import TenantUser


@admin.register(TenantUser)
class TenantUserAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active')
