from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('certification/', views.certification, name='certification'),
    path('cv/', views.cv, name='cv'),
    path('contact/', views.contact, name='contact'),
    path('upload-project/', views.upload_project, name='upload_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
]