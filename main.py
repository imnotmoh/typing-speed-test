from tkinter import *
import time

window = Tk()
window.config(pady=30,padx=30)
start_time = None
timer = None
speed = 0
label = Label(text="type in here")
label.grid(column=0,row=0)
text_input = Entry()
text_input.grid(column=1,row=0,columnspan=3)
speed_label = Label(text=f"speed:{speed} cps")
speed_label.grid(row=1, column=2)



def cal_speed(inp):
    global start_time
    global timer
    global speed
    if inp != None:
        if start_time == None:
            start_time = time.time()
        time_now = time.time()
        typing_time = time_now - start_time
        if typing_time != 0:
            speed = round(len(inp) / typing_time,2)
        speed_label.config(text=f"speed:{speed} cps")
        timer = window.after(1000,cal_speed, text_input.get())
    else:cal_speed(text_input.get())

def reset():
    global timer
    global start_time
    global speed
    speed = 00
    start_time =None
    text_input.delete(0, END)
    window.after_cancel(timer)
    cal_speed(text_input.get())


reset_button = Button(text="reset",command=reset)
reset_button.grid(row=3,column=2)
cal_speed(text_input.get())
window.mainloop()
