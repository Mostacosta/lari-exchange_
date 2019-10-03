from django.db import models

# Create your models here.
class slider_image (models.Model):
    image = models.ImageField(upload_to="home_slider")

class slider_master(models.Model):
    image = models.ManyToManyField(slider_image)

class slider_detail (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(slider_image,on_delete=models.CASCADE)

class paymentcard_master(models.Model):
    image = models.ImageField(upload_to="paymentcard")

class paymentcard_detail (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = (('eng','eng'),
                   ('ar','ar')
    )
    tag = models.CharField(max_length=5,choices=language,default='eng')
    master = models.ForeignKey(paymentcard_master,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



    