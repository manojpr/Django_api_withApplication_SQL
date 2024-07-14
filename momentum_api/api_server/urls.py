from django.urls import path
from . import views

urlpatterns = [
path('api/filter_pies_api/', views.filter_pies_api, name='filter_pies_api')
]