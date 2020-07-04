from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["UserName"];
        firstname = request.POST["FirstName"];
        lastname = request.POST["LastName"];
        email = request.POST["email"];
        pass1 = request.POST["Password1"];
        pass2 = request.POST["Password2"];
        if pass1 == pass2:

            if User.objects.filter(username=username).exists():
                messages.info(request, "User name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=firstname,
                                                last_name=lastname)
                user.save();
                print("User created");
                return redirect("/")
        else:
            messages.info(request, "Password doesn't match")
            return redirect("register")
    else:
        return render(request, 'register.html');


def login(request):
    print("inside login method")
    if request.method == "POST":
        print("in post method")
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect('login')
        else:
            print("Authenticated")
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
