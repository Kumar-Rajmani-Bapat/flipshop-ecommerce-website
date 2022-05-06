from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from digishop.models import Product, ProductImages, User
from django.db.models import Q


def productDetails(request, product_id):
    product = Product.objects.get(id=product_id)
    images = ProductImages.objects.filter(product=product_id)
    can_download = False
    try:
        session_user = request.session.get('user')
        if session_user:
            user_id = session_user.get('id')
            user = User(id=user_id)
            payment = Payment.objects.filter(~Q(status="Failed"), product=product, user=user)
            if len(payment) != 0:
                can_download = True
    except:
        pass;
    return render(request, 'product_details.html',
                  {
                      'product': product,
                      'images': images,
                      'can_download': can_download

                  })
