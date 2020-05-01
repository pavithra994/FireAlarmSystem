from django.apps import AppConfig


class SensorAppConfig(AppConfig):
    name = 'sensor_app'

    def ready(self):
        import sensor_app.signals