from django.urls import path

from one_endpoint_rest_api.views import start_endpoint

urlpatterns = [
  path('start', start_endpoint)
]
