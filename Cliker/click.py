from tkinter import *

tk = Tk()
tk.title('Clicker')

btn = Button(text='Click Me', width=30, height=20)

btn.pack()

n = 0 # переменная для счетчика
x = 0
def nplus(event):
    global n
    global x
    n = n + 1 # добавляем 1 к переменной n
    x = x + 1
    label['text'] = str(n)


btn.bind('<Button-1>', nplus)

label = Label(tk, text=str(n),  font ='Helvetica')
label.pack()

tk.mainloop()