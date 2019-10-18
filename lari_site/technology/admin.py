from django.contrib import admin
from .models import technologies,technology_detail,technology_master
# Register your models here.
admin.site.register(technologies)
admin.site.register(technology_detail)
admin.site.register(technology_master)
