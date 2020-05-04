import random

from django.test import TestCase

# Create your tests here.

from sensor_app.models import *

for i in Floor.objects.all():
    for f in range(random.randint(2,6)):
        x = 0
        room = Room(roomName=f'Room {i.floorId}{x}',floor=i)
        room.save()
        x += 1
        for s in range(random.randint(2,4)):
            sens = Sensor(room=room)
            sens.sensorType = random.choice(['CO2','SMOKE'])
            sens.sensorStatus = random.randint(1,10)
            sens.save()


