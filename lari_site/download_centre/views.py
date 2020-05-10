from django.shortcuts import render,HttpResponse
from django.shortcuts import get_list_or_404
from .models import download_details

# Create your views here.

def pdf_list (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'ar'
    lang = 'eng'
    files = get_list_or_404(download_details,tag=lang)
    return render (request,"download/download.html",{'files':files})
    

