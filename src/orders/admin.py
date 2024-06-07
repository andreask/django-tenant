from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'amount')
