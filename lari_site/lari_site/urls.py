"""lari_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import currency_table,home_view,change_lang
from django.conf.urls.static import static
from django.conf import settings
from contact.views import contact_view,job_view
from about.views import about_view
from ceo.views import ceo_view
from missionsandvision.views import mission_view
from products.views import products_view,products_detail_view
from technology.views import technology_view
from faq.views import questions_view
from partners.views import partner_view
from news.views import news_view,news_details_view
from rates.views import rates_view
from django.views.generic import TemplateView
from branches.views import branch_view
from atm.views import atm_view
from download_centre.views import pdf_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('contact',contact_view,name="contact"),
    path('about',about_view,name="about"),
    path('ceo',ceo_view,name="ceo"),
    path('mission',mission_view,name="mission"),
    path('products',products_view,name="products"),
    path('technology',technology_view,name="technology"),
    path ('faq',questions_view,name='faq'),
    path ('partner',partner_view,name='partner'),
    path('news',news_view,name='news'),
    path('news/<int:pk>',news_details_view,name='news_details'),
    path('product/<int:pk>',products_detail_view,name='product_detail'),
    path('rates',rates_view,name='rates'),
    path('lang',change_lang,name='lang'),
    path('privacy', TemplateView.as_view(template_name='footer/privacy-policy.html'),name='privacy'),
    path('termscondition', TemplateView.as_view(template_name='footer/terms-conditions.html'),name='condition'),
    path('termsuse', TemplateView.as_view(template_name='footer/terms-use.html'),name='use'),
    path('branches',branch_view,name='branches'),
    path('atm',atm_view,name='atm'),
    path('careers',job_view,name='jobs'),
    path('aboutmain', TemplateView.as_view(template_name='about/about-main.html'),name='aboutmain'),
    path('download', TemplateView.as_view(template_name='download/download.html'),name='download')


]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
