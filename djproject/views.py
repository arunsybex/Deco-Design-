from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def home(request):
    return render(request, 'Main.html')
def cafe(request):
    return render(request, 'Cafe.html')
def livingroom(request):
    return render(request, 'Living Room.html')
def managerroom(request):
    return render(request, 'Manager Room.html')
def gym(request):
    return render(request, 'Gym.html')
def restaurant(request):
    return render(request, 'Restaurant.html')
def school(request):
    return render(request, 'School.html')
def bedroom(request):
    return render(request, 'Bedroom.html')
def diningroom(request):
    return render(request, 'Dining Room.html')
def falseceiling(request):
    return render(request, 'False Ceiling.html')
def studyroom(request):
    return render(request, 'Study Room.html')
def kidrroom(request):
    return render(request, 'Kids Room.html')
def reception(request):
    return render(request, 'Reception.html')
def sharedoffice(request):
    return render(request, 'Shared Office.html')


def contact(request):


    if request.method == "POST":

        fullname = request.POST['fullname']
        email = request.POST['email']
        # number = request.POST['number']
        message = request.POST['message']

        # send mail
        send_mail(
            fullname, #subject
            message, #body
            email, #from email 
            ['manmeetsingh28603@gmail.com'], #to email
            fail_silently = False
        )

        # return mail 
        send_mail(
            fullname, #subject 
            "Thank You For Contacting With Deco Designs Our Team Will Respond You shortly", #body
            email, #from email
            [email], #to email
            fail_silently= False
        )

    else:
        return render(request, 'Contact.html')
    return render(request, 'Response.html')


def response(request):
    return render(request, 'Response.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'Login.html')
    return redirect('/')



def register(request):
    
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user1 = auth.authenticate(username=username, password=password1)
                user.save()
                auth.login(request, user1)
                print('user created')
                return redirect('/')
            
        else:
            messages.info(request, 'Password Not Matching...')
            return redirect(register)
        return redirect('/')

    else:
        return render(request, 'Register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

