"""FireAlarmSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from sensor_app.views import *
from auth_app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    url('service/manage/floor$', manage_floor, name="manage_floor"),
    url('service/manage/room$', manage_room, name="manage_room"),
    url('service/manage/sensor$', manage_sensor, name="manage_sensor"),
    url('service/sensor/all$', all_sensor_status, name="all_sensor_status"),
    url('services/sensor/(?P<sensorId>[^/]+)/currentStatus$', sensor_readings, name="sensor_readings"),

    url('service/user/login$', login, name="login"),

]
