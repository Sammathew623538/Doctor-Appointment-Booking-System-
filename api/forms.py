from django import forms
from.models import*


class StuForm(forms.ModelForm):
    class Meta:
        model=Stu
        fields='__all__'
