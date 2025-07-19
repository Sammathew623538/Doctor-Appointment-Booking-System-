from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)  
    age = models.IntegerField()
    

class Employee(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    address=models.CharField()






class Laptop(models.Model):
    name = models.CharField(max_length=20)  
    age = models.CharField()
    price=models.IntegerField
    description = models.TextField()  




class car(models.Model):
    name = models.CharField(max_length=30)  
    brand = models.CharField()
    price=models.IntegerField
    description = models.TextField()  




class mobile(models.Model):
    name = models.CharField(max_length=30)  
    brand = models.CharField()
    price=models.IntegerField
    description = models.TextField() 
    email=models.EmailField() 
     




class Course(models.Model):
   id=models.IntegerField(primary_key=True)
   name=models.CharField(max_length=30)
   des=models.TextField()
   duration=models.CharField()
   def _str_(self):
        return str(self.id)

  




class Teacher(models.Model):
  name=models.CharField()
  course=models.CharField()
  address=models.CharField()
  def _str_(self):
        return self.name

class Address2(models.Model):
      house=models.CharField() 
      location=models.CharField()
      state=models.CharField()
      district=models.CharField()
      add=models.OneToOneField(Teacher,on_delete=models.CASCADE,null=True)
      def _str_(self):
         return self.house




class Student(models.Model):  
   name=models.CharField(max_length=20)
   age=models.IntegerField()
   roll_no=models.IntegerField(primary_key=True)
   course=models.CharField(max_length=20)
   teacher=models.CharField()
   address=models.TextField()
   address=models.OneToOneField(Address2,on_delete=models.CASCADE,null=True)
   teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
   course=models.ForeignKey(Course ,on_delete=models.CASCADE)
   def _str_(self):
        return self.name
   

   


   
class Expense(models.Model):
    name = models.CharField(max_length=100)  
    price = models.IntegerField()

    def __str__(self):                        
        return self.name








class Expenses(models.Model):
    name=models.CharField()
    price=models.IntegerField()
    def __str__(self):                        
        return str(self.name)
  



class Task(models.Model):
 Task_Name=models.CharField(max_length=100)
 Description=models.TextField(max_length=200)
 Task_completed=models.BooleanField(default=False)

 def __str__(self):
        return str(self.Task_Name)
 




class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    

class Booking(models.Model):
    status= (
        ('pending','pending'),
        ('approved','approved'),
        ('rejected','rejected'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    reason=models.TextField()
    bookingdate=models.DateField()
    bookingstatus=models.CharField(choices=status,default='pending')
    doctor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctor",null=True)
    def __str__(self):
        return str(self.user)