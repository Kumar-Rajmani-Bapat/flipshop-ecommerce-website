from django.shortcuts import render, HttpResponse, redirect
from digishop.models import Product, ProductImages, User, Payment
from django.db.models import Q


def my_orders(request):
    user_id = request.session.get('user').get('id')
    user = User(id=user_id)
    payments = Payment.objects.filter(~Q(status="Failed"), user=user)
    return render(request, 'orders.html', {'orders': payments});
