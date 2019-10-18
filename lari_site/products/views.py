from django.shortcuts import render
from .models import products_detail
from django.shortcuts import get_object_or_404

# Create your views here.
def products_view(request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    products_ = products_detail.objects.filter(tag=lang)
    return render (request,'products/products.html',{'products':products_})

def products_detail_view(request,pk):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    products_ = products_detail.objects.filter(tag=lang)
    product = get_object_or_404(products_detail,pk=pk)
    return render (request,'products/single-product.html',{'products':products_,'product':product})

