import tkinter as tk


root = tk.Tk()

entry = tk.Entry(width=30,border=5)
entry.grid(row=0,column=0,columnspan=3)

def getNumber(number):
    current = entry.get()
    entry.insert(tk.END,str(number))
    # first parametre of the insert defines where shoul the number be inserted

def calculate():
    current = entry.get()
    entry.delete(0,tk.END)
    result = eval(current)
    entry.insert(0,result)   
    # eval function is used to evaluate the string expression directly 

numberSeven = tk.Button(text=7,width=10,height=5,command=lambda: getNumber(7))
numberSeven.grid(row=1,column=0)

numberEight = tk.Button(text=8,width=10,height=5,command=lambda: getNumber(8))
numberEight.grid(row=1,column=1)

numberNine = tk.Button(text=9,width=10,height=5,command=lambda: getNumber(9))
numberNine.grid(row=1,column=2)


numberSeven = tk.Button(text=6,width=10,height=5,command=lambda: getNumber(6))
numberSeven.grid(row=2,column=0)

numberEight = tk.Button(text=5,width=10,height=5,command=lambda: getNumber(5))
numberEight.grid(row=2,column=1)

numberNine = tk.Button(text=4,width=10,height=5,command=lambda: getNumber(4))
numberNine.grid(row=2,column=2)

numberSeven = tk.Button(text=3,width=10,height=5,command=lambda: getNumber(3))
numberSeven.grid(row=3,column=2)

numberEight = tk.Button(text=2,width=10,height=5,command=lambda: getNumber(2))
numberEight.grid(row=3,column=1)

numberNine = tk.Button(text=1,width=10,height=5,command=lambda: getNumber(1))
numberNine.grid(row=3,column=0)

numberZero = tk.Button(text=0,width=10,height=5,command=lambda: getNumber(0))
numberZero.grid(row=4,column=0)

clearButton = tk.Button(text="Clear", width=20,height=5,command=lambda: entry.delete(0,tk.END))
clearButton.grid(row=5,column=1,columnspan=2)

plusButton = tk.Button(text="+", width=10,height=5,command=lambda: getNumber("+"))
plusButton.grid(row=5,column=0)

subtractionButton = tk.Button(text="-", width=10,height=5,command=lambda: getNumber("-"))
subtractionButton.grid(row=6,column=0)

devideButton = tk.Button(text="/", width=10,height=5,command=lambda: getNumber("/"))
devideButton.grid(row=4,column=1)

multiplyButton = tk.Button(text="*", width=10,height=5,command=lambda: getNumber("*"))
multiplyButton.grid(row=4,column=2)

equalButton = tk.Button(text="=", width=20,height=6,command=calculate)
# eval() function is used to evaluate the string expression directly
equalButton.grid(row=6,column=1,columnspan=2)

root.mainloop()
