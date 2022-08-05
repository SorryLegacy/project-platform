from django.urls import path
from . import views


urlpatterns = [
    path('', views.Profiles.as_view(), name='profiles'),
    path('profile/<str:pk>/', views.ProfileView.as_view(), name='single-profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', views.AccountView.as_view(), name='account')
]