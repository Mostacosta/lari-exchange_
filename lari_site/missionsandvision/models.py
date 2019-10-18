from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class mission_master (models.Model):
    img = models.ImageField(upload_to="ceo")

class mission_detail(models.Model):
    title = models.CharField(max_length=100)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    description = RichTextField()
    master = models.ForeignKey(mission_master,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title