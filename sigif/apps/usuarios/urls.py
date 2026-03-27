from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('us/', views.usuarios, name='usuarios'),
]