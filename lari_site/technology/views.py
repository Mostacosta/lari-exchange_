from django.shortcuts import render
from .models import technology_detail,technologies
from django.shortcuts import get_object_or_404

# Create your views here.

def technology_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'ar'
    lang = 'eng'
    techno_ = get_object_or_404(technology_detail,tag=lang)
    technos_ = technologies.objects.filter(tag=lang)
    return render (request,'technology/technology.html',{'techno':techno_,'technos':technos_})
