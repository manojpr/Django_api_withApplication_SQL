from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_dropdowns, name='filter_dropdowns'),
    path('ajax/filter_dropdowns/', views.filter_dropdowns_ajax, name='filter_dropdowns_ajax'),
    path('ajax/filter_new_dropdowns/', views.filter_new_dropdowns, name='filter_new_dropdowns'),
    path('api/filter_pies_api/', views.filter_pies_api_view, name='filter_pies_api'),
    path('fetch_api_results/', views.filter_pies_view, name='fetch_api_results'),
]