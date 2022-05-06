from django.views import View
from django.shortcuts import render, redirect
from digishop.models import Address


class AddressView(View):

    def get(self, request):
        return render(request, 'address.html')

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            pincode = request.POST.get('pincode')


            add =(name, email, phone, address, pincode)
            print(add)
            Address.models.Model.save(pincode, address)
            address.save()


        except:
            return render(request,'login.html')
