from django.urls import path
from projectk.views import *
from . import views


urlpatterns = [
path('home',homei),
path('addstudent',addstudent),
path('result',result,name='answer'),
path('piller',piller),
path('resultzz',resultzz),
path('adimakal',adimakal),
path('ans',ans),




]