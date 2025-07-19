
from django import forms

from.models import Employee
class Employeeform(forms.ModelForm):
    class Meta:
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        model=Employee
        fields='__all__'
    