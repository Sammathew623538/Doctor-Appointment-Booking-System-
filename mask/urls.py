from django.urls import path
from mask.views import *

urlpatterns = [
    path('monday', monday),
    path('tuesday', tuesday),
    path('wednesday', wednesday),
    path('home', home),
    path('allpro', sam),
    path('addstu', addstu),
    path('result', result,name='result'),
    path('login', loginpage,name='Login'),
    path('addexp', add_expense,name='addexp'),
    path('viewexp', view_expense,name='viewexp'),
    path('Expense',Expen,name='exx'),
    path('Exp',Expp),
    path('Exppp/<int:pid>',Expenseedit,name='Expedit'),
    path('Expppp/<int:pid>',Expensedel,name='Expdel'),
    path('task',Todo,name='task'),
    path('task2',Todo2,),
    path('task3/<int:pid>', complete_task, name='Todocomplete'),
    path('task4/<int:pid>', Taskdit,name='Todoedit'),
    path('task5/<int:pid>', Taskdel,name='Tododel'),
    path('register',Register,name='register'),
    path('logout',logoutpage,name='Logout'),
    path('house', house,name='house'),
    path('month/<month>', monthview),
    path('profile',profilepage,name='profile'),
    path('profiless',proedit, name='Editprofile'),
    path('addbooking/<int:uid>',addbooking,name='bookdoc'),
    path('viewbook',booking_list),
    path('doctor',doctors,name='dctr'),
    path('app',appointment,name='appo'),
    path('acc/<int:pid>',accept,name='accept'),
    path('rej/<int:uid>',reject,name='reject'),
    path('pat',patient,name='patient'),
    path('sam',hello)
   
   


]