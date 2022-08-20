from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView


from .models import User, Profile, Skill
from .seralizers import ProfileSerializer
from .forms import UserForm, ProfileForm, SkillForm


class Profiles(ListView):
    """View to see all profiles"""
    model = Profile
    template_name = 'users/profiles.html'


class ProfileView(DetailView):
    """View to see single profile with all info"""
    model = Profile
    template_name = 'users/single-profile.html'


class AccountView(LoginRequiredMixin, ListView):
    """View for user who want to see his profile"""
    model = Profile
    template_name = 'users/account.html'

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)


class UpdateAccount(LoginRequiredMixin, UpdateView):
    """View for update data for UserAccount"""
    model = Profile
    form_class = ProfileForm
    template_name = 'users/update-account.html'
    success_url = reverse_lazy('account')


class DeleteAccount(LoginRequiredMixin, DeleteView):
    """View for Delete Account"""
    model = Profile
    success_url = reverse_lazy('projects')
    template_name = 'users/delete-account.html'


class CreateSkill(LoginRequiredMixin, CreateView):
    """View for create skill"""
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('account')
    template_name = 'users/create-skill.html'


class UpdateSkill(LoginRequiredMixin, UpdateView):
    """View for update skill"""
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('account')
    template_name = 'users/update-skill.html'


class DeleteSkill(LoginRequiredMixin, DeleteView):
    """View for delete skill"""
    model = Skill
    success_url = reverse_lazy('account')
    template_name = 'users/delete-skill'


class SignUp(CreateView):
    """View for sign up people"""
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class ProfileGetPost(ListCreateAPIView):
    """API for POST and Get request to Profile"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdateDeleteRetrieve(RetrieveUpdateDestroyAPIView):
    """API for PUT, PATCH and DELETE request to Profile"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
