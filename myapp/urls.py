from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path('students/',views.all_students,name='show-students'),
    path('form/',views.form,name='form'),
    path('success/',views.createpost,name='success'),
    path('successforhelp/',views.createpost1,name='successforhelp'),
    #path('printdata/',views.printdata,name='printdata'),
    path('post/',views.post,name='post'),
    path('faqs/',views.faqs,name='faqs'),
    path('viewprevposts/',views.viewprevposts,name='viewprevposts'),
    path('askforhelp/',views.askforhelp,name='askforhelp'),
    #path('blockA/',views.blockA,name="blockA"),
    #path('blockB/',views.blockB,name="blockB"),
    #path('blockC/',views.blockC,name="blockC"),
    #path('blockD/',views.blockD,name="blockD"),
    #path('library/',views.library,name="library"),
    #path('busbay/',views.busbay,name="busbay"),
    #path('canteen/',views.canteen,name="canteen"),
    #path('profile/',views.profile,name="profile"),
    path('home/',views.home,name='home'),
    # path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    #path('',views.login,name='login'),
    path('',views.welcome,name='welcome')
]
