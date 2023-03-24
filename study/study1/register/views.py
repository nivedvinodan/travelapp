from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request, user)
            return redirect('/')
        else:

            messages.info(request, "invalid id")
            return redirect('login')

    return render(request, "login.html")


def register2(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register2')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register2')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password, )
                user.save();

        else:
            messages.info(request, "password not matching")
            return redirect('register2')
        print("user created")
        return redirect('/')
    return render(request, "registerForm.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

