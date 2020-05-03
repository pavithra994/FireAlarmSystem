# from Pyro5 import api
from controllers.dataController import FireAlarmController
import socket
import Pyro4


@Pyro4.expose
class Tester:
    def print(self,x):
        self.num = x
        print("Hi there!", x)
        return f"return: {x}"

# sensor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(socket.gethostname())
# sensor_socket.bind((socket.gethostname(),9090))
# sensor_socket.listen(16)

deamon = Pyro4.Daemon()

# remote_server_classes = {
#     Tester : "test",
#     FireAlarmController: "FireAlarm"
# }
# uri = deamon.serveSimple(remote_server_classes,host="127.0.0.1",port=9000,ns=False,verbose=True)
ns = Pyro4.locateNS()
# uri = deamon.register(Tester)
uri = deamon.register(FireAlarmController)
ns.register("FireAlarm",uri)
print("done...")
deamon.requestLoop()
