from django.shortcuts import render
from .models import contact_info
from django.shortcuts import get_object_or_404
from .forms import contact_form

# Create your views here.
def contact_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    my_contacts = get_object_or_404(contact_info, tag=lang)
    form  = contact_form()
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'contacts/contact.html',{"contact":my_contacts,'form':form})
    return render (request,'contacts/contact.html',{"contact":my_contacts,'form':form})
    
