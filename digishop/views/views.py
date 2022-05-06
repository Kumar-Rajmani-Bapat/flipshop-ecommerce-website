from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from digishop.models import Product, ProductImages, User
from django.db.models import Q


class searchbar(View):
    def searchbar(request,product_id):
        product = Product.objects.get(id=product_id)
        search = request.GET.get('search')
        post = Product.objects.filter(product=search)
        return (post,"under develpment")