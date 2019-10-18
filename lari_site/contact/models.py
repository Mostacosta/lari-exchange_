from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class contact_info (models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')

    def __str__(self):
        return self.title

class contact_form (models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    