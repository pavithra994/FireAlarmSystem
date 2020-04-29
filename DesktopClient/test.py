import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FireAlarmSystem.settings")
django.setup()

from sensor_app.models import Sensor


if __name__ == "__main__":
    c = Sensor(sensorType="CO2")
    c.save()