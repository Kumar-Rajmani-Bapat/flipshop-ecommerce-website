from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import check_password
from digishop.models import User
import random
import math
from digishop.utils.email_sender import sendEmail
import sys


def sendOtp(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    otp = math.floor(random.random() * 10000000)

    html = f'''
        <h4>Hello {name} ,</h4>
        </br>
        <p>your Varifaction Code is <b>{otp}</b></p>
        </br>
        <p>if you didnt requested verification code , you can ignore this email</p>

    '''
    print(name, email)
    if name and email:
        response = sendEmail(name=name, email=email, htmlContent=html, subject="verify Email")

        try:
            if (response.json()['messageId']):
                request.session['verification-code'] = otp
                return HttpResponse("{'message' : 'success'}", status=200)

            else:
                return HttpResponse(sys.exc_info()[0], status=400)
        except:
            return HttpResponse(sys.exc_info()[0], status=400)


def verifyCode(request):
    try:
        code = request.POST.get('code')
        otp = request.session.get('verification-code')
        print(code, otp)

        if (str(otp) == code):
            return HttpResponse("{'message' : 'success'}", status=200)

        else:
            return HttpResponse(sys.exc_info()[0], status=400)
    except:
        return HttpResponse(sys.exc_info()[0], status=400)
