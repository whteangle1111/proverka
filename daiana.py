import tkinter
from tkinter import *
from tkinter import messagebox
def start_up():
    import json
    with open('users.json',"r",encoding="utf-8") as f:
        data = json.load(f)
        return data
def func():
    user = entry.get()
    pas = entry1.get()
    if(user in data['users'].keys() and pas == data['users'][user]):
        return messagebox.showinfo("УВЕДОМЛЕНИЕ","УСПЕШНЫЙ ВХОД")
    else:
        return messagebox.showerror("УВЕДОМЛЕНИЕ","ТАКОГО ПОЛЬЗОВАТЕЛЯ НЕ СУЩЕСТВУЕТ")

data = start_up()
window = Tk()
window.geometry('300x110')
label=Label(text='ЛОГИН:')
label.pack()
entry=Entry()
entry.pack()
label1=Label(text='ПАРОЛЬ:')
label1.pack()
entry1=Entry()
entry1.pack()
button = Button(text='ВОЙТИ',command=func).pack()



window.mainloop()
