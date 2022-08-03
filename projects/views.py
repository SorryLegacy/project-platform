from .models import Project
from django.views.generic import DetailView, ListView


class ProjectView(ListView):
    """View single project"""
    model = Project
    template_name = 'projects/projects.html'


class SingleProject(DetailView):
    """View of all projects"""
    model = Project
    template_name = 'projects/single-project.html'

