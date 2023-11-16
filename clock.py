#https://python.plainenglish.io/make-a-digital-clock-using-python-and-tkinter-a463aa8c19e1
# pip install tk (install tkinter package)
from tkinter import *
from time import strftime
root = Tk()
root.geometry("1000x400")
root.resizable(2,4)
root.title('Clock')
Label(root,text = 'Clock and Date', font ='arial 20 bold').pack(side=TOP)
def time():
    today_now = strftime('NaN')

    string = strftime('%h %d, %Y')
    mark.config(text = string)
    mark.after(1000, time)

def today_time():
    today_time = strftime('%I:%M:%S %p')
    mark.config(text = today_time)
    mark.after(1000, time)

mark = Label(root, 
            font = ('calibri', 60, 'bold'),
            pady=100,
            foreground = 'blue')
mark.pack(anchor = 'center')

time()

today_time()
 
mainloop()