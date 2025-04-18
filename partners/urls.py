from django.urls import path

from .views import partner_list, partner_add

app_name = 'partners'

urlpatterns = [
    path('', partner_list, name='partner-list'),
    path('be-partner/', partner_add, name='partner-add'),
]