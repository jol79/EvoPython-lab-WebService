from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users', views.users, name='users'),
    path('createNewUser', views.createNewUser, name='createNewUser'),
]
