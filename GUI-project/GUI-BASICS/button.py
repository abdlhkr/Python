from tkinter import *

root = Tk()
root.title("hello again")
# root.geometry("500x500")
def increase():
    global last_number
    last_number += 1
    text_label.config(text = f"last number : {last_number}")
    new_label = Label(root,text="I got clicked ")
    new_label.pack()

button = Button(root,text=" increase the number +1 ",command=increase)
# state DISABLED is an option if you dont wanna show that button untii some
#conditions happen
button.config(pady=50,fg="red",bg="yellow")
button.pack()
last_number = 0
text_label = Label(root,text=f"last number : {last_number}")
text_label.pack()


root.mainloop()