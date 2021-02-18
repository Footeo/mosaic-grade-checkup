
from tkinter import *
from screens import *


#GUI 

root = Tk() 
root.title("Mosaic Grade Checkup")
root.geometry("400x400")

contentFrame = Frame(root)
contentFrame.grid(columnspan=1)

# add a menu to window
menu = Menu(root)
item = Menu(menu)
item.add_command(label="Exit", command=quit)
menu.add_cascade(label="Menu", menu=item)
root.config(menu=menu) 

screens = Screens(contentFrame)

home = Home(contentFrame,screens)
home.homeDisplay()

mainloop()





