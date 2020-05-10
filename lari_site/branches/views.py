from django.shortcuts import render
from .models import branch_master,branch_details
# Create your views here.

def branch_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'ar'
    lang = 'eng'

    master = branch_master.objects.filter(tag=lang)
    details = branch_details.objects.filter(tag=lang)

    return render (request,"branches/branches.html",{"masters":master,"details":details})

    
