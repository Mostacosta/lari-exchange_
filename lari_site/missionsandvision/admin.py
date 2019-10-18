from django.contrib import admin
from .models import mission_detail,mission_master

# Register your models here.

admin.site.register(mission_detail)
admin.site.register(mission_master)

