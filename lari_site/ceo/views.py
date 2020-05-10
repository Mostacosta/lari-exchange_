from django.shortcuts import render
from .models import ceo_detail
from django.shortcuts import get_object_or_404
# Create your views here.

def ceo_view (request):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    ceo_ = get_object_or_404(ceo_detail,tag=lang)
    return render (request,'ceo/ceo.html',{"ceo":ceo_})
