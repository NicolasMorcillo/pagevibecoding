from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('registro/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('contenido/', views.educational_content, name='content'),
]
