from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Details")
            return redirect('login')
    else:
        return render(request, "login.html")


def registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('registration')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password1)
                user.save()
                print('user created')
        else:
            print("wrong password")
            return redirect('registration')
        return redirect('/')
    else:

        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
