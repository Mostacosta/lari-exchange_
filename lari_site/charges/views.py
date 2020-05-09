from django.shortcuts import render,get_list_or_404
from .models import charges_headline,charges_details
# Create your views here.

def charges_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    master = get_list_or_404(charges_headline,tag=lang)
    details = get_list_or_404(charges_details,tag=lang)
    return render (request,"charges/charges.html",{"masters":master,"details":details})
