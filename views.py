import os

from django.contrib import auth, messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect,loader
from.models import Package,Login,Admin
from django.http import HttpResponse




def index(request):
    return render(request, "photoapp/index.html")
def login(request):
    return render(request, "photoapp/login.html")
def userlogin(request):
    return render(request, "photoapp/userlogin.html")
def register(request):
    return render(request, "photoapp/register.html")
def adminhome(request):
    return render(request, "photoapp/adminhome.html")
def addpackage(request):
    return render(request, "photoapp/addpackage.html")


def event(request):
    return render(request, "photoapp/event.html")
def about(request):
    return render(request, "photoapp/aboutus.html")
def gallery(request):
    return render(request, "photoapp/gallery.html")
def bookpackage(request):
    return render(request, "photoapp/bookpackage.html")



# Create your views here.

def packages(request):
    if request.method == "POST":
        packobj = Package()
        packobj.packagename = request.POST.get("packagename")
        packobj.price = request.POST.get("price")
        packobj.image = request.FILES['image']
        packobj.about = request.POST.get("about")
        packobj.save()
        return HttpResponse("<script>alert('Inserted..');</script>")
    else:
        return render(request, "photoapp/addpackage.html")


def seepackages(request):
    packages=Package.objects.all()
    return render(request, "photoapp/viewpackage.html",{'packages': packages})

def userbook(request):
    packages=Package.objects.all()
    return render(request, "photoapp/bookpackage.html",{'packages': packages})
def userhome(request):
    id=request.session['id']
    name=request.session['name']

    return render(request, "photoapp/userhome.html",{'id':id, 'name':name})



def registers(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        Login(name=name,email=email,password=password).save()

    return render(request,'photoapp/register.html')


def loginaction(request):
     if request.method == 'POST':
         name = request.POST.get('name')
         password = request.POST.get('password')
         user = Login.objects.filter(name=name,password=password)
         if user:
              userdet=Login.objects.get(name=name,password=password)
              id=userdet.id
              username_user=userdet.name
              request.session['id']=id
              request.session['name']=username_user
              return redirect('userhome')
         else:
             return redirect('userlogin')
     return render(request, 'userlogin')

def login_action(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if Admin.objects.filter(name=name, password=password).exists():
            loginobj = Admin.objects.get(name=name, password=password)

            return render(request,'photoapp/adminhome.html')
        else:
            return render(request, "photoapp/login.html", {'message': "login failed.. try again"})


def editpackage(request,pid):
    package=Package.objects.get(id=pid)



    return render(request,"photoapp/editpackage.html",{'package':package})

def update(request,pid):
    obj=Package()
    obj.id=pid
    obj.packagename=request.POST.get('packagename')
    obj.price=request.POST.get('price')
    obj.image=request.POST.get('image')
    obj.about=request.POST.get('about')

    obj.save()
    return redirect('photoapp/viewpackage.html')









