from django.contrib import admin
from .models import news_master,news_detail,cards
# Register your models here.
admin.site.register(news_master)
admin.site.register(news_detail)
admin.site.register(cards)