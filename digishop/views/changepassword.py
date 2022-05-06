from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from digishop.models import User



class ChangePassword(View):
    def get(self, request):
        return render(request, 'changepassword.html')

    def post(self, request):
        print(request.POST.get('email'))
        email=request.POST.get('email')

        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None;

        if password != repassword:
            error = 'password not matched'
            print(error)
        if error :
            return render(request, 'changepassword.html')
        else:

            user = User.objects.get(email = email)
            user.password = make_password(password)
            user.save()
            request.session.clear()

            return render(request , 'login.html' , { 'message' : 'Password Changed..'})






