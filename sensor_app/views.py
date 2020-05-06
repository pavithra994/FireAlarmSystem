from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from sensor_app.forms import LoginForm
from sensor_app.models import Floor, Room, Sensor
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def manage_floor(request):
    """
        ** Form data
    Add new floor : without floorId
    update a floor : with floorId
    Service call : /service/manage/floor
    """
    requestData = request.POST

    try:
        if requestData.get("floorId"):
            floor_obj = Floor.objects.get(floorId=requestData['floorId'])
        else:
            floor_obj = Floor()
    except:
        return JsonResponse({"message":"invalid floor id"}, status=400, safe=False)

    floor_obj.floorName = requestData.get('floorName')

    floor_obj.save()

    responseData = {
        "message": "successful response",
        "code": 200,
        "payload": {
            "floorId": floor_obj.floorId
        }
    }

    return JsonResponse(responseData, status=200, safe=False)


@api_view(['POST'])
def manage_room(request):
    """
        ** Form data
    Add new room : without roomId
    update a room : with roomId
    Service call : /service/manage/room
    """
    requestData = request.POST

    try:
        if requestData.get("roomId"):
            room_obj = Room.objects.get(roomId=requestData['roomId'])
        else:
            room_obj = Room()
    except:
        return JsonResponse({"message": "invalid room id"}, status=400, safe=False)

    try:
        floor_obj = Floor.objects.get(floorId=requestData.get("floorId"))
    except:
        return JsonResponse({"message":"invalid floor id"}, status=400, safe=False)

    room_obj.floor = floor_obj
    room_obj.roomName = requestData.get('roomName')

    room_obj.save()

    responseData = {
        "message": "successful response",
        "code": 200,
        "payload": {
            "roomId": room_obj.roomId
        }
    }

    return JsonResponse(responseData, status=200, safe=False)


@api_view(['POST'])
def manage_sensor(request):
    """
        ** Form data
    Add new sensor : without sensorId
    update a sensor : with sensorId
    Service call : /service/manage/sensor
    """
    requestData = request.POST

    try:
        if requestData.get("roomId"):
            sensor_obj = Sensor.objects.get(sensorId=requestData['sensorId'])
        else:
            sensor_obj = Sensor()
    except:
        return JsonResponse({"message": "invalid sensor id"}, status=400, safe=False)

    try:
        room_obj = Room.objects.get(roomId=requestData['roomId'])
    except:
        return JsonResponse({"message": "invalid room id"}, status=400, safe=False)

    sensor_obj.room = room_obj
    sensor_obj.sensorType = requestData.get('sensorType')

    sensor_obj.save()

    responseData = {
        "message": "successful response",
        "code": 200,
        "payload": {
            "roomId": sensor_obj.sensorId
        }
    }

    return JsonResponse(responseData, status=200, safe=False)


@api_view(['POST'])
@permission_classes((AllowAny,))
def sensor_readings(request,sensorId):
    """
    POST service **form data
    submit the sensor status: status = 1-10
    service call : /services/sensor/currentStatus
    """
    try:
        sensor_obj = Sensor.objects.get(sensorId=sensorId)
    except:
        return JsonResponse({"message": "invalid sensor id"}, status=400, safe=False)

    sensor_obj.sensorStatus = int(request.POST.get("status"))
    sensor_obj.save()

    return JsonResponse({"message":"successful update the sensor value"}, status=200, safe=False)


@api_view(['GET'])
def all_sensor_status(request):
    floors = []
    for _floor in Floor.objects.all():
        rooms = []
        for _room in _floor.room_related.all():
            sensors = []
            for _sensor in _room.sensor_related.all():
                sensors.append(
                    {
                        "sensorId": _sensor.sensorId,
                        "sensorType": _sensor.sensorType,
                        "sensorStatus": _sensor.sensorStatus
                    }
                )
            rooms.append(
                {
                    "roomId": _room.roomId,
                    "roomName": _room.roomName,
                    "sensors": sensors
                }
            )
        floors.append(
            {
                "floorId": _floor.floorId,
                "floorName": _floor.floorName,
                "rooms": rooms
            }
        )

    responseData = {
        "message": "successful response",
        "code": 200,
        "payload": floors
    }

    return JsonResponse(responseData, status=200, safe=False)


def view_sensors(request):
    return render(request, 'allsensor.html', {
        'room_name': "test_channel"
    })


def index(request,floorId=None):
    if not request.user.is_authenticated:
        print("nonn")
        return redirect('/login')

    roomQs = Room.objects.all()
    floorName = None
    if floorId:
        roomQs = roomQs.filter(floor__floorId=floorId)
    floors_list = []
    for f in Floor.objects.all():
        try:
            if f.floorId == int(floorId):
                floorName = f.floorName
        except:
            pass
        floors_list.append(
            {
                "floorName": f.floorName,
                "floorId": f.floorId,
                "alert": True
            }
        )

    rooms = []
    for _room in roomQs:
        sensors = []
        is_room_alart = False
        for _sensor in _room.sensor_related.all():
            if _sensor.sensorStatus > 5:
                is_room_alart= True
                for f in floors_list:
                    if f['floorId'] == _room.floor_id:
                        f['alert'] = True

            sensors.append(
                {
                    "sensorId": _sensor.sensorId,
                    "sensorType": _sensor.sensorType,
                    "sensorStatus": _sensor.sensorStatus
                }
            )
        rooms.append(
            {
                "roomId": _room.roomId,
                "roomName": _room.roomName,
                "floorId": _room.floor_id,
                "floorName": _room.floor.floorName,
                "sensors": sensors,
                "alert":is_room_alart
            }
        )


    context = {
        "floorList":floors_list,
        "rooms":rooms,
        "selectedFloor":floorId,
        "selectedFloorName":floorName,
        "user": request.user.email

    }
    return render(request,'index.html',context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)

        if user:
            print("auth...")
            token, e = Token.objects.get_or_create(user=user)
            response = redirect('home')
            response['Authorization'] = f"Token {token.key}"
            return response
        else:
            return redirect('/')


    context = {
        "form":form
    }
    return render(request,'login.html',context)


def log_out(request):
    logout(request)
    return redirect('/login')
