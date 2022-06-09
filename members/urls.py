from django.urls import path
from .views import ShowProfilePageView, UserSignupView , UserEditView,PasswordsChangeView ,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
from django.contrib.auth import views as auth_views
urlpatterns=[
   
path('signup/',UserSignupView.as_view(),name="signup"),
path('editprofile/',UserEditView.as_view(),name="editprofile"),
path('password/',PasswordsChangeView.as_view(template_name='registration/changepassword.html')),
path('<int:pk>/profile/',ShowProfilePageView.as_view(),name="profile_page"),
path('<int:pk>/edit-profile-page/',EditProfilePageView.as_view(),name="edit_profile_page"), 
path('create-profile-page/',CreateProfilePageView.as_view(),name="create_profile"),

]