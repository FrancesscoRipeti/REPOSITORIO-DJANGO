from django.urls import path
from . import views

urlpatterns = [
    path('pagprueba2/', views.pagprueba2, name='pagprueba2'),
    path('pagprueba3/', views.pagprueba3, name='pagprueba3'),
    path('login', views.login, name='login')
]