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
def monday(request):
    return HttpResponse('today is monday')
def tuesday(request):
    return HttpResponse('today is tuesday')
def wednesday(request):
    return HttpResponse('today is wednesday')




def home(request):
    return render(request,'hello.html')



def sam(request):
    return render(request,'allpro.html')




def addstu(request):
    success = False  # success message flag

    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            # Save the data to DB
            e1 = Employee(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                address=form.cleaned_data['address']
            )
            e1.save()
            success = True
            form = Employeeform()  # clear form after success
    else:
        form = Employeeform()

    return render(request, 'addstu.html', {'form': form, 'success': success})
  
  
  
def result(request):
    return render(request,'result.html')


months= {
    '1': 'welcome to januvary',
    '2': 'welcome to februvary',
    '3': 'welcome to march',
    '4': 'welcome to April',
    '5': 'welcome to may',
    '6': 'welcome to june',
     '7': 'welcome to july',
    '8': 'welcome to august',
    '9': 'welcome to september',
     '10': 'welcome to october',
     '11': 'welcome to november',
     '12': 'welcome to december',
              
}
print(list(months.keys()))

def monthview(request, month):
  
    return HttpResponse(months[month])





def house(request):
    return render(request, 'components/carousel.html') 

def add_expense(request):
    if request.method=='POST':
        form=ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(view_expense)
    else:        
      form= ExpenseForm()
    return render(request,'addexp.html',{'form':form})

def hello(request):
    return render(request,'daa.html')





def view_expense(request):
    exp=Expense.objects.all()
    total=0
    for i in exp:
        total=total+ i.price
    return render(request,'expense.html',{'exp':exp,'tot':total})





def Expen(request):
    if request.method =="POST":
        form=ExpensesForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect(Expp)
    else:
        form=ExpensesForm    
    return render(request,'exx.html',{'form':form})


def Expp(request):
    pro=Expenses.objects.all()
    total=0
    for i in pro:
        total=total + i.price
    return render(request,'addexppp.html',{'pro':pro,'tot':total})



def Expenseedit(request,pid):
    pro=Expenses.objects.get(pk=pid)
    if request.method =='POST':
        form=ExpensesForm(request.POST,instance=pro)
        if form.is_valid():
           form.save()
           return redirect(Expp)
    else:
        form=ExpensesForm(instance=pro)
        return render(request,'Expedit.html',{'form':form}) 
    


def Expensedel(request,pid):
     pro=Expenses.objects.get(id=pid)
     if request.method =='POST':
        pro.delete()
        return redirect(Expp)
     return render(request,'Expdel.html',{'pro':pro})


def Todo(request):
    if request.method =='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Todo2)
    else:
            form=TaskForm()     
    return render(request,'task.html',{'form':form})



def Todo2(request):
    pro=Task.objects.all()
    return render(request,'task2.html',{'pro':pro})

def complete_task( request, pid):
    task = Task.objects.get(id=pid)
    task.Task_completed = True  
    task.save()
    return redirect(Todo2)    





def Taskdit(request,pid):
    pro=Task.objects.get(pk=pid)
    if request.method =='POST':
        form=TaskForm(request.POST,instance=pro)
        if form.is_valid():
           form.save()
           return redirect(Todo2)
    else:
        form=TaskForm(instance=pro)
        return render(request,'Todoedit.html',{'form':form}) 
    

def Taskdel(request,pid):
     pro=Task.objects.get(id=pid)
     if request.method =='POST':
        pro.delete()
        return redirect(Todo2)
     return render(request,'Tododel.html',{'pro':pro})






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
    