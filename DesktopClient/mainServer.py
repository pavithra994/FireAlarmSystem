from Pyro5 import api
from controllers.dataController import FireAlarmController


@api.expose
class Tester:
    def print(self,x):
        self.num = x
        print("Hi there!", x)
        return f"return: {x}"


deamon = api.Daemon()

remote_server_classes = {
    Tester : "test",
    FireAlarmController: "FireAlarm"
}
uri = deamon.serveSimple(remote_server_classes,host="127.0.0.1",port=9000,ns=False,verbose=True)


