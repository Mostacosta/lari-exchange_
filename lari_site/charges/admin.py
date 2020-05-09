from django.contrib import admin
from .models import charges_headline,charges_details
# Register your models here.

admin.site.register(charges_details)
admin.site.register(charges_headline)