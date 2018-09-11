import json, requests
from unittest.mock import patch
from django.test import TestCase

from services.helpers import service_alive
from services.models import Service

class TestHealthChecks(TestCase):

    def setUp(self):
        for url in ['https://bim360dm-dev.autodesk.com/health?self=true',
                    'https://commands.bim360dm-dev.autodesk.com/health',
                    'https://360-staging.autodesk.com/health']:
            Service.objects.create(url=url)

    @patch.object(requests, 'get')
    def test_service_alive(self, mockget):
        mockget.return_value.status_code = 200

        # Test dict
        mockget.return_value.text = "{'status':{'overall':'GOOD'}}"
        self.assertTrue(service_alive(Service.objects.all()[0]))
        mockget.return_value.text = "{'status':{'overall':'OK'}}"
        self.assertTrue(service_alive(Service.objects.all()[0]))
        mockget.return_value.text = "{'status':{'overall':'NOT OK'}}"
        self.assertFalse(service_alive(Service.objects.all()[0]))

        # Test xml
        mockget.return_value.text = '<HealthCheck><status>Good</status></HealthCheck>'
        self.assertTrue(service_alive(Service.objects.all()[0]))
        mockget.return_value.text = '<HealthCheck><status>Not Good</status></HealthCheck>'
        self.assertFalse(service_alive(Service.objects.all()[0]))

        # Test error
        mockget.return_value.text = '<HealthCheck><status>Good</status></HealthCheck>'
        mockget.return_value.status_code = 400
        self.assertFalse(service_alive(Service.objects.all()[0]))

    @patch.object(requests, 'get')
    def test_health_view(self, mockget):
        mockget.return_value.status_code = 200
        mockget.return_value.text = "{'status':{'overall':'GOOD'}}"
        number_of_services = Service.objects.count()

        # Test alive
        response = self.client.get('/services/health/')
        self.assertEqual(list(json.loads(response.content).values()), ['alive'] * number_of_services)

        # Test dead
        mockget.return_value.text = "{'status':{'overall':'NOT GOOD'}}"
        response = self.client.get('/services/health/')
        self.assertEqual(list(json.loads(response.content).values()), ['dead'] * number_of_services)

    def test_availability(self):
        # No checks run
        number_of_services = Service.objects.count()
        response = self.client.get('/services/availability/')
        self.assertEqual(list(json.loads(response.content).values()), ['Not known'] * number_of_services)