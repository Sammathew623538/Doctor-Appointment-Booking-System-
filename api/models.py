from django.db import models


class Employee(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    address=models.TextField()
    salary=models.IntegerField()
    def __str__(self):
     return str(self.name)
    



class Piller(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models. CharField(max_length=20)
    rollno=models.IntegerField()
    def __str__ (self):
         return str(self.name)
    

class Stu(models.Model):
    name=models.CharField()
    rollno=models.IntegerField()

