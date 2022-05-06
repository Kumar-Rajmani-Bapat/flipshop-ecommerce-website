from django.shortcuts import render, HttpResponse, redirect
from digishop.models import Product, ProductImages, User
from django.template import loader


def index(request):
    products = Product.objects.filter(active=True)
    print(products)
    data = {
        'products': products
    }
    return render(request, 'index.html', data)


def logout(request):
    request.session.clear()
    return redirect('index')


def profile(request):
    try:
        user_id = request.session.get('user').get('id')
        user = request.session.get('user')
        email = user.get('email')

        user = request.session.get('user')
        userObject = User.objects.get(id=user.get('id'))
        q = userObject

        c = ["<br> <br> <br> <b><u> YOUR PROFILE <br> <br> <br> </u>",
             "<b>  Name :", "\n", q, " <br> <br> <br> ",
             "UserId :", "\n", user_id, " <br> <br> <br> ",
             " Email :", "\n", email,
             "<br> <br> <br> Kindly go ← back to continue to Flipshop ",
             ]

        return HttpResponse(c)
    except:

        return render(request,'login.html')




