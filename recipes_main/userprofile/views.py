from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from .forms import ProfileTypeForm

User = get_user_model()

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        error = False
        if not username: 
            messages.error(request, _('You did not entered username'))
            error = True
        if User.objects.filter(username=username).first():
            messages.error(request, _('That user already exists'))
            error = True
        if not email:
            messages.error(request, _('Email not entered'))
            error = True
        if User.objects.filter(email=email).first():
            messages.error(request, _('This email is already taken'))
        else:
            try:
                validate_email(email)
            except:
                messages.error(request, 'Invalid email')
        if not password or not password2 or password != password2:
            messages.error(request, _('Password not entered or did not match'))
            error = True
        if not error:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f"_('User') {username} _('was created. You can now log in.) ")
            return redirect('login')
    return render(request, 'registration/register.html')


@login_required
@csrf_protect
def profile(request):
    context = {}
    context['form'] = ProfileTypeForm()
    form = ProfileTypeForm(request.POST)
    tipas = form.save(commit=False)
    tipas.save()

    return render( request, 'user_profile/profile.html', context)