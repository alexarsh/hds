import ast
from django.conf import settings
import requests
import xmltodict

def service_alive(service):
    try:
        response = requests.get(service.url, timeout=settings.SERVICE_PING_TIMEOUT)
        if response.status_code == 200:
            try:
                # Got dict
                return ast.literal_eval(response.text)["status"]["overall"] in ["GOOD", "OK"]
            except SyntaxError:
                # Got xml
                return xmltodict.parse(response.text)["HealthCheck"]["status"] == "Good"
            except Exception as e:
                pass
    except requests.exceptions.ConnectTimeout:
        # Got timeout
        pass
    return False