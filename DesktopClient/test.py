import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FireAlarmSystem.settings")
django.setup()

from sensor_app.models import Sensor


if __name__ == "__main__":
    c = Sensor.objects.get(room_id=1)
    c.sensorStatus = 7
    c.save()