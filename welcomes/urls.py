from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users', views.users, name='users'),
    path('create_new_user', views.create_new_user, name='create_new_user'),
]
