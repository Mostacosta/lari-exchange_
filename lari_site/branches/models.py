from django.db import models

# Create your models here.

class branch_master (models.Model):
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class branch_details (models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    map = models.CharField(max_length=500)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    city = models.ForeignKey(branch_master,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
