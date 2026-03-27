from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('crear_productos/', views.crear_producto, name='crear_productos'),
    path('listar_productos/', views.listar_producto, name='listar_productos'),
    path('actualizar_productos/<int:id>/', views.actualizar_producto, name='actualizar_productos'),
    path('eliminar_productos/<int:id>/', views.eliminar_producto, name='eliminar_productos'),
]