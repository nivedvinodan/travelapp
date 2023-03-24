from . import views
from django.urls import path

urlpatterns = [
    path('registerForm/', views.register2, name="register2"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
