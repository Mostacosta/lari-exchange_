from django.shortcuts import render
from .models import atm_details
from branches.models import branch_master

# Create your views here.

def atm_view(request):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')

    masters = branch_master.objects.filter(tag=lang)
    details = atm_details.objects.filter(tag=lang)

    return render(request,"atm/atm.html",{"masters":masters,"details":details})