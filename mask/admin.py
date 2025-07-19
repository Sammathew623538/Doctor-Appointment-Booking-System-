from django.contrib import admin

# Register your models here.
from .models import mobile,car,Employee,Expense,Expenses,Task,profile,Booking
admin.site.register(mobile)
admin.site.register(car)
admin.site.register(Employee)
admin.site.register(Expense)
admin.site.register(Expenses)
admin.site.register(Task)
admin.site.register(profile)
admin.site.register(Booking)
