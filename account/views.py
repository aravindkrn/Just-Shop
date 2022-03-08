from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView

from .forms import RegistrationForm
from .models import Account


class RegisterView(APIView):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'account/register.html', context=context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')

            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password)
            user.phone_number = phone_number
            user.save()

            messages.success(request, 'Registration Success!')
            return redirect('register')

        context = {'form': form}
        return render(request, 'account/register.html', context=context)


class LoginView(APIView):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

        auth.login(request, user)
        return redirect('home')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are successfully logged out!')
    return redirect('login')
