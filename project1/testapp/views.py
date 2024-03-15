from django.shortcuts import render
from django.http import HttpResponse
from .models import login
from .models import Survey
from .models import Sign
from .models import Client
from .models import Enquiry
# Create your views here.
def display(request):
     return render(request,'index.html')

def card1(request):
     return render(request,'card1.html')
def card2(request):
     return render(request,'card2.html')
def card3(request):
     return render(request,'card3.html')

def doLogin(request):
    return render(request,'login.html')

def receive(request):
     if request.method=='POST':
          myname=request.POST.get('myname')
          mypass=request.POST.get('mypass')
          z=login(name=myname,password=mypass)
          z.save()
          return HttpResponse("Data successfully entered...")
     else:
          return HttpResponse("Invalid request")
     

def loginreport(request):
    dologin=login.objects.all()
    return render(request,'report1.html',{'dologin':dologin})


def show(request):
    return render(request, 'review.html')

def doreviews(request):
    if request.method=='POST':
        myreview=request.POST.get('opinion')
        z=Survey(text=myreview)
        z.save()
        return HttpResponse("Data Entered...")
    else:
        return HttpResponse("Invalid request")
    
def surveyreport(request):
   doreviews=Sign.objects.all()
   return render(request,'report5.html',{'doreviews':doreviews})
    
def getin(request):
    return render(request, 'sign.html')

def dosign(request):
    if request.method=='POST':
        myusername=request.POST.get('myusername')
        myemail=request.POST.get('myemail')
        mypassword=request.POST.get('mypassword')
        mycnfpass=request.POST.get('mycnfpass')
        z=Sign(username=myusername,email=myemail,password=mypassword,cnfpass=mycnfpass)
        z.save()
        return HttpResponse("Data Entered...")
    else:
        return HttpResponse("Invalid request")
    
def signreport(request):
    dosign=Sign.objects.all()
    return render(request,'report2.html',{'dosign':dosign})
    
def clie(request):
    return render(request, 'client.html')

def formclient(request):
    if request.method=='POST':
        com_name=request.POST.get('com_name')
        location=request.POST.get('location')
        duration=request.POST.get('duration')
        services=request.POST.get('services')
        z=Client(com_name=com_name,location=location,duration=duration,services=services)
        z.save()
        return HttpResponse("Data Entered...")
    else:
        return HttpResponse("Invalid request")
    
def clientreport(request):
    formclient=Client.objects.all()
    return render(request,'report3.html',{'formclient':formclient})
    
def enqu(request):
    return render(request,'enquiry.html')

def doenqui(request):
    if request.method=='POST':
        enq_name=request.POST.get('enq_name')
        enq_email=request.POST.get('enq_email')
        enq_phone=request.POST.get('enq_phone')
        enq_location=request.POST.get('enq_location')
        enq_service=request.POST.get('services')
        z=Enquiry(enq_name=enq_name,enq_email=enq_email,enq_phone=enq_phone,enq_location=enq_location,enq_service=enq_service)
        z.save()
        return HttpResponse("Data Entered...")
    else:
        return HttpResponse("Invalid request")
    
def enquiryreport(request):
    doenqui=Client.objects.all()
    return render(request,'report4.html',{'doenqui':doenqui})
    

    