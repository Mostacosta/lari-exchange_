from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ceo_master (models.Model):
    img = models.ImageField(upload_to="ceo")

class ceo_detail(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    description = RichTextField()
    master = models.ForeignKey(ceo_master,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title