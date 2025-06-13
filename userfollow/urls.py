from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    #path('follow/<str:username>/', views.follow_toggle, name='follow_toggle'),
    path('follow-toggle/<str:username>/', views.follow_toggle, name='follow_toggle'),
]
