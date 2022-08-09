from django.urls import path
from . import views


urlpatterns = [
    path('', views.Profiles.as_view(), name='profiles'),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name='single-profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', views.AccountView.as_view(), name='account'),
    path('account/update/<str:pk>/', views.UpdateAccount.as_view(), name='update-account'),
    path('account/delete/<str:pk>/', views.DeleteAccount.as_view(), name='delete-account'),
    path('skill/create-skill/', views.CreateSkill.as_view(), name='create-skill'),
    path('skill/update-skill/<slug:slug>/', views.UpdateSkill.as_view(), name='update-skill'),
    path('skill/delete-skill/<slug:slug>/', views.DeleteSkill.as_view(), name='delete-skill')
]