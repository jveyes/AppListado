from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('db/', views.db, name='db'),
    path('applistado/', views.mysql, name='applistado'),
    #path('users/', views.user_list, name='user_list'),
]