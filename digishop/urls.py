
from django.contrib import admin
from django.conf import settings
from django.urls import path
from digishop.views import index
from digishop.views import LoginView,SignupView
from digishop.views.changepassword import ChangePassword
from digishop.views.products import productDetails
from digishop.views.download import downloadFree,downloadPaidProduct
from digishop.views.payment import createPayment,verifyPayment
from digishop.middleware.login_required_middleware import login_required
from digishop.middleware.can_not_access_after_login import cantAccessAfterLogin
from digishop.views.orders import my_orders
from digishop.views.reset_password import ResetPassword, PasswordResetVerification, verifyResetPasswordCode
from digishop.views.views import searchbar
from digishop.views.address import AddressView

urlpatterns = [
    path('',index.index, name='index'),
    path('logout',index.logout, name='logout'),
    path('orders',login_required(my_orders), name='orders'),
    path('login',cantAccessAfterLogin(LoginView.as_view()), name='login'),
    path('signup',cantAccessAfterLogin(SignupView.as_view()), name='signup'),
    path('product/<int:product_id>', productDetails , name='details'),
    path('download-free/<int:product_id>', downloadFree, name='downloadfree'),
    path('create-payment/<int:product_id>', login_required(createPayment), name='create-payment'),
    path('complete-payment', login_required(verifyPayment), name='verify-payment'),
    path('download/paidproduct/<int:product_id>', downloadPaidProduct, name='download-paidproducts'),
    path('reset-password', ResetPassword.as_view(), name='reset-password'),
    path('reset-password-verification', PasswordResetVerification.as_view(), name='reset-password-verfication'),   path('verify-reset-password-code', verifyResetPasswordCode),
    path('reset-password-verification', PasswordResetVerification.as_view(), name='reset-password-verfication'),
    path('profile',index.profile,name='profile'),
    path('changepassword', ChangePassword.as_view(), name='changepassword'),
    path('searchbar',searchbar.as_view(),name='searchbar'),
    path('address',AddressView.as_view(),name='address')
]