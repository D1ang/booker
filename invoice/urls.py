from django.urls import path
from .views import generate_invoice


urlpatterns = [
    path('generate/', generate_invoice, name='generate_invoice')
]
