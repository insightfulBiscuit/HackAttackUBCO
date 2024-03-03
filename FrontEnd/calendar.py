from time import strftime, time
from tkinter import *
import datetime

from pytz import timezone

pst = timezone('Canada/Pacific')

def update():

    day_string = datetime.datetime.now(pst).strftime("%A, %B %d, %Y   " "%I:%M:%S %p"   )
    day_label.config(text=day_string)


    root.after(1000, update)

def m_function():
    print("Monday")

def t_function():
    print("Tuesday")

def w_function():
    print("Wednesday")

def th_function():
    print("Thursday")

def f_function():
    print("Friday")

def sa_function():
    print("Saturday")

def su_function():
    print("Sunday")

root = Tk()
root.title('Personal Planner')
root.geometry("350x700")

day_label = Label(root, font=('Times New Roman', 9))

day_label.grid(sticky='W', row=0, column=0, columnspan=2)

days = ["M", "T", "W", "Th", "F", "Sa", "Su"]

for i, day in enumerate(days):
  button = Button(root, text=day, font=("Arial", 12), bg="#BBC4FA",  command=eval(day.lower() + "_function"), width=1)
  button.grid(sticky='W', row=5, column=i, pady=(0, 0))

my_label = Label(root, text='Welcome to ', font=('Times New Roman ', 14, 'bold'))
my_label2 = Label(root, text='Wave', font=('Times New Roman', 14, 'bold'))

my_label.grid(sticky="W", row=3, column=0, columnspan=2, padx=(15, 0))
my_label2.grid(sticky="W", row=4, column=0, columnspan=2, padx=(15, 0))

tasks_frame = Frame(root)
tasks_frame.grid(row=6, column=0, columnspan=2, pady=(20, 10))

my_label3 = Label(tasks_frame, text='Add a Task', font=('Times New Roman', 9), relief=RIDGE)
my_label4 = Label(tasks_frame, text='Order precedence', font=('Times New Roman', 9), bg="#252BB7", fg="white", relief=RIDGE)
my_label5 = Label(tasks_frame, text='Manage your day', font=('Times New Roman', 9), relief=RIDGE)
my_label6 = Label(tasks_frame, text='Burnout', font=('Times New Roman', 9), relief=RIDGE)

my_label3.grid(row=0, column=0, padx=(10, 5))
my_label4.grid(row=0, column=3, padx=5)
my_label5.grid(sticky='E', row=1, column=0, padx=5)
my_label6.grid(sticky='E', row=1, column=3, padx=(5, 10))




update()
root.mainloop()
