from django.shortcuts import render

# Create your views here.
def rates_view (request):
    return render (request,'rates/rates.html')