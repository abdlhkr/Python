import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        count_down(work_sec)
    elif reps == 7:
        count_down(long_break)
    elif reps % 2 == 0:
        count_down(short_break)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = math.floor(count / 60)
    formatted_minute = str(minute).zfill(2)
    second = count % 60
    formatted_second = str(second).zfill(2)
    canvas.itemconfig(timer_text, text = f"{formatted_minute}:{formatted_second}")
    if count > 0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)
# canvas is a place allows us to put thing on on another

# its a method that says agter x milisecond command and inputs as args
# if you ask why are we using it instead of time.sleep window.mainloop crash with the time module
def saySomething(thing):
    print(thing)

window.after(1000,saySomething,"Hello")




label = Label(text="TIMER")
label.config(font=(FONT_NAME,35), fg=GREEN, bg= YELLOW)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
canvas.config(bg=YELLOW)
timer_text = canvas.create_text(100, 130,text="00:00",font=(FONT_NAME, 35, "bold"), fill= "white")
canvas.grid(row=1, column=1)


button_start = Button(text="Start", command = start_timer)
button_start.grid(row = 2, column = 0)

button_reset = Button(text="Reset")
button_reset.grid(row = 2 , column = 2)

label_check = Label(text="✓",fg = GREEN , bg=YELLOW)
label_check.grid(row = 3 ,column = 1)



window.mainloop()