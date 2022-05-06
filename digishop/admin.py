from django.contrib import admin
from digishop.models import ProductImages, Product, User, Payment
from digishop.models import Address
from django.utils.html import format_html
from instamojo_wrapper import Instamojo
from minishop.settings import PAYMENT_API_AUTH_TOKEN, PAYMENT_API_KEY

API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN)


class ProductImageModel(admin.StackedInline):
    model = ProductImages


class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_description', 'get_price', 'get_discount', 'get_sale_price', 'file',
                    'thumbnail']

    inlines = [ProductImageModel]

    def get_thumbnail(self, obj):
        return format_html(f'''
            <img height='80px' src='{obj.thumbnail.url}'/>
        ''')

    def get_sale_price(self, obj):
        return 'INR ' + str((obj.price) - (obj.price * (obj.discount / 100)))

    def get_description(self, obj):
        return format_html(f'<span title="{obj.description}">{obj.description[0:50]}....</span>')

    def get_price(self, obj):
        return 'INR ' + str(obj.price)

    def get_discount(self, obj):
        return str(obj.discount) + " %"

    get_sale_price.short_description = "Sale Price"
    get_discount.short_description = "Discount"
    get_price.short_description = "Original Price"


class UserModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'active']
    sortable_by = ['id', 'name']
    list_editable = ['active']


# Payment Model
class PaymentModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_user', 'get_product',
                    'payment_request_id',
                    'payment_id',
                    'status', 'created_at'
                    ]
    list_editable = ['status', 'user']

    def get_user(self, obj):
        return format_html(f'<a target="_blank" href="/admin/digishop/user/{obj.user.id}">{obj.user}</a>')

    def get_product(self, obj):
        return format_html(f'<a target="_blank" href="/admin/digishop/product/{obj.product.id}">{obj.product}</a>')

    get_user.short_description = 'User Details'
    get_product.short_description = 'Product'


class AddressModel(admin.ModelAdmin):

    fields = ('address')

admin.site.register(Product, ProductModel)
admin.site.register(User, UserModel)
admin.site.register(Payment, PaymentModel)
#admin.site.register(Address,AddressModel)
