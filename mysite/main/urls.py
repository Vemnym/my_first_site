from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
    path('project/<int:number_of_project>', views.project),
    path('list_projects', views.list_projects),
    path('create_project', views.create_project)
]