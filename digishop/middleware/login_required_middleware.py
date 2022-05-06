from django.shortcuts import render, redirect


def login_required(get_response):
    # // index

    def middleware(request, product_id=None):
        user = request.session.get('user')
        print("user", user)
        if user:
            response = None
            if product_id:
                response = get_response(request, product_id)
            else:
                response = get_response(request)
            return response
        else:
            print("Please Login")
            url = request.path
            print(url)
            return redirect(f'/login?return_url={url}')

    return middleware
