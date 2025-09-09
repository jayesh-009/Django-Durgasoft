from django import forms
from AugustApp.models import Stud,Movie


class StudentForm(forms.Form):

    name=forms.CharField()
    marks=forms.IntegerField()

class StudForm(forms.ModelForm):
    
    class Meta:
        model=Stud

        fields='__all__'

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'


class LoginForm(forms.Form):

    name=forms.CharField()
    datetime=forms.DateTimeField()
        
class AddItemForm(forms.Form):

    name=forms.CharField()
    quantity=forms.IntegerField()

