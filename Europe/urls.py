from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'), 
    path('create/', views.create_trip, name='create_trip')
]
