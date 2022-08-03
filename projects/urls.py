from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectView.as_view(), name="projects"),
    path('project-object/<str:pk>/', views.SingleProject.as_view(), name="project"),
]