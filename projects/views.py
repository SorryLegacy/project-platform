from .models import Project
from .forms import ProjectForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


class ProjectView(ListView):
    """View single project"""
    model = Project
    template_name = 'projects/projects.html'


class SingleProject(DetailView):
    """View of all projects"""
    model = Project
    template_name = 'projects/single-project.html'


class CreateProjectView(CreateView):
    """View for create project"""
    model = Project
    form_class = ProjectForm
    template_name = 'projects/create-project.html'


class UpdateProject(UpdateView):
    """View for update project"""
    model = Project
    form_class = ProjectForm
    template_name = 'projects/update-project.html'
    success_url = reverse_lazy('projects')


class DeleteProject(DeleteView):
    """View for delete project"""
    model = Project
    template_name = 'projects/delete-project.html'
    success_url = reverse_lazy('projects')
