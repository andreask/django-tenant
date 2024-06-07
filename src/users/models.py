from django.db import models
from tenant_users.tenants.models import UserProfile


class TenantUser(UserProfile):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
