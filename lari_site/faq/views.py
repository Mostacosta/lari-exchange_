from django.shortcuts import render
from .models import GCard_questions,paymax_questions,general_questions
# Create your views here.

def questions_view (request):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    gc_ques = GCard_questions.objects.filter(tag=lang)
    pay_ques = paymax_questions.objects.filter(tag=lang)
    generals = general_questions.objects.filter(tag=lang)
    return render (request,'faq/faq.html',{'pay':pay_ques,'gc':gc_ques,"generals":generals})
