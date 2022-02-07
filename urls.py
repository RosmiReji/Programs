from django.contrib import admin
from django.urls import path,include
#import photoapp.views

from.import views
urlpatterns = [


    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('register/',views.register,name='register'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('addpackage/',views.addpackage,name='addpackage'),
    path('userhome/',views.userhome,name='userhome'),
    path('event/',views.event,name='event'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('registers/',views.registers,name='registers'),
    path('loginaction/',views.loginaction,name='loginaction'),
    path('packages/',views.packages,name='packages'),
    path('seepackages/',views.seepackages,name='seepackages'),
    path('bookpackage/',views.bookpackage,name='bookpackage'),
    path('userbook/',views.userbook,name='userbook'),
    path('login_action/',views.login_action,name='login_action'),
    path('editpackage/<int:pid>',views.editpackage,name='editpackage'),
    path('update/<int:pid>', views.update, name='update'),
    ]
