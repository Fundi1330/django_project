from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_post/', views.AddPostView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('login', views.Login.as_view()),
    path('post/<int:id>', views.PostView.as_view(), name='post'),
    path('profile/<username>', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', views.EditProfileView.as_view())
]