from django.db import models


class Student(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    address=models.CharField()
    def __str__(self):
        return str(self.name)
    



class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    salary=models.IntegerField()
    address=models.TextField()
     


class employeee(models.Model):
    id=models.IntegerField(primary_key=True)
    salary=models.CharField()
    address=models.TextField()

