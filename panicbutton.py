import tkinter as tk
from tkinter import messagebox
x = 0  
def panic():
    messagebox.showinfo('panic room','crisis averted!!!')
    global x
    x+=1
    var.set(x)
root = tk.Tk()
b = tk.Button(root,text='panic button',command=panic)
b.pack()
var = tk.StringVar()
var.set(x)
label2 = tk.Label(root,text = 'no of times panic button pressed : \n')
label2.pack()
label = tk.Message(root,textvariable=var)
label.pack()
root.mainloop()
