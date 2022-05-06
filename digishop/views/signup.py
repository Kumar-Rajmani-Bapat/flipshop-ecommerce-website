from django.views import View
from django.shortcuts import render, redirect
from digishop.models import User
from django.contrib.auth.hashers import make_password


class SignupView(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            hashedPassword = make_password(password=password)
            user = User(name=name, email=email, password=hashedPassword, phone=phone)
            result = user.save()
            return render(request, 'login.html')
        except:
            return render(request, 'signup.html', {'error': "User Already Registered.."})
