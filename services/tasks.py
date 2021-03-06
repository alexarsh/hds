from celery import shared_task
from datetime import datetime
import pytz

from services.helpers import service_alive
from services.models import Service, HealthCheck


@shared_task
def check_health_statuses():
    for service in Service.objects.all():
        HealthCheck(service=service, alive=service_alive(service), date=datetime.utcnow().replace(tzinfo=pytz.utc)).save()