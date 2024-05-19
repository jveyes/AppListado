from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testdb/', views.testdb, name='testdb'),
    path('applistado/', views.applistado, name='applistado'),
    #path('users/', views.user_list, name='user_list'),
]