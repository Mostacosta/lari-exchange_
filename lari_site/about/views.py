from django.shortcuts import render
from .models import about_details
from ceo.models import ceo_detail
from missionsandvision.models import mission_detail
from technology.models import technology_detail
from partners.models import partner
from django.shortcuts import get_object_or_404,get_list_or_404
# Create your views here.

def about_view (request):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    about_ = get_object_or_404(about_details,tag=lang)
    ceo_ = get_object_or_404(ceo_detail,tag=lang)
    mission_ = get_object_or_404(mission_detail,tag=lang)
    tech_ = get_object_or_404(mission_detail,tag=lang)
    partner_ = get_list_or_404(partner,tag=lang)
    return render(request,'about/about-main.html',{'about':about_,"ceo":ceo_,'mission':mission_,'tech':tech_,"partner":partner_[0]})


def about_details_view (request):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    about_ = get_object_or_404(about_details,tag=lang)
    return render (request,'about/about.html',{'about':about_})
