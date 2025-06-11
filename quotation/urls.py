from django.urls import path
from .views import generate_quotation


app_name = 'quotation'

urlpatterns = [
    path('generate/', generate_quotation, name='generate_quotation'),
]
