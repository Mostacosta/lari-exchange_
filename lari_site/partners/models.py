from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class partners_main (models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')

    def __str__(self):
        return self.title

class points (models.Model):
    point = models.CharField(max_length=150)

    def __str__(self):
        return self.point

class partner (models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = RichTextField()
    points = models.ManyToManyField(points,blank=True)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')

    def __str__(self):
        return self.name


