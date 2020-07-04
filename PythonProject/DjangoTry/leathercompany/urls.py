from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registerRawMaterial', views.login, name='registerRawMaterials'),
    path('listOfRawMaterials', views.logout, name='listOfRawMaterials'),
]