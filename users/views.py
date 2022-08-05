from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import User, Profile, Skill
from .forms import UserForm, ProfileForm, SkillForm


class Profiles(ListView):
    """"""
    model = Profile
    template_name = 'users/profiles.html'


class ProfileView(DetailView):
    """"""
    model = Profile
    template_name = 'users/single-profile.html'


class AccountView(LoginRequiredMixin, ListView):
    """"""
    model = Profile
    template_name = 'users/account.html'

    def get_queryset(self):
        """"""
        return Profile.objects.get(user=self.request.user)


class SignUp(CreateView):
    """Class for sign up people"""
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
