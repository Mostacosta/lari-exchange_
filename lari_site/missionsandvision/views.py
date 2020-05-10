from django.shortcuts import render
from .models import mission_detail

# Create your views here.

def mission_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'ar'
    lang = 'eng'
    missions_ = mission_detail.objects.filter (tag=lang)
    return render (request,'missions/mission.html',{'missions':missions_})
    
    