from django.contrib import admin
from .models import download_master,download_details
# Register your models here.

admin.site.register(download_master)
admin.site.register (download_details)

