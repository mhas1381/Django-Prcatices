from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('' , home , name = "home"),
    path('post/<int:id>/' , single_post , name="post"),
]

