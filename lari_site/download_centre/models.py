from django.db import models

# Create your models here.
class download_master (models.Model):
    pdf_file = models.FileField(upload_to="files")

class download_details (models.Model):
    description = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(download_master,on_delete=models.CASCADE)

    def __str__(self):
        return self.description[0:20]
