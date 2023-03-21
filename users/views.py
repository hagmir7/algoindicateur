from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.views.generic import ListView, DetailView, UpdateView, UpdateView
from django.contrib.auth.models import User
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.http import JsonResponse
import smtplib
from email.message import EmailMessage
from django.utils.translation import gettext_lazy as _



# LOGIN
def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    alert = False
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if authenticate(username=username, password=password):
                user = authenticate(username=username, password=password)
                login(request, user)
                if request.user.is_superuser:
                    return redirect('/dash')
                else:
                    return redirect('/products')

            else:
                messages.add_message(request, messages.ERROR, _('Password is incorrect!'))
                return redirect('login')
        if next:
            return redirect(next)

    
    context = {'form': form,'alert':alert, 'title': _("Log in")}
    return render(request, "registrations/login.html", context)

# Welcom Message   
def email_message(obj, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = obj
    msg['to'] = to
    username = 'hagmir7@gmail.com'
    msg['from'] = username
    password = 'jfpgqzkxetgyjbvo'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()



import json
import urllib.request

# REGISTER 
def register(request):
    block_name = False
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                username = form.cleaned_data['username']
                email = new_user.email
                new_user.save()
                if new_user is not None:
                    if new_user.is_active:
                        login(request, new_user)
                        return redirect('home')
                    
                return redirect('login')
    context = {'title': _('Register'), 'form': form, }
    return render(request, 'registrations/register.html', context)


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile/profile.html'
    count_hit = True

    def get_context_data(self, *arge, **kwargs):
        context = super(ProfileView, self).get_context_data(*arge, **kwargs)
        page = get_object_or_404(Profile, slug=self.kwargs['slug'])
        title = f'{page.user.first_name} {page.user.last_name}'
        description = _('You can join now to connect with your  friends and enjoy your books and courses register now')
        context["page"] = page
        context['description'] = f'{title} {description}'
        return context




def ProfileUpdate(request, id):
    profile = get_object_or_404(Profile, id=id)
    form = UpdateProfile(instance=profile)
    if request.method == "POST":
        if request.user == profile.user:
            form = UpdateProfile(request.POST, instance=request.user.profile, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('profile_update', id=profile.id)
        else:
            return redirect('/')
        

    context = {
        'page': profile,
        'title': _('Update Profile')
    }

    return render(request, 'profile/update_profile.html', context)


class ProfileViewUpdate(UpdateView):
    model = Profile
    template_name = 'profile/update_profile.html'
    form_class = UpdateProfile

    def get_context_data(self, *arge, **kwargs):
        context = super(ProfileViewUpdate, self).get_context_data(*arge, **kwargs)
        page = get_object_or_404(Profile, id=self.kwargs['pk'])
        title = _('Update Profile')
        context["page"] = page
        context["title"] = title
        return context
    


 



    

def user_update_info(request):
    confirm = False
    if request.method == 'POST':
        form = UserUpdateInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            confirm = True
    else:
        form = UserUpdateInfo(instance=request.user)
    context = {'form': form, 'confirm':confirm, 'title': _("Contact information")}
    return render(request, 'profile/user_update_info.html', context)



from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile/change-password.html', {'form': form})





def posword_reset_done(request):
    context = {'title':_("Password reset has been sent")}
    return render(request, 'password_reset/reset_password_done.html', context)


def settings(request):
    return render(request, 'settings.html')


        


