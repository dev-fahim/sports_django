from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.
from user_profile.forms import RegistrationForm
from user_profile.models import Profile, UserTypeChoice


def register(request):
    registration_form = RegistrationForm()

    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)
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

    context = {
        'form': registration_form
    }

    return render(request, 'user_profile/registration.html', context=context)
