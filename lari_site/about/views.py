from django.shortcuts import render
from .models import about_details
from django.shortcuts import get_object_or_404
# Create your views here.

def about_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    about_ = get_object_or_404(about_details,tag=lang)
    return render(request,'about/about.html',{'about':about_})
