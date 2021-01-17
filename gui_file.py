#creating the gui

#import necessary libraries
from tkinter import *
gui_obj = Tk()

#window title
gui_obj.title("Welcome to Talking2U")
gui_obj.geometry('500x600')


main_menu = Menu(gui_obj)

#create sub main menu
file_menu = Menu(gui_obj)
file_menu.add_command(label ='New Conversation')
file_menu.add_command(label='GoodBye')


main_menu.add_cascade(label='File', menu = file_menu)
main_menu.add_command(label='Quit')
gui_obj.config(menu=main_menu)


#chat awindow

chat_win = Text(gui_obj, bd=1, bg= 'black', width = 80, height = 9)
chat_win.place(x=6, y=6, height=385, width = 475)

#create messaging window

messageBox = Text(gui_obj,bg='black',width=30,height=4)
messageBox.place(x=130,y=400,height=120,width=350)

#create send button
button = Button(gui_obj, text='Enter', bg='pink', activebackground ='light blue', width =30, height=6, font =('Calibri, 13'))
button.place(x=7, y=400,height=120, width =120)

scrolling = Scrollbar(gui_obj, command =chat_win.yview())
scrolling.place(x=480, y=5,height=385)


gui_obj.mainloop()