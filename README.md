# Tenant test

Test repository to test django-tenants and django-tenants-user.

The instructions here should work, but are not guaranteed. Your mileage may vary.

## Installation

### Database
Create a postgres user and database called `tenant`.

### Install dependencies
Create a virtual python environment and install poetry in it, then run poetry install in the root of the project.

### Migrate database
Run the following command to migrate the public schema database:
```bash
$ ./manage.py migrate_schemas --shared
```

### Create user and tenant (Client)
Run the following command to create a new user and tenant (this shows the first one which NEEDS to be public, public is required):
```python
> from clients.models import Client, Domain
> from users.models import TenantUser
> user = TenantUser.objects.create_user("test@example.com", "password")
> client = Client.objects.create(name="Public", schema_name="public", owner=user)
> domain = Domain.objects.create(domain="localhost", tenant=client)
```

You can now run the application and go to "localhost:8000/"

### Existing views
There are only 2 existing views:
```
/accounts/login
/orders
```

These are available on all other tenants - you can create new ones that should be "subdomains" for localhost. I tried: test.localhost and added it to my hosts file.

## Documentation
Check the following pages for documentation:
* [Django tenants](https://django-tenants.readthedocs.io/en/latest/)
* [Django Tenant Users](https://django-tenant-users.readthedocs.io/en/latest/)
