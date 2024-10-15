# admin_app/urls.py

from django.urls import path
from .views import admin_create, admin_list, admin_detail, admin_update
from . import views

urlpatterns = [
    path('create/', views.admin_create, name='admin_create'),
    path('list/', admin_list, name='admin_list'),
    path('detail/<int:pk>/', admin_detail, name='admin_detail'),
    path('update/<int:pk>/', admin_update, name='admin_update'),
    path('profile/<int:pk>/delete/', views.admin_delete, name='admin_delete'), 
]