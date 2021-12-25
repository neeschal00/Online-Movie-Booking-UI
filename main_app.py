""" This is the main module that links both user and admin module to run the app"""


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import re
import user_m
from admin_m import *

from omdbapi import *

from PIL import Image,ImageTk

# import user_m
BACKGROUND = '#24262E' #Hash color code
foregroundpurple = '#b368c8'
foregrounndgray = '#a4a9b4'
orgcolor = '#B28360'
darkgray = '#1D2021'
blued = '#1D2021'


TFONT = ('Bauhaus 93',28,'bold') #Title font
MFONT = ('Britannic Bold',14)
BFONT = ('Arial Rounded MT Bold',10) #Base Font



class window(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.container = tk.Frame(self)
        self.container.pack(side='top',fill='both',expand=True)
        self.resizable(width=False,height=False)

        self.container.grid_rowconfigure(0,weight=1) #0 is minimal value and weight is priority i.e 1 for both
        self.container.grid_columnconfigure(0,weight=1)
        self.geometry('600x600+350+50')
        self.title('Online Movie Booking')
        self.configure(background=BACKGROUND)

        self.switch_frames(FrontPage)

    def switch_frames(self,class_name):

        new_frame = class_name(self.container,self)
        new_frame.grid(row=0,column=0,sticky='nsew')
        new_frame.tkraise() #raising each frame


class FrontPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.configure(background=BACKGROUND)

        # image_l = tk.Label(self,)


        bgimg = Image.open('cinemahall.jpg')
        width,height = 600,600

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        pil_img = Image.open('cinema.jpg')
        self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        tk.Label(self,text='BOOK MOVIE ONLINE',bg='#080705',fg=foregroundpurple,font=TFONT).place(relx=0.5,rely=0.15,anchor='center')
        lf = tk.LabelFrame(self,bg='black',text='Admin',fg=foregroundpurple)
        lf.place(relx=0.1,rely=0.3,y=50,anchor='nw')

        loginA = tk.Button(lf,text='Sign In',bg=BACKGROUND,fg=foregroundpurple,width=20,font=('Georgia',10),command=lambda:controller.switch_frames(SingnIn))
        loginA.grid(row=0,column=0,padx=10,pady=10)
        registerA = tk.Button(lf,text='Sign Up',bg=BACKGROUND,fg=foregroundpurple,width=20,font=('Georgia',10),command=lambda:self.checking()).grid(row=1,column=0,padx=10,pady=10)

        lfU = tk.LabelFrame(self,bg='#080705',text='Customer',fg=foregroundpurple)
        lfU.place(relx=0.5,rely=0.3,y=50,anchor='nw')

        loginU = tk.Button(lfU,text='Sign In',bg=BACKGROUND,fg=foregroundpurple,width=20,font=('Georgia',10),command=lambda:controller.switch_frames(user_m.SingnInU))
        loginU.grid(row=0,column=0,padx=10,pady=10)
        registerU = tk.Button(lfU,text='Sign Up',bg=BACKGROUND,fg=foregroundpurple,width=20,font=('Georgia',10),command=lambda:controller.switch_frames(user_m.BackUser))
        registerU.grid(row=1,column=0,padx=10,pady=10)


        # tk.Button(self,text='nextpage',width=40,command=lambda:self.checking()).grid(row=1,column=1)
    def checking(self):
        print('checking')
        self.controller.switch_frames(SignupA)




if __name__ == '__main__':
    app = window()
    app.mainloop()
























