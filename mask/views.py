from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . form import Employeeform
from .form import ExpenseForm,ExpensesForm,TaskForm, RegisterForm,ProfileForm,BookingForm
from . models import Employee,Task,profile,Booking
from . models import Expense,Expenses
from django.contrib.auth.models import User

# Create your views here.

def house(request):
    return render(request, 'components/carousel.html') 


def loginpage(request):

    if request.method=='POST':
        usern=request.POST.get('username')
        passwordn=request.POST.get('password')
        user=authenticate(request,username=usern,password=passwordn)
        if user:
            login(request,user)
            print('user authenticate')
            return redirect(house)
        else:
            print('no such user')    
    return render(request,'loginpage.html')




def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           a= form.save() 
           profile.objects.create(user=a) 
           return redirect(loginpage)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def logoutpage(request):
    logout(request)
    return redirect(house)

def profilepage(request):
    usr=request.user
    pro=profile.objects.get(user=usr)
    return render(request,'profile.html',{'pro':pro})

def proedit(request,):
    pro=profile.objects.get(user=request.user)
    if request.method =="POST":
        form=ProfileForm(request.POST,instance=pro)
        if form.is_valid():
           form.save()
           return redirect(profilepage)
    else:
        form=ProfileForm(instance=pro)        
    return render(request,'Editprofile.html',{'form':form})



@login_required
def addbooking(request,uid):
    docs=User.objects.get(id=uid)
    if not request.user.is_superuser and not request.user.is_staff:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                a = form.save(commit=False)
                a.user = request.user
                a.doctor=docs
                a.save()
                return redirect(house)
            
        else:
            form = BookingForm()
        return render(request, 'addbook.html', {"form": form})

@login_required
def booking_list(request):
      if request.user.is_staff:
       return render(request,'booklist.html')


def doctors(request):
    doctor=User.objects.filter(is_staff=True ,is_superuser=False)
    print(doctor)
    return render(request,'doctor.html',{'doctor':doctor})
   


def appointment(request):
       if request.user.is_staff:
            app= Booking.objects.filter(doctor=request.user,bookingstatus='pending')
            return render(request,'appointment.html',{'app':app}) 

def accept(request,pid): 
    book=Booking.objects.get(id=pid)
    book.bookingstatus='approved'
    book.save()
    return redirect(appointment)



def reject(request,uid): 
    book=Booking.objects.get(id=uid)
    book.bookingstatus='reject'
    book.save()
    return redirect(appointment)

def patient(request):
    book=Booking.objects.filter(user=request.user)
    return render(request,'patview.html',{'book':book})
    
