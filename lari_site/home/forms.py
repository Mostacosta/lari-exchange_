from django import forms

class calculator (forms.Form):
    first_amount = forms.IntegerField(max_value=1000000)
    first_currency = forms.CharField(max_length=5)
    second_currency = forms.CharField(max_length=5)
 
