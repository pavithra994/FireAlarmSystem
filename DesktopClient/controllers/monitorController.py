from tkinter import *
from tkinter import ttk
"""
___________________________________________________________
Fire Alarm Window                                  - | x  
___________________________________________________________
Add Floor       +   |   *** Floor 1 ***     Add Room    + 
____________________|   -----------------------------------
>   Floor 1    *edit|  * Room 10  ( # sensors - 2 )  *edit
    Floor 2    *edit|       |- Sensor #312 | CO2 | status
    Floor 3    *edit|       |- Sensor #315 | SMK | status
                    |  * Room 11  ( # sensors - 1 )  *edit
                    |       |- Sensor #212 | CO2 | status

"""
class FireAlarmDashboard(Frame):
    def __init__(self,remoteObj,selectedFloor=None):
        super().__init__()
        self.sensorDetails = remoteObj.get_sensors_updates()
        print(self.sensorDetails)
        self.intiUI()
        self.selectedFloor = selectedFloor
        if selectedFloor:
            self.floor_label_click(id=self.selectedFloor)


    def intiUI(self):
        floors_list = [
            {"floorId": 1, "floorName": "Floor 1"},
            {"floorId": 2, "floorName": "Floor 2"},
            {"floorId": 3, "floorName": "Floor 3"},
        ] # hard corded values

        self.floors_label_list = []  # list of{"floorId":12,"floorLabel":LabelObj}
        self.rooms_label_list = []  # list of{"roomId":12,"roomFrame":FrameObj}


        self.master.title('Fire Alarm | Dashboard')
        # Root frame
        # self.pack(expand='yes',fill='both')
        self.grid(sticky=E+W+S+N)
        floor_list_frame = Frame(self,width=20,bd=1, relief=RIDGE)
        floor_list_frame.pack(anchor="w",side=LEFT,expand='no',fill='y')
        floor_list_frame.config(background='ghost white')
        # floor_list_frame.columnconfigure(1,weight=1)


        l = Label(floor_list_frame,text="Floors list",bg="saddle brown",width=20)
        l.pack()


        for f in self.sensorDetails:
            l = Label(floor_list_frame,text=f['floorName'],bg="white",width=20)
            self.floors_label_list.append({"floorId":f['floorId'],"floorLabel":l})
            l.pack()
            l.bind('<Button-1>',lambda event,l=f['floorId']:self.floor_label_click(event,l))

        self.room_list_frame = Frame(self,bd=1)
        self.room_list_frame.pack(anchor="w",side=LEFT,expand='no',fill='both')
        # self.room_list_frame.config()

        rooms_title_label = Label(self.room_list_frame,text="Rooms List")
        rooms_title_label.pack(fill='x')
        # b1 = RoomFrame(room_list_frame,floorId=2)
        # b1.pack()

    def floor_label_click(self,event=None,id=None):
        print(id)
        self.selectedFloor = id
        if event:
            event.widget.config(bg='light blue')

        self.load_rooms(id)
        # todo remove existing rooms and load new rooms
        for l in self.floors_label_list:
            if l['floorId'] != id:
                l['floorLabel'].config(bg="old lace",relief=FLAT)
            else:
                l['floorLabel'].config(bg="seashell4",relief=SUNKEN)


    def load_rooms(self,floorId=None):
        # todo: get room list from all status service by floor id
        for f in self.sensorDetails:
            if f['floorId'] != floorId:
                continue
            else:
                room_list = f['rooms']
                break

        for w in self.room_list_frame.winfo_children():
            w.destroy()
        rooms_title_label = Label(self.room_list_frame, text=f"Floor #{floorId} | List of Rooms",width=500)
        rooms_title_label.pack(fill='x')
        room_label_list = []
        for r in room_list:
            room = RoomFrame(self.room_list_frame,roomId=r['roomId'],roomName=r['roomName'],sensorList=r['sensors'],relief=SUNKEN)
            room.pack(padx=5, pady=5)
            room_label_list.append({"roomId":r['roomId'],"roomFrame":room})

class RoomFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self,parent)
        self.roomId = kwargs['roomId']
        self.roomName = kwargs['roomName']
        self.sensorList = kwargs['sensorList']
        self.intiUI()

    def intiUI(self):
        self.pack(expand='no', fill='both')
        self.config(bg="green")
        name_label = Label(self,text=self.roomName,bg="yellow")
        name_label.pack(anchor="w")

        for s in self.sensorList:
            print(s)
            sensor_frame = Frame(self)
            sensor_frame.columnconfigure(0,weight=2)
            sensor_frame.columnconfigure(1,weight=1)
            sensor_frame.columnconfigure(2,weight=1)
            sensor_frame.columnconfigure(3,weight=1)
            sensor_frame.columnconfigure(4,weight=1)
            sensor_frame.columnconfigure(5,weight=1)
            sensor_frame.pack(anchor='w')
            sensor_id_label = Label(sensor_frame,text=f"Sensor ID #{s['sensorId']} : ",bg="white",width=20)
            sensor_id_label.grid(row=0,column=0,sticky='w')
            print(s['sensorType'])
            x= s['sensorType']
            sensor_name_label = Label(sensor_frame,text=f" Type: {x}",bg="white",width=15,anchor='w')
            sensor_name_label.grid(row=0,column=1,sticky='w')
            sensor_reading_label = Label(sensor_frame,text=f" Reading: {s['sensorStatus']}",bg="white",width=15)
            sensor_reading_label.grid(row=0,column=2,sticky='w')
            colour_code={
                1: "green3",
                2: "green2",
                3: "SpringGreen3",
                4: "green yellow",
                5: "yellow",
                6: "orange",
                7: "dark orange",
                8: "orange red",
                9: "red",
                10: "red3",
            }
            sensor_colour_label = Label(sensor_frame,text=" ",bg=colour_code[s['sensorStatus']],width=2,bd=1)
            sensor_colour_label.grid(row=0,column=2,sticky='w')

            b = Button(sensor_frame,text="edit")
            b.grid(row=0,column=3,sticky='e')

        # l = Label(self,text=self.roomName,bg="white").pack()

