from django.contrib import admin
from .models import branch_master,branch_details
# Register your models here.

admin.site.register(branch_master)
admin.site.register(branch_details)
