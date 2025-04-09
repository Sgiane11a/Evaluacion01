from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_user_list, name='guest_user_list'),
    path('create/', views.guest_user_create, name='guest_user_create'),
    path('<int:user_id>/', views.guest_user_detail, name='guest_user_detail'),
    path('<int:user_id>/update/', views.guest_user_update, name='guest_user_update'),
    path('<int:user_id>/delete/', views.guest_user_delete, name='guest_user_delete'),
]