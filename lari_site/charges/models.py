from django.db import models

# Create your models here.


class charges_headline (models.Model):
    headline = models.CharField(max_length=100)
    table_headline = models.CharField(max_length=100)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    def __str__(self):
        return self.headline

class charges_details (models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    Headline = models.ForeignKey(charges_headline,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
