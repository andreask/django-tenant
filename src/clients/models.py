from django.db import models
from django_tenants.models import DomainMixin
from tenant_users.tenants.models import TenantBase


class Client(TenantBase):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Domain(DomainMixin):
    ...
