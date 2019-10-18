from django.contrib import admin
from .models import contact_form,contact_info
# Register your models here.
admin.site.register(contact_form)
admin.site.register(contact_info)