from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectView.as_view(), name="projects"),
    path('project-object/<str:pk>/', views.SingleProject.as_view(), name="project"),
    path('craete-project', views.CreateProjectView.as_view(), name="create-project"),
    path('project-object/<str:pk>/update', views.UpdateProject.as_view(), name="update-project"),
    path('project-object/<str:pk>/delete', views.DeleteProject.as_view(), name="delete-project"),
]