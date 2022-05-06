from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import check_password , make_password
from digishop.models import User



class ResetPassword(View):
    def get(self, request):
        return render(request, 'reset-password.html', {'step1': True})

    def post(self, request):
        print(request.POST.get('email'))
        email=request.POST.get('email')
        return HttpResponse(email)
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        error = None;
        if len(password) < 6:
            error = 'Password must be more then 6 char long'
        elif len(repassword) < 6:
            error = 'password must be more then 6 char long'
        elif password != repassword:
            error = 'passoword not matched'

        if error :
            return render(request, 'reset-password.html')
        else:
            email = request.session.get('reset-password-email')
            user = User.objects.get(email = email)
            user.password = make_password(password)
            user.save()
            request.session.clear()
            sendEmailAfterChangePassword(user)
            return render(request , 'login.html' , { 'message' : 'Password Changed..'})


def sendEmailAfterChangePassword(user):
    html = "<h1>Password Changed Succuessfully...</h1>"
    sendEmail(user.name , user.email , 'Password Changed' , htmlContent= html)


def verifyResetPasswordCode(request):
    code = request.POST.get('code')
    sessioncode = request.session['reset-password-verificaion-code']
    if code == str(sessioncode):
        return render(request, 'reset-password.html', {'step3': True})
    else:
        return render(request, 'reset-password.html', {'step2': True})


import math
import random


class PasswordResetVerification(View):
    def post(self, request):
        print(request.POST.get('email'))
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            print(user)
            otp = math.floor(random.random() * 10000000)
            html = f'''

                   <h4>Your Password reset Verification Code is {otp}</h4>

                  '''
            sendEmail("User"
                      , email
                      , "Password Reset Verification Code", html)
            request.session['reset-password-verificaion-code'] = otp
            request.session['reset-password-email'] = email
            return render(request, 'reset-password.html', {'step2': True})
        except:
            return redirect('/reset-password')
