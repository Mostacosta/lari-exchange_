from django.db import models

# Create your models here.
class paymax_questions(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')

    def __str__(self):
        return self.question

class GCard_questions(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')

    def __str__(self):
        return self.question

