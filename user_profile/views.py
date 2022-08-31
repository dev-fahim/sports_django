from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user_profile.forms import SignUpForm, LoginForm
from user_profile.models import Profile, UserTypeChoice


def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('sports:all_events'))
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                messages.success(request, 'Welcome ' + user.first_name + ' ' + user.last_name, extra_tags='alert-success')
                login(request, user)
                return redirect(reverse('sports:all_events'))
            else:
                messages.error(request, 'Invalid credentials', extra_tags='alert-danger')
    context = {
        'form': form
    }
    return render(request, 'user_profile/login.html', context=context)


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('user_profile:login'))


def user_signup(request):
    registration_form = SignUpForm()

    if request.method == 'POST':
        registration_form = SignUpForm(data=request.POST)
        if registration_form.is_valid():
            user = User.objects.create_user(
                username=registration_form.cleaned_data.get('email'),
                email=registration_form.cleaned_data.get('email'),
                password=registration_form.cleaned_data.get('password'),
                first_name=registration_form.cleaned_data.get('first_name'),
                last_name=registration_form.cleaned_data.get('last_name'),
            )
            Profile.objects.create(
                user_id=user.id,
                user_type=UserTypeChoice.STUDENT,
                address=registration_form.cleaned_data.get('address'),
                gender=registration_form.cleaned_data.get('gender'),
                phone_number=registration_form.cleaned_data.get('phone_number')
            )
            messages.success(request, 'Please login to continue', extra_tags='alert-success')
            return redirect(reverse('user_profile:login'))

    context = {
        'form': registration_form
    }

    return render(request, 'user_profile/registration.html', context=context)
