
from tkinter import *
import math

PINK= "#FFF5E1"
ORANGE= "#FF6969"
MARRON= "#C80036"
NAVY = "#0C1844"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps=0
timer=None


def reset_timer(): 
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt,text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
    start_button.config(state="normal")


def start_timer():
    global reps
    reps+=1
    start_button.config(state="disabled")
    work_Sec=WORK_MIN*60
    l_b_s=LONG_BREAK_MIN*60
    s_b_S=SHORT_BREAK_MIN*60

    if reps % 8==0:
        count_down(l_b_s)
        title_label.config(text="Break",fg=MARRON)

    elif reps%2==0:
        count_down(s_b_S)
        title_label.config(text="Break",fg=PINK)
    else:        
        count_down(work_Sec)
        title_label.config(text="Work Time")


def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_txt,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer() 
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✅"

        check_mark.config(text=mark)
        start_button.config(state="normal")       


window=Tk()
window.title("Pomodoro")
window.config(padx=30,pady=30,bg=NAVY)
title_label=Label(text="timer",fg=PINK,bg=NAVY, font=(FONT_NAME,25,"bold"))
title_label.grid(column=1,row=0)

canvas=Canvas(width=208,height=224,bg=NAVY,highlightthickness=0)
pomodoro_img=PhotoImage(file="/home/krishna/Documents/python/day26-30/day28/pomodoro-start/tomato.png")
canvas.create_image(104,112,image=pomodoro_img)
timer_txt=canvas.create_text(104,127,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button=Button(text="Start",fg=NAVY,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",fg=NAVY,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark=Label(fg=ORANGE ,bg=NAVY)
check_mark.grid(column=1,row=3)

window.mainloop()

#text="✅",