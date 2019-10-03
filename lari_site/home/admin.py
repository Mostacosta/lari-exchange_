from django.contrib import admin
from .models import slider_detail,slider_image,slider_master,paymentcard_master,paymentcard_detail

# Register your models here.
admin.site.register(slider_master)
admin.site.register(slider_image)
admin.site.register(slider_detail)
admin.site.register(paymentcard_master)
admin.site.register(paymentcard_detail)