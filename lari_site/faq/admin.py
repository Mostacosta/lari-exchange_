from django.contrib import admin
from .models import GCard_questions,paymax_questions,general_questions
# Register your models here.

admin.site.register(GCard_questions)
admin.site.register(paymax_questions)
admin.site.register(general_questions)