from django.db import models


class Service(models.Model):
    url = models.URLField()

    def __str__(self):
        return u'%s' % self.url


class HealthCheck(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    alive = models.BooleanField(default=False)

    def __str__(self):
        return u'Service %s is %s on %s' % (self.service, 'alive' if self.alive else 'dead', self.date)

