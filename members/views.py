from cProfile import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from members.forms import EditProfileForm, EditProfilePageForm, ProfilePageForm, SignUpForm,PasswordChangingForm,ProfilePageForm,EditProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView,CreateView
from blog.models import Profile
class UserSignupView(generic.CreateView):
    form_class=SignUpForm
    template_name ='registration/signup.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name ='registration/editprofile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    template_name ='registration/changepassword.html'
    success_url=reverse_lazy('home')
class ShowProfilePageView(DetailView):
    model=Profile
    template_name='registration/user-profile.html'

    def get_context_data(self,*args,**kwargs):
        users=Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user= get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model =Profile
    form_class=EditProfilePageForm
    template_name='registration/editprofilepage.html'
    #fields =['bio','profile_pic','website_url','fb_url','twitter_url','instagram_url','linkedin_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class= ProfilePageForm
    template_name = 'registration/createprofile.html'
    #fields = '__all__'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

