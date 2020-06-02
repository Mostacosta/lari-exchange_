from django.shortcuts import render
from .models import news_detail,cards
from django.shortcuts import get_object_or_404
# Create your views here.

def news_view(request):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    news = news_detail.objects.filter(tag=lang)
    return render (request,'news/promotions.html',{'news':news})

def news_details_view (request,pk):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    new = get_object_or_404(news_detail,pk=pk)
    return render (request,'news/single-news.html',{'new':new})

def cards_view (request,pk):
    if request.session.get('lang') == None:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    card = get_object_or_404(cards,pk=pk)
    return render (request,'news/single-news.html',{'new':card})

