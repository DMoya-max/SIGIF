from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('us/', views.usuarios, name='usuarios'),
    path('crear_usuarios/', views.crear_usuarios, name='crear_usuarios'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('editar_usuarios/<int:id>/', views.editar_usuarios, name='editar_usuarios'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
]