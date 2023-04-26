from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, \
    PProfileCreationForm, DProfileCreationForm


def home(request):
    return render(request, 'users/home.html')


@login_required
def profile(request):
    return HttpResponse("Profile")


def register(request):
    return render(request, 'users/ask_register.html')


def try_register(u_form, p_form, Type):
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.Type = Type
        user.save()
        prof = p_form.save(commit=False)
        prof.user = user
        prof.save()
        username = u_form.cleaned_data.get('username')
        return f'Account for {username} is created successfully as patient'

    return None


def register_p(request):
    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST)
        p_form = PProfileCreationForm(request.POST)

        msg = try_register(u_form, p_form, 1)
        if msg is not None:
            messages.success(request, msg)
            return redirect('login')

    else:
        u_form = CustomUserCreationForm()
        p_form = PProfileCreationForm()

    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})


def register_d(request):
    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST)
        p_form = DProfileCreationForm(request.POST)

        msg = try_register(u_form, p_form, 2)
        if msg is not None:
            messages.success(request, msg)
            return redirect('login')
    else:
        u_form = CustomUserCreationForm()
        p_form = DProfileCreationForm()

    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})
