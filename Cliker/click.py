from tkinter import *

tk = Tk()
tk.title('Clicker')

btn = Button(text='Click Me', width=10, height=10)
btn = Button(text='Click Me', width=10, height=10)
btn.pack()

n = 0 # переменная для счетчика
def nplus(event):
    global n
    n = n + 1 # добавляем 1 к переменной n
    label['text'] = str(n)

btn.bind('<Button-1>', nplus)

label = Label(tk, text=str(n), font ='Helvetica')
label.pack()

tk.mainloop()