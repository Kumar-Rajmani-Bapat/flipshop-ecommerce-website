from django.shortcuts import render , redirect
def cantAccessAfterLogin(get_response):
    # // index

    def middleware(request):
        user = request.session.get('user')
        print("user" , user)
        if user :
            return redirect('index')
        else:
            return get_response(request)


    return middleware