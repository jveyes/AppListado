from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('db/', views.db, name='db'),
    path('applistado/', views.applistado, name='applistado'),
    #path('users/', views.user_list, name='user_list'),
]