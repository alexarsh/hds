from django.contrib import admin

from django.contrib import admin
from .models import Service, HealthCheck

class ServiceAdmin(admin.ModelAdmin):
    pass

class HealthCheckAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)
admin.site.register(HealthCheck, HealthCheckAdmin)
