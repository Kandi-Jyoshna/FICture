from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ClassC3
from .models import Form,AskHelp
from datetime import date

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this

# Create your views here.

def all_students(request):
    context={
        "student_list":ClassC3.objects.all()
    }
    return render(request,'student_list.html',context=context)


def home(request):
    return render(request,'home.html')

def form(request):
    return render(request,'form.html')
def post(request):
    return render(request,"post.html")
def faqs(request):
    return render(request,"faqs.html")
def askforhelp(request):
    return render(request,"askforhelp.html")
# def blockA(request):
#     return render(request,"blockA.html")
# def blockB(request):
#     return render(request,"blockB.html")
# def blockC(request):
#     return render(request,"blockC.html")
# def blockD(request):
#     return render(request,"blockD.html")
# def library(request):
#     return render(request,"library.html")
# def canteen(request):
#     return render(request,"canteen.html")
# def busbay(request):
#     return render(request,"busbay.html")
# def profile(request):
#     return render(request,"profile.html")

def createpost(request):
    if(request.method=='POST'):
        if(request.POST.get('name') and request.POST.get('objectname') and request.POST.get('place')):
            post=Form()
            post.name=request.POST.get('name')
            post.rollnumber=request.POST.get('rollnumber')
            post.objectname=request.POST.get('objectname')
            post.place=request.POST.get('place')
            post.contact=request.POST.get('contact')
            post.description=request.POST.get('description')
            post.pub_date=date.today()
            post.save()
            return render(request,'success.html')
    else:
        return render(request,'success.html')


def viewprevposts(request):
    obj=Form.objects.all()
    obj1=AskHelp.objects.all()
    return render(request,'viewprevposts.html',{'obj':obj,'obj1':obj1})

def createpost1(request):
    if(request.method=='POST'):
        if(request.POST.get('name1') and request.POST.get('objectname1')):
            helpme=AskHelp()
            helpme.nameField=request.POST.get('name1')
            helpme.roll=request.POST.get('roll1')
            helpme.objectlost=request.POST.get('objectname1')
            helpme.contactdetails=request.POST.get('contact1')
            helpme.describe=request.POST.get('description1')
            helpme.post_date=date.today()
            helpme.save()
            return render(request,'successforhelp.html')
    else:
        return render(request,'successforhelp.html')

def logout(request):
    return render(request,'logout.html')

# def profile(request):
#     nameuser=request.POST.get('username')
#     return render(request,'profile.html')

def welcome(request):
    return render(request,'welcome.html')




def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/login/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})