import tkinter as tk

window = tk.Tk()


def takeEntry():
    text = entry.get()
    print(text)

entry = tk.Entry(window)
entry.insert(0,"type something")
entry.grid(row=0,column=0)

button = tk.Button(window,text="send",command=takeEntry)
button.grid(row=0,column=1)

window.mainloop()