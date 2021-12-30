from django.shortcuts import render
from django.http import HttpResponse
from registerapp.models import *

# Create your views here.
def page(request):
    return render(request, 'index.html')
def logpage(request):
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        user=request.POST['uname']
        uphone=request.POST['phone']
        uemail=request.POST['email']
        upassword=request.POST['password']
        details=registration_tb(first_name=fname,last_name=lname,username=user,phone=uphone,email=uemail,password=upassword)
        details.save()
        return render(request,'login.html',{'out': "Successfully Registered"})
    else:
        return render(request,'index.html',{'fail': "Register Failed"})
def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        check=registration_tb.objects.all().filter(email=email,password=password)
        if check:
            for x in check:
                request.session['id']=x.id
                myid=request.session['id']
                show=registration_tb.objects.all().filter(id=myid)
                print(show)
                return render(request,'profile.html', {'display':show})
            else:
                return render(request,'login.html')
        else:
            return render(request,'login.html')



