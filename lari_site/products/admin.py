from django.contrib import admin
from .models import products_master,products_detail
# Register your models here.

admin.site.register(products_master)
admin.site.register(products_detail)

