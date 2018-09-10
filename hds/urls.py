from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('services/', include('services.urls')),
    path('', admin.site.urls)
]
