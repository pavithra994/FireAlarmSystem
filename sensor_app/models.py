from django.db import models

# Create your models here.

class Sensor(models.Model):
    sensorId = models.AutoField(primary_key=True)
    sensorType = models.CharField(max_length=15,null=True,blank=True)
