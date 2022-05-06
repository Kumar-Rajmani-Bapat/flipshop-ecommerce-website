from django.shortcuts import render, HttpResponse, redirect
from digishop.models import Product, ProductImages, User, Payment


def downloadFree(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.discount == 100:
            return redirect(product.link)
        else:
            return redirect(product.file.url);
    except:
        return redirect('index');


def downloadPaidProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    session_user = request.session.get('user');
    user = User(session_user.get('id'))
    payment = Payment.objects.filter(user=user, product=product);
    if (len(payment) > 0):
        print(len(payment))
        file = product.file
        if file:
            return redirect(product.file.url)
        else:
            return redirect(product.link)
    else:
        return redirect('index')

def proimages(request, product_id):

    return redirect(Product.thumbnail)