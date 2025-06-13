from django.urls import path
from .views import quotation_details, generate_quotation


app_name = 'quotation'

urlpatterns = [
    path('details/<str:quotation_number>/', quotation_details, name='quotation_details'),
    path('generate/', generate_quotation, name='generate_quotation'),
]
