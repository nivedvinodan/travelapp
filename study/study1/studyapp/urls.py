from . import views
from django.urls import path

urlpatterns =[
    path('', views.study, name="study"),

    # path('add/',views.addition,name="addition")

]