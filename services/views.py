import pytz
from datetime import datetime, timedelta
from django.http import JsonResponse

from services.helpers import service_alive
from services.models import HealthCheck, Service


def health(request):
    statuses = {}
    for service in Service.objects.all():
        statuses[service.url] = 'alive' if service_alive(service) else 'dead'
    return JsonResponse(statuses)


def availability(request):
    availability = {}
    last_hour = datetime.utcnow().replace(tzinfo=pytz.utc) - timedelta(hours=1)
    for service in Service.objects.all():
        total_checks = HealthCheck.objects.filter(service=service, date__gte=last_hour)
        if total_checks.count() < 60:
            #Maybe the Health checking was down for some reason
            availability[service.url] = "Not known"
        else:
            availability[service.url] = '%s%%' % int(total_checks.filter(alive=True).count() / total_checks.count() * 100)
    return JsonResponse(availability)
