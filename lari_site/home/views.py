from django.shortcuts import render,HttpResponse,redirect
import requests
from .models import slider_detail,paymentcard_detail
from news.models import news_detail
from products.models import products_detail
from .forms import calculator
from django.http import JsonResponse
# Create your views here.

def currency_table (request):
    url = 'https://api.exchangerate-api.com/v4/latest/AED'
    response = requests.get(url)
    data = response.json()
    print (data)
    return HttpResponse (data)

def home_view(request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    cal = calculator()
    sliders = slider_detail.objects.filter(tag=lang)
    news = news_detail.objects.filter(tag=lang)
    payment = paymentcard_detail.objects.filter(tag=lang)
    products = products_detail.objects.filter(tag=lang)
    if request.method == "POST":
        print(request.POST)
        cal = calculator(request.POST)
        if cal.is_valid():
            amount = request.POST['first_amount']
            first_currency = request.POST['first_currency']
            second_currency = request.POST['second_currency']
            url = 'https://api.exchangerate-api.com/v4/latest/'+first_currency
            response = requests.get(url)
            data = response.json()
            result = float(amount) * data['rates'][second_currency]
            result = round(result,2)
            response_data = {}
            response_data['result']= result
            return JsonResponse(response_data)

    return render(request,'home/index.html',{"sliders":sliders,"news":news,"pay":payment[0],"products":products[:3],"form":cal})

def change_lang (request):
    lang = request.session.get('lang')
    print(lang)
    if lang =='eng':
        request.session['lang'] = 'ar'
    else :
        request.session['lang'] = 'eng'
    return redirect(request.META.get('HTTP_REFERER'))