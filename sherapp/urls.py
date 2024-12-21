from django.urls import path
from .views import *

app_name='sherapp'

urlpatterns=[
    path("",home,name='home'),
    path("courses/",course,name='courses'),
]