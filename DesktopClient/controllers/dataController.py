import requests
import json
from Pyro5.api import expose
from .configurations import SERVICES


@expose
class FireAlarmController:
    """FireAlarmController class handles as remote server which control sensor api requests and responses"""
    def __init__(self):
        self.fire_alarm_rest_api = "http://127.0.0.1:8000/"
        self.token = None

    def add_or_edit_floor(self,floor_name,floor_id=None):
        if not self.token:
            pass # todo: handle the error
        data = {"floorName":floor_name}
        if floor_id:
            data["floorId"] = floor_id
        header = {
            "Authorization": "Token " + self.token,
            "Content-Type": "multipart/form-data"
        }

        _response = requests.post(self.fire_alarm_rest_api+SERVICES["ADD_FLOOR"],data=data,headers=header)
        # todo: handle the rest (errors)

    def add_or_edit_room(self,room_name,floor_id,room_id=None):
        if not self.token:
            pass  # todo: handle the error
        data = {"floorId": floor_id, "roomName": room_name}
        if room_id:
            data["roomId"] = room_id
        header = {
            "Authorization": "Token " + self.token,
            "Content-Type": "multipart/form-data"
        }

        _response = requests.post(self.fire_alarm_rest_api + SERVICES["ADD_ROOM"],data=data,headers=header)
        # todo: handle the rest (errors)

    def add_or_edit_sensor(self,sensor_type,room_id,sensor_id=None):
        if not self.token:
            pass  # todo: handle the error
        data = {"roomId": room_id, "sensorType": sensor_type}
        if sensor_id:
            data["sensorId"] = sensor_id
        header = {
            "Authorization": "Token " + self.token,
            "Content-Type": "multipart/form-data"
        }

        _response = requests.post(self.fire_alarm_rest_api + SERVICES["ADD_SENSOR"],data=data,headers=header)
        # todo: handle the rest (errors)

    def get_sensors_updates(self):
        if not self.token:
            pass  # todo: handle the error

        header = {
            "Authorization": "Token " + self.token,
            # "Content-Type": "multipart/form-data" # todo: test

        }
        _response = requests.get(self.fire_alarm_rest_api + SERVICES["ALL_DETAILS"],headers=header)
        return _response.json()

    def login(self,email,password):
        data = {"email":email, "password":password}

        _response = requests.post(self.fire_alarm_rest_api + SERVICES["LOGIN"], data=data)

        res_dict = _response.json()
        print(res_dict)
        if res_dict.get("code"):
            self.token = res_dict["payload"]["token"]
            print("login success...")
            return self.token
        else:
            pass # todo: handle errors

    def logout(self):
        self.token = None




