from django.db import models

# Create your models here.
class products_master (models.Model):
    date = models.DateField()

class products_detail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(products_master,on_delete=models.CASCADE)
