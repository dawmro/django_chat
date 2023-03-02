from django.urls import path

from . import views


urlpatterns = [
    # path is empty because in main url file 'rooms' will be set as prefix 
    path('', views.rooms, name='rooms')
]