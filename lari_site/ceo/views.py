from django.shortcuts import render
from .models import ceo_detail
from django.shortcuts import get_object_or_404
# Create your views here.

def ceo_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'ar'
    lang = 'eng'
    ceo_ = get_object_or_404(ceo_detail,tag=lang)
    return render (request,'ceo/ceo.html',{"ceo":ceo_})
