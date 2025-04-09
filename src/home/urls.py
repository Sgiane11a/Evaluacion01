from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('invitation/', views.invitation, name='invitation'),
    path('guest-user-list/', views.guest_user_list, name='guest-user-list'),
]