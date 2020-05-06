import requests
import random
import time


while True:
    try:
        sensorId = random.randint(2,34)
        sensor_url = f"http://localhost:8000/services/sensor/{sensorId}/currentStatus"
        data = {"status": random.randint(1,10)}
        res = requests.post(url=sensor_url,data=data)
        print("Sensor: ",sensorId," Status: ",data["status"])
        time.sleep(15)
    except:
        pass



