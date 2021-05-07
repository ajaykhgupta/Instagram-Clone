from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate,login
# from django.contrib import messages

def index(request):    # home page
    # context={
    #     'variable1' : 'Instagram'
    # }
    # return HttpResponse("this is home page")
    return render(request, 'index.html')

def explore(request):
    # return HttpResponse("this is explore page")
    return render(request, 'explore.html')


def inbox(request):
    return render(request, 'inbox.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        # Get the post parameter
        Mobemail  = request.POST['Mobemail']
        fullname  = request.POST['fullname']
        username  = request.POST['username']
        password  = request.POST['password']

    # create the user
        myuser = User.objects.create_user(username, Mobemail, password )
        myuser.fullname = fullname
        myuser.save()

        # # ADD messages that account has been created
        # messages.success(request, "Your account is created pls log in")                

    return render(request, 'signup.html')
    



def view_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            print("hello")
            login(request , user)
            return redirect("explore")
        else:
            print("hey")
            return render(request, 'view_login.html')
    
    return render(request, 'view_login.html')


    

