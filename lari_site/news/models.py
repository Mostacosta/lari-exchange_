from django.db import models

# Create your models here.
class news_master (models.Model):
    image = models.ImageField(upload_to="news")
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class news_detail (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(news_master,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

