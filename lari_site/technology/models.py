from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class technology_master (models.Model):
    img = models.ImageField(upload_to="ceo")

class technology_detail(models.Model):
    main_title = models.CharField(max_length=100)
    main_description = RichTextField()
    sub_description = RichTextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(technology_master,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.main_title

class technologies (models.Model):
    title = models.CharField(max_length=100)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')

    def __str__(self):
        return self.title
