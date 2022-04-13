from django import forms
from .models import students


class Loginform(forms.Form):
    username = forms.CharField(max_length=20, min_length=5)
    password = forms.CharField(max_length=50, min_length=8)
    rememberme = forms.BooleanField()

    class Meta:
        model = 'myuser'


class insertstudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['name', 'track']  # '__all__'


class insertstudentForm2(forms.Form):
    name = forms.CharField(max_length=20, min_length=5)
    track = forms.CharField(max_length=50, min_length=10)

    class Meta:
        model = 'students'


class updatestudentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['name', 'track']


class updatestudentForm2(forms.Form):
    id = forms.CharField(max_length=20, min_length=5)
    name = forms.CharField(max_length=20, min_length=5)
    track = forms.CharField(max_length=50, min_length=10)

    class Meta:
        model = 'students'
