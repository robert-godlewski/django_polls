# urls file controlls the routing of the apps
# Have to create this from scratch every time and represents the controllers for this app
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]