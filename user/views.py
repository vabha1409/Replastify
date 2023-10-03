from django import forms
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
# from googletrans import Translator
from django.http import JsonResponse
from django.urls import reverse


from .models import Contact
from .models import Service ,Collect ,Subscribed




# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='login')
def services(request):
    return render(request, 'services.html')

def servicesdetails(request):
    return render(request, 'service-details.html')
def servicesdetails1(request):
    return render(request, 'service-details1.html')
def servicesdetails2(request):
    return render(request, 'service-detail2.html')
def servicesdetails3(request):
    return render(request, 'service-detail3.html')
def servicesdetails4(request):
    return render(request, 'service-detail4.html')
def servicesdetails5(request):
    return render(request, 'service-detail5.html')

def replastform(request):
    return render(request, 'replastform.html')



def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def blogdetails2(request):
    return render(request, 'blog-details2.html')


def blogdetails3(request):
    return render(request, 'blog-details3.html')


def blogdetails4(request):
    return render(request, 'blog-details4.html')


def blogdetails5(request):
    return render(request, 'blog-details5.html')


def blogdetails6(request):
    return render(request, 'blog-details6.html')

def projectdetails(request):
    return render(request, 'project-details.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'An error occurred.')
            return render(request, 'signup.html')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse("PASSWORD DID NOT MATCH")


        else:
            my_user = User.objects.create_user(username, email, password1)
            my_user.save()
            subject = 'Successfull!!'
            message = 'Thanks for contacting us!'
            email_from = "yashlakhan27@gmail.com"
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'okay')
            return redirect("signup")

        # print(username, email, password1, password2)

    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:

            return render(request, 'login.html', {'error': 'Invalid username or password'})
            #return HttpResponse("INVALID USER OR PASSWORD")
    else:
        return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


def enquiry(request):
    return render(request, 'index.html')
    # subject = 'welcome to Hello world'
    # message = 'Thanks for contacting us!'
    # email_from = "yashlakhan27@gmail.com"
    # recipient_list = [email]
    # send_mail(subject, message, email_from, recipient_list)


# def translate_text(request):
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         target_lang = request.POST.get('target_lang')
#
#         translator = Translator()
#         translation = translator.translate(text, dest=target_lang)
#
#         return JsonResponse({'translated_text': translation.text})
#
#     return render(request, 'translate.html')


def voice_search(request):
    return render(request, 'voice_search.html')

def dynamic_theme(request):
    return render(request, 'dynamic_theme.html')


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, "contact.html")


def subscribe_form(request):
    if request.method == "POST":
        # name= request.POST.get('name')
        email = request.POST.get('email')
        subscribe = Subscribed( email=email)
        messages.success(request, "Thank you for subscribing!")
        send_mail(
            "Subscription Mail",
            "Thank You For Subscribing",
            "yashlakhan27@gmail.com",
            [email],
            fail_silently=False,
        )

        subscribe.save()

        show_alert = True
        success_message = "Thank you for subscribing!"
        return render(request, 'index.html', {'success_message': success_message})
    return HttpResponseRedirect(reverse(index))

def  collect_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        location = request.POST.get('location')
        business = request.POST.get('business')
        feedback = request.POST.get('feedback')
        collectss = Collect(name=name, mobile=mobile, location=location, business=business,feedback=feedback)
        collectss.save()
    return HttpResponseRedirect(reverse(index))


def service_form(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        industry = request.POST.get('industry')
        bn = request.POST.get('bn')
        wu = request.POST.get('wu')
        jt = request.POST.get('jt')
        years = request.POST.get('years')
        email = request.POST.get('email')
        number = request.POST.get('number')
        howhelp = request.POST.get('howhelp')
        service = Service(firstname=firstname,lastname=lastname, email=email, industry=industry,bn=bn,wu=wu,jt=jt,years=years,number=number,howhelp=howhelp)
        service.save()
    return render(request, "replastform.html")


