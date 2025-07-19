from dataclasses import fields
from django import forms
from.models import Booking, Expense,Expenses,Task,profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class Employeeform(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        max_length=300
    )

    
    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name should not contain numbers.")
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise forms.ValidationError("Age must be greater than 0.")
        return age

    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address.strip()) < 10:
            raise forms.ValidationError("Address must be at least 10 characters long.")
        return address
    

class ExpenseForm(forms.ModelForm):
    class Meta:
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        model = Expense
        fields = '__all__'





class ExpensesForm(forms.ModelForm):
    class Meta:
     
        model=Expenses
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
        fields="__all__"





class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        widgets = {
            'Task_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Task_completed': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
        }
        fields="__all__"



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['username'].required = True

        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

def clean(self):
    cleaned_data = super().clean()
    password1 = cleaned_data.get("password1")
    password2 = cleaned_data.get("password2")

    if password1 and password2 and password1 != password2:
        raise forms.ValidationError("Passwords do not match.")



class ProfileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields="__all__"
        exclude=['user']


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        exclude=['user','bookingstatus','doctor']
