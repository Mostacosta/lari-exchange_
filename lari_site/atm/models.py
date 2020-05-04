from django.db import models
from branches.models import branch_master
# Create your models here.

class atm_details (models.Model):
    adress_name = models.CharField(max_length=100)
    adress_details = models.CharField(max_length=300)
    map = models.CharField(max_length=500)
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    city = models.ForeignKey(branch_master,on_delete=models.CASCADE)

    def __str__(self):
        return self.adress_name

