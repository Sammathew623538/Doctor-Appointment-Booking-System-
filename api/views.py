from pickle import GET
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import Employee,Piller,Stu
from .forms import StuForm
from.serializers import Employeeserializer,Pillerserializer





@api_view(['GET'])
def employee(request):
    emp=Employee.objects.all()
    serializers=Employeeserializer(emp,many=True)
    return Response(serializers.data)






@api_view(['POST'])
def employe(request):
   data=request.data
   serializers=Employeeserializer(data=data)
   if serializers.is_valid():
      serializers.save()
   return Response(serializers.data)



@api_view(['GET'])

def kunjngal(request):
   stu=Piller.objects.all()
   see=Pillerserializer(stu,many=True)
   return Response(see.data)



@api_view(['POST'])

def Machuu(request):
   data=request.data
   serializers=Pillerserializer(data=data)
   if serializers.is_valid():
    serializers.save()
   return Response(serializers.data)



def sam(request):
   if request.method =='POST':
      Form=StuForm(request.POST)
      if Form.is_valid():
       Form.save()
       return redirect(mikk)
   else:
      Form=StuForm

   return render (request,'sams.html',{'form':Form})


def mikk(request):
   return render(request,'ss.html')