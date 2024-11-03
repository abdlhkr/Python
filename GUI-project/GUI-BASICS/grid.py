from tkinter import *

# every app needs a root wich means the screan to show
root = Tk()
root.wm_attributes('-fullscreen', False)  # Tam ekranı kapalı tutar
root.wm_attributes('-type', 'normal')  # GNOME için pencere türünü ayarlar
root.geometry("500x500")
# creating things
myLabel = Label(root,text="hello tkinter")
myLabelTwo = Label(root,text="hello mom")
myLabelTree = Label(root,text="              ")
#showing on the root
myLabel.grid(row=0,column=0)
myLabelTree.grid(row=0,column=2)
myLabelTwo.grid(row=1,column=5)


myLabelFor = Label(root,text="""another way of pack or grid since 
                   python is a object oreanted program""").grid(row=1,column=3)

root.mainloop()