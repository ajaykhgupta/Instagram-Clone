from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout ,login
from django.contrib.auth import authenticate
from .forms import ImageForm
from .models import Image
# from django.contrib import messages

def index(request):    # home page
    # context={
    #     'variable1' : 'Instagram'
    # }
    # return HttpResponse("this is home page")
    return render(request, 'index.html')

def explore(request):
    img = Image.objects.all()
    return render(request, 'explore.html',{'img':img})


def inbox(request):
    return render(request, 'inbox.html')

def profile(request):
    if request.method =='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    return render(request, 'profile.html',{'form':form})

# signup working properly
def signup(request):
    if request.method == 'POST':
        print("hello")
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
        username = request.POST.get("loginusername")
        password = request.POST.get("loginpassword")

        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            print("Correct credentials")
            login(request , user)
            return redirect('home')    #name of page where you want to redirect
        else:
            print("Incorrect credentials")
            return render(request, 'view_login.html')
    
    return render(request, 'view_login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
