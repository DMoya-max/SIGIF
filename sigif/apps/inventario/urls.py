from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario, name='inventario'),
    path('inv_historial/', views.inv_historial, name='inv_historial'),
    path('inv_control/', views.inv_control, name='inv_control'),
]