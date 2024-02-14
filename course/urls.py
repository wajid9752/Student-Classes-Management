from django.urls import path
from .views import *

urlpatterns=[
    path('' , home , name="home"),
    path('user_logout/' , user_logout , name="logout"),
    path('login/' , user_login , name="login"),
    path('add-attendance/<int:pk>/' , add_attendance , name="add-attendance"),
]