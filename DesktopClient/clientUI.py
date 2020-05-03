from controllers.monitorController import LoginWindow
from tkinter import *


if __name__ == '__main__':
    window= Tk()
    # window.geometry('425x185+700+300')
    app = LoginWindow(window)
    window.mainloop()