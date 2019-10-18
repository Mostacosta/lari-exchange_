from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class products_master (models.Model):
    date = models.DateField()
    image = models.ImageField(upload_to='products',null=True)

    def __str__(self):
        return str(self.date)

class products_detail(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(products_master,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title
