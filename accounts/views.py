from django.contrib.auth.models import User, auth


from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def register(request):
    if request.method == "POST":

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:

            if User.objects.filter(username=username).exists():

                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():

                messages.info(request, "email taken")
                return redirect('register')

            else:

                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=firstname, last_name=lastname)

                user.save()
                print("user created")
                return redirect('/')

        else:

            messages.info(request, "password not matched")

            return redirect('register')

    else:

        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid details")
            return redirect('login')
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