class LoginWindow(Frame):
    def __init__(self,root):
        super().__init__()
        self.intiUI()
        self.root = root

    def intiUI(self):
        self.master.title("Fire Alarm | Admin Login")
        self.grid(sticky=W+E+S+N)

        rows = 0
        while rows<10:
            self.rowconfigure(rows, weight=1)
            self.columnconfigure(rows, weight=1)
            rows+=1

        '''Username and Password'''

        frame = LabelFrame(self, text='Login')
        frame.grid(row = 1,column = 1,columnspan=10,rowspan=10)

        Label(frame, text = ' Usename ').grid(row = 2, column = 1, sticky = W)
        self.username = Entry(frame)
        self.username.grid(row = 2,column = 2)

        Label(frame, text = ' Password ').grid(row = 5, column = 1, sticky = W)
        self.password = Entry(frame, show='*')
        self.password.grid(row = 5, column = 2)

        # Button

        ttk.Button(frame, text = 'LOGIN',command = self.login_user).grid(row=7,column=2)
        #ttk.Button(frame, text='FaceID(Beta)',command = self.face_unlock).grid(row=8, column=2)

        '''Message Display'''
        self.message = Label(text = '',fg = 'Red')
        self.message.grid(row=9,column=6)

    def login_user(self):
        import Pyro4

        fire = Pyro4.Proxy("PYRONAME:FireAlarm")
        # if fire.login(self.username.get(),self.password.get()):
        if fire.login('admin@test.lk','password'):
            self.destroy()
            self.root.geometry("720x720")
            app = FireAlarmDashboard(fire)

        else:
            self.message['text'] = 'Email or password incorrect. Try again'

s = sensorDetails = [
                                {
                                    "floorId": 1,
                                    "floorName": "Floor 1",
                                    "rooms": [
                                        {
                                            "roomId": 1,
                                            "roomName": "Room 10",
                                            "sensors": [
                                                {
                                                    "sensorId": 1,
                                                    "sensorType": "CO2",
                                                    "sensorStatus": 7
                                                },
                                                {
                                                    "sensorId": 2,
                                                    "sensorType": "SMOKE",
                                                    "sensorStatus": 7
                                                }
                                            ]
                                        },
                                        {
                                            "roomId": 2,
                                            "roomName": "Room 11",
                                            "sensors": [
                                                {
                                                    "sensorId": 3,
                                                    "sensorType": "CO2",
                                                    "sensorStatus": 7
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "floorId": 2,
                                    "floorName": "Floor 2",
                                    "rooms": [
                                        {
                                            "roomId": 13,
                                            "roomName": "Room 10",
                                            "sensors": [
                                                {
                                                    "sensorId": 5,
                                                    "sensorType": "CO2",
                                                    "sensorStatus": 7
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]

# main_window = Tk()
# main_window.geometry("720x720")
# app = LoginWindow()
#
# main_window.mainloop()


# if __name__ == '__main__':
#


#############3333

#
#
# content = ttk.Frame(self, padding=(3, 3, 12, 12))
#
#         floor_list_frame = ttk.Frame(content)
#         room_list_frame = ttk.Frame(content)
#
#         fl1 = ttk.Label(floor_list_frame,text="Floor 1")
#         fl2 = ttk.Label(floor_list_frame,text="Floor 2")
#         fl3 = ttk.Label(floor_list_frame,text="Floor 3")
#
#         rl1 = ttk.Label(room_list_frame,text="Room 13")
#         rl2 = ttk.Label(room_list_frame,text="Room 14")
#         rl3 = ttk.Label(room_list_frame,text="Room 15")
#
#         content.grid(column=0, row=0, sticky=(N, S, E, W))
#
#         floor_list_frame.grid(column=0,row=0, sticky=(N, S, E, W),columnspan=2)
#         room_list_frame.grid(column=1,row=0, sticky=(N, S, E, W),columnspan=3)
#
#         fl1.grid(column=0,row=0, sticky=(N, W), padx=5)
#         fl2.grid(column=0,row=1, sticky=(N, W), padx=5)
#         fl3.grid(column=0,row=2, sticky=(N, W), padx=5)
#
#
#         rl1.grid(column=0,row=0, sticky=(N, W), padx=5)
#         rl2.grid(column=0,row=1, sticky=(N, W), padx=5)
#         rl3.grid(column=0,row=2, sticky=(N, W), padx=5)
#
#         self.grid(column=0,row=0, sticky=(N, S, E, W))
#
#
#
#         # row and col configure root
#         self.columnconfigure(0,weight=1)
#         self.rowconfigure(0,weight=1)
#
#         content.columnconfigure(0, weight=1)
#         content.columnconfigure(1, weight=1)
#         content.columnconfigure(2, weight=1)
#         content.columnconfigure(3, weight=1)
#         content.columnconfigure(4, weight=1)
#         content.rowconfigure(0, weight=1)
#
#         # row and col configure floor list
#         floor_list_frame.columnconfigure(0,weight=4)
#         floor_list_frame.columnconfigure(1,weight=1)