from django import forms
from .models import contact_form

class contact_form (forms.ModelForm):
    class Meta :
        model = contact_form
        fields = '__all__'

class job_form (forms.Form):
    job = forms.CharField( max_length=100)
    info = forms.Textarea()
    name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    Date = forms.DateField()
    Nationality = forms.CharField(max_length=100)
    Qualifications = forms.Textarea()
    Experience = forms.Textarea()
    Mobile_Number = forms.IntegerField(max_value=None)
    email = forms.EmailField()




