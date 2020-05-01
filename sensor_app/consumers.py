import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
from asgiref.sync import async_to_sync



# class SensorConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print("web socket connected")
#         await self.send(
#             {
#                 "type":"websocket.accept"
#             }
#         )
#
#     async def websocket_disconnect(self, event):
#         print("web socket disconnected")
#
#     async def websocket_receive(self, event):
#         print("websocket received a message: ",event)
#         await self.send({
#             "type":"websocket.send",
#             "text": event["text"]
#         })

# class SensorConsumer(AsyncWebsocketConsumer):
#     # async def websocket_connect(self, event):
#     #     print("web socket connected")
#     #     self.group_name = 'web_client'
#     #
#     #     await self.channel_layer.group_add(
#     #                 self.group_name,
#     #                 self.channel_name
#     #             )
#     #     await self.accept()
#
#     async def connect(self):
#         print("web socket connected")
#         self.group_name = 'web_client'
#
#         await self.channel_layer.group_add(
#                     self.group_name,
#                     self.channel_name
#                 )
#         await self.accept()
#
#
#     async def websocket_receive(self, event):
#         print("websocket_receive")
#
#
#     async def message_send(self,event):
#         self.message = event['message']
#         await self.send(text_data=json.dumps(
#             {
#                 'message': self.message
#             }
#         ))


class SensorConsumer(WebsocketConsumer):
    def connect(self):
        self.groups_name = "web_client"
        async_to_sync(self.channel_layer.group_add)(
            self.groups_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.groups_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.groups_name,
            {
                'type': 'send_message',
                'message': message
            }
        )

    def send_message(self, event):
        print("send message event: ",event)
        message = event['text']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))