from tkinter import *

current_image = 0
def before():
    global current_image 
    if current_image > 0:
        current_image = current_image - 1
    else:
        current_image = len(image_list) - 1 
    photo_label.config(image=image_list[current_image])
    

def after():
    global current_image
    if current_image < len(image_list) - 1:
        current_image = current_image + 1
    else:
        current_image = 0
    photo_label.config(image=image_list[current_image])
    
root = Tk()


first_image = PhotoImage(file= "images/image.png")
second_image= PhotoImage(file = "images/images.png")

image_list = [first_image,second_image]

print(len(image_list))

photo_label = Label(image=first_image)
photo_label.grid(row=0,column=0,columnspan=3)

before_button = Button(root,text= "<<" , command= before)
before_button.grid(row=1,column=0)

quit_button = Button(root,text="quit", command=root.quit)
quit_button.grid(row=1,column=1)

after_button = Button(root,text=">>",command=after)
after_button.grid(row = 1, column = 2)





root.mainloop()