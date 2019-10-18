from django.shortcuts import render
from .models import partners_main,partner
from django.shortcuts import get_object_or_404
# Create your views here.

def partner_view(request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    main_ = get_object_or_404(partners_main,tag=lang)
    partners = partner.objects.filter(tag=lang)
    return render (request,'partners/partners.html',{'main':main_,"partners":partners})