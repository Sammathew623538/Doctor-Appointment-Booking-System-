from django.shortcuts import render,redirect
from.models import Student,employeee
from .forms import Employeeform




def homei(request):
    return render(request,'sam.html')
 
 
def addstudent(request):
  return render(request,'student.html')



def result(request):
   
   n=request.GET.get('name')
   a=request.GET.get('age')
   add=request.GET.get('address')

   return render(request,'answer.html',{'name':n,'age':a,'address':add})



def piller(request):
   if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('age')
        c=request.POST.get('address')
        s1=Student(name=a,age=b,address=c)
        s1.save()
        return redirect(resultzz)

   return render(request,'pillerz.html')



def resultzz(request):
   return render(request,'resultzzz.html')


def adimakal(request):
    if request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ans)
            
    else:
        form=Employeeform()

    return render(request,'adimakal.html',{'form':form})


def ans(request):
    return render(request,'pariharam.html')




