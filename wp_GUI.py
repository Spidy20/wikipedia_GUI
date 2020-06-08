from PIL import ImageTk
import PIL.Image
from tkinter import *
import tkinter as tk
import wikipedia
import subprocess
import clipboard

windo = Tk()
windo.configure(background='white')
windo.title("Wikipedia App")
# width  = windo.winfo_screenwidth()
# height = windo.winfo_screenheight()
# windo.geometry(f'{width}x{height}')
windo.geometry('1120x820')
windo.iconbitmap('./meta/icon.ico')
windo.resizable(0,0)

def copy_text():
    clipboard.copy(result)
    lab1 = tk.Label(windo, text="Text copied to Clipboard!", width=20, height=1, fg="black", bg="gold",
                   font=('times', 16, ' bold '))
    lab1.place(x=720, y=605)
    windo.after(5000, destroy_widget,lab1 )

def clear():
    txt2.delete(first=0,last=100)
    T.destroy()
    FA.destroy()
    FA1.destroy()


def search():
    try:
        global result,T,FA,FA1
        query = txt2.get()
        result = wikipedia.summary(query)
        T = tk.Text(windo, borderwidth=7, height=14, width=57, font=('times', 16))
        T.place(x=430, y=250)
        T.configure(state='normal')
        T.insert(tk.END, result)
        T.configure(state='disabled')

        FA = tk.Button(windo, text="Copy Text",command = copy_text, fg="white", bg="blue2", font=('times', 15, ' bold '))
        FA.place(x=430, y=600)

        FA1 = tk.Button(windo, text="Clear",command = clear, fg="white", bg="red", font=('times', 15, ' bold '))
        FA1.place(x=550, y=600)
    except Exception as e:
        lab2 = tk.Label(windo, text="Something went wrong!", width=20, height=1, fg="white", bg="red",
                        font=('times', 16, ' bold '))
        lab2.place(x=720, y=605)
        windo.after(5000, destroy_widget, lab2)

def destroy_widget(widget):
    widget.destroy()

im = PIL.Image.open('./meta/wp.png')
im =im.resize((351,263), PIL.Image.ANTIALIAS)
wp_img = ImageTk.PhotoImage(im)
panel4 = Label(windo, image=wp_img,bg = 'white')
panel4.pack()
panel4.place(x=20, y=100)

im1 = PIL.Image.open('./meta/search.png')
im1 =im1.resize((70,70), PIL.Image.ANTIALIAS)
sp_img = ImageTk.PhotoImage(im1)
panel5 = Button(windo,borderwidth=0,command = search, image=sp_img,bg = 'white')
panel5.pack()
panel5.place(x=920, y=165)

pred = tk.Label(windo, text="Wikipedia App", width=30, height=2, fg="white",bg="black",
                font=('times', 25, ' bold '))
pred.place(x=274, y=10)

lab = tk.Label(windo, text="Enter your Keyword", width=18, height=1, fg="white",bg="blue2",
                font=('times', 16, ' bold '))
lab.place(x=544, y=120)

txt2 = tk.Entry(windo,borderwidth = 7, width=26, bg="white", fg="black", font=('times', 25, ' bold '))
txt2.place(x=430, y=170)

windo.mainloop()