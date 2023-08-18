from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import StudentForm
from . models import Course
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request,"index.html")

def new(request):
    return render(request,"new.html")

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or Password does not exist')

    context={'page':page}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            try:
                User.objects.get(username=username)  # Check if username exists
                messages.error(request, 'Username already exists. Please choose a different username.')
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                print('User created:', username)
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')

def studentform(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed')
            return redirect('new')
    context = {
        'form': form,
    }
    return render(request, 'studentreg.html', context)

# def studentform(request):
#     form = StudentForm()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('new')
#     context={
#         'form':form,
#     }
#     return render(request,'studentreg.html',context)

def load_cities(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id)
    return render(request, 'citydropdown.html', {'course': course})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)