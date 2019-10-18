from django import forms
from .models import contact_form

class contact_form (forms.ModelForm):
    class Meta :
        model = contact_form
        fields = '__all__'
