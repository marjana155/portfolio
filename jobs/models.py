from django.db import models

# Create your models here.


class Job(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)
    title = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
