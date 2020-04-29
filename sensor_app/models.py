from django.db import models

# Create your models here.

class Sensor(models.Model):
    sensorId = models.AutoField(primary_key=True)
    __sensorType = (("CO2","CO2"),("SMOKE","SMOKE"))
    sensorType = models.CharField(max_length=15,null=True,blank=True,choices=__sensorType)
    sensorStatus = models.IntegerField(default=0)
    room = models.ForeignKey("Room",on_delete=models.CASCADE,related_name='sensor_related')


class Room(models.Model):
    roomId = models.AutoField(primary_key=True)
    floor = models.ForeignKey("Floor",on_delete=models.CASCADE,related_name="room_related")
    roomName = models.CharField(max_length=15,default="Room #")

class Floor(models.Model):
    floorId = models.AutoField(primary_key=True)
    floorName = models.CharField(max_length=15, default="Floor #")

