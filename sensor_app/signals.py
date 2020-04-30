import channels.layers
from asgiref.sync import async_to_sync

from django.db.models.signals import post_save
from django.dispatch import receiver

from sensor_app.models import Sensor
import json


def send_message(event):
    '''
    Call back function to send message to the browser
    '''
    message = event['text']
    channel_layer = channels.layers.get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        message
    ))


@receiver(post_save, sender=Sensor)
def sensor_post_save(sender, instance, **kwargs):
    print("sensor post saver triggered")
    group_name = 'web_client'

    message = {
        'sensorId': instance.sensorId,
        'status': instance.sensorStatus,
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'send_message',
            'text': message
        }
    )