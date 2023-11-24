# This is a sample Python script.
'''from tkinter import *
import tkinter as tk

top = tk.Tk()
f=Frame(top, width=500, height=500,cursor="cross")
f.propagate(1)
f.pack()
w = tk.Button(f, text ="REMINDER", width=17, height=3)
w.pack()
w.bind("<Button-1>")
top.mainloop()'''



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import time
from tkinter import *
import vlc
class MyEntry:
    def __init__(self, root):
        self.f=Frame(root,height=500, width=500)
        self.f.propagate(0)
        self.f.pack()
        self.l1=Label(text="Tittle for the reminder")
        self.l2 = Label(text="Set time")
        self.el=Entry(self.f, width=25)
        self.el.bind("<Return>", self.display)
        self.e2=Entry(self.f, width=20)
        self.e2.bind("<Return>", self.display)
        self.l1.place(x=50,y=100)
        self.el.place(x=200,y=100)
        self.l2.place(x=50,y=150)
        self.e2.place(x=200,y=150)
        self.b = Button(self.f, text='SET', command=self.display)
        self.b.place(x=180, y=350)

    def alarm(self):
        alarm_time=self.e2.get()
        print(alarm_time)

    def display(self):
        str1 = self.el.get()
        str2 = self.e2.get()
        #current_time= current_time.get()

        lbl1 = Label(text='Reminder set for :  ' + str1).place(x=50, y=200)
        lbl2 = Label(text='Alarm will be triggered at :  ' + str2).place(x=50, y=220)
        #lbl3=Label(text="Current Time =" + current_time).place(x=50,y=230)
        #lbl3=Label(text="Task Time = "+  alarm_time).place(x=50,y=250)


root=Tk()
mb = MyEntry(root)
root.mainloop()



