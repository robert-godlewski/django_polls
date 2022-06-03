# urls file controlls the routing of the apps
# Have to create this from scratch every time and represents the controllers for this app
from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
