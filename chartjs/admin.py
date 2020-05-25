from django.contrib import admin

from .models import OrganizationUser, Date

admin.site.register(OrganizationUser)
admin.site.register(Date)