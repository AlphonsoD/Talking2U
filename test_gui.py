import tkinter

def send(event = None):
    msg = 'Alphonso: ' + message.get()
    message.set("")
    message_list.insert(tkinter.END, msg)

def on_closing():
    chatbox.quit()

chatbox = tkinter.Tk()
chatbox.title('Talking2U')

#welcome = tkinter.Toplevel(chatbox)

messages_frame = tkinter.Frame()
message = tkinter.StringVar()
message.set("")

scrollbar = tkinter.Scrollbar(messages_frame)

message_list = tkinter.Listbox(messages_frame, height = 15, width = 50, yscrollcommand = scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(chatbox, textvariable=message)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(chatbox, text="Send", command=send)
send_button.pack()

chatbox.protocol("WM_DELETE_WINDOW", on_closing)

tkinter.mainloop()