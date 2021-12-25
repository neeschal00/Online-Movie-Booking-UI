"""The Admin Module that consists of all the classes and methods for admin's portion"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import re
import json
# from collegesampleuser import *
# from main_app import *
from sqdb.conditionalquery import *
from createregno import *
import main_app
from ttkthemes import ThemedTk
from PIL import Image,ImageTk
from tkinter import PhotoImage
import omdbapi

BACKGROUND = '#24262E' #Hash color code
foregroundpurple = '#b368c8'
foregroundgray = '#a4a9b4'
orgcolor = '#B28360'
darkgray = '#1D2021'
blued = '#1D2021'


TFONT = ('Bauhaus 93',28,'bold') #Title font
MFONT = ('Britannic Bold',14)
BFONT = ('Arial Rounded MT Bold',10) #Base Font

genres =['Comedy',
        'Horor',
        'Sci-fi',
        'Action',
        'Drama',
        'Romance',
        'Fantasy',
        'Superhero',
        'Adventure',
        'Crime',
        'Children',
        'Mystery',
        'Thriller',
        'Western',
        'Historical',
        'Satire']


date_list = getdates() #imported function to get dates of next 5 days
time_list = ['07:00-10:30','11:00-14:30','15:00-18:30','19:00-22:30']



class window(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.container = tk.Frame(self)
        self.container.pack(side='top',fill='both',expand=True)

        self.container.grid_rowconfigure(0,weight=1) #0 is minimal value and weight is priority i.e 1 for both
        self.container.grid_columnconfigure(0,weight=1)
        self.geometry('600x600+350+50')
        self.title('Online Movie Booking')
        self.configure(background=BACKGROUND)


        self.switch_frames(UpdateRemove)

    def switch_frames(self,class_name):

        new_frame = class_name(self.container,self)
        new_frame.grid(row=0,column=0,sticky='nsew')
        new_frame.tkraise() #raising each frame

class SignupA(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.For_admin = ForAdmin()

        self.controller = controller
        self.configure(background=BACKGROUND)
        tk.Label(self,text='Sign Up Admin',font=TFONT,bg=BACKGROUND,fg=foregroundgray).place(relx=0.5,rely=0.1,anchor='center')

        signLf = tk.LabelFrame(self,bg=BACKGROUND)
        signLf.place(relx=0.1,rely=0.2,x=45,anchor='nw')

        tk.Label(signLf,text='User-name',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        self.unameEntry = tk.Entry(signLf,font=BFONT)
        self.unameEntry.grid(row=0,column=1,padx=10,pady=10)

        tk.Label(signLf,text='First Name',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        self.nameEntry = tk.Entry(signLf,font=BFONT)
        self.nameEntry.grid(row=1,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Last Name',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        self.lnameEntry = tk.Entry(signLf,font=BFONT)
        self.lnameEntry.grid(row=2,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Mobile Number',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        self.numberEntry = tk.Entry(signLf,font=BFONT)
        self.numberEntry.grid(row=3,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Password',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        self.passwrdEntry = tk.Entry(signLf,show='*',font=BFONT)
        self.passwrdEntry.grid(row=4,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Confirm Password',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        self.conPaswrdEntry = tk.Entry(signLf,show='*',font=BFONT)
        self.conPaswrdEntry.grid(row=5,column=1,padx=10,pady=10)

        backbtn = tk.Button(self,text='Back',width=10,bg=BACKGROUND,fg=foregroundgray,command=lambda:controller.switch_frames(main_app.FrontPage))
        backbtn.place(relx=0.3,rely=0.62,x=80,y=80,anchor='center')

        resetbtn = tk.Button(self,text='Reset',width=10,bg=BACKGROUND,fg=foregroundgray,command=lambda:self.resetBtn())
        resetbtn.place(relx=0.2,rely=0.52,y=80,anchor='nw')

        signupbtn = tk.Button(self,text='Sign Up ',width=10,bg=BACKGROUND,fg=foregroundgray,command=lambda:self.finalcheck())
        signupbtn.place(relx=0.2,rely=0.52,x=210,y=80,anchor='nw')

    def resetBtn(self):
        self.nameEntry.delete(0,tk.END)
        self.lnameEntry.delete(0,tk.END)
        self.numberEntry.delete(0,tk.END)
        self.unameEntry.delete(0,tk.END)
        self.passwrdEntry.delete(0,tk.END)
        self.conPaswrdEntry.delete(0,tk.END)

    def checkentry(self):
        if (self.nameEntry.get() and self.lnameEntry.get() and self.numberEntry.get() and self.unameEntry.get() and self.passwrdEntry.get() and self.conPaswrdEntry.get()) == '':
            print('Every entries wasn\'t filled')
            tk.messagebox.showerror('Entry Error','All the entries must be filled')
        else:
            print('Done')
            return True

    def checkno(self):
        try:
            val = int(self.numberEntry.get())
            if len(self.numberEntry.get()) != 10:
                tk.messagebox.showwarning('Number Error','The number should be 10 characters long')
            else:
                print('come back to this chckno fun later')

        except ValueError:
            tk.messagebox.showwarning('Number Entry Error','The entry in Mobile Number should be numerical')

    def checkPasswrd(self):

        length_check = len(self.passwrdEntry.get()) > 8 #checking if the character is smaller
        digit_error = re.search(r"\d", self.passwrdEntry.get()) is None
        uppercase_error = re.search(r"[A-Z]", self.passwrdEntry.get()) is None
        lowercase_error = re.search(r"[a-z]", self.passwrdEntry.get()) is None
        symbol_error = re.search(r"[ !#@$%&'()*+,-./[\\\]^_`{|}~]", self.passwrdEntry.get()) is None
        password_ok = not (digit_error or uppercase_error or lowercase_error or symbol_error)
        if self.passwrdEntry.get() != self.conPaswrdEntry.get():
                tk.messagebox.showerror('Password Doesn\'t Match','The passwords don\'t match up')
        else:
            if (length_check and password_ok) != True:
                tk.messagebox.showwarning('Password Requirement not fulfilled','The password must be greater than 8 characters, consisting of Uppercase, Lowercase, Numeric digit and special character')
            else:
                print('done')
                return True

    def finalcheck(self):
        if self.checkentry() is True:
            self.checkno()

            if self.checkPasswrd() is True:
                try:
                    self.For_admin.enteradmindata(self.unameEntry.get(),self.nameEntry.get(),self.lnameEntry.get(),self.numberEntry.get(),self.conPaswrdEntry.get())
                    tk.messagebox.showinfo('Success','Your account has been set up')
                except Exception as e:
                    print(e)
                    tk.messagebox.showwarning('User-name Error','The username already exists in the system')
            else:
                print('You can\'t create if there is no password check')
        else:
            print('Entry error')


class SingnIn(tk.Frame):

    admin_name = None
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.For_admin = ForAdmin()

        self.controller = controller
        self.configure(background=BACKGROUND)
        tk.Label(self,text='Sign In Admin',font=TFONT,bg=BACKGROUND,fg=foregroundgray).place(relx=0.5,rely=0.1,anchor='center')
        signInLf = tk.LabelFrame(self,bg=BACKGROUND)
        signInLf.place(relx=0.2,rely=0.2,x=45,anchor='nw')

        tk.Label(signInLf,text='User-name',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        self.unameEntry = tk.Entry(signInLf,font=BFONT)
        self.unameEntry.grid(row=0,column=1,padx=10,pady=10)

        tk.Label(signInLf,text='Password',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        self.passwrdEntry = tk.Entry(signInLf,show='*',font=BFONT)
        self.passwrdEntry.grid(row=1,column=1,padx=10,pady=10)

        signinbtn = tk.Button(self,text='Sign In ',width=10,bg=BACKGROUND,fg=foregroundgray,command=lambda:self.checkCreds())
        signinbtn.place(relx=0.2,rely=0.4,x=240,anchor='nw')

        backbtn = tk.Button(self,text='Back',width=10,bg=BACKGROUND,fg=foregroundgray,command=lambda:self.controller.switch_frames(main_app.FrontPage))
        backbtn.place(relx=0.2,rely=0.4,x=60,anchor='nw')


    def checkCreds(self):
        credentials = (self.unameEntry.get(),self.passwrdEntry.get())
        if self.For_admin.check_Credentials(credentials) == []: #fetching all data and if it returns empty list no such name exists
            tk.messagebox.showerror('Login Error','Chcek User-name and Password')
        else:
            SingnIn.admin_name = self.unameEntry.get()
            tk.messagebox.showinfo('Login Confirmation','You\'ve Successfully Logged In')
            self.controller.switch_frames(AdminHpage)


class AdminHpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.For_admin = ForAdmin()
        admin_details = self.For_admin.getadmindata(SingnIn.admin_name)

        fullnameGen = lambda fn,ln : fn.title() + ' ' + ln.title() #Making the full name
        full_name = fullnameGen(admin_details[0][1],admin_details[0][2])

        self.controller = controller
        self.configure(background=BACKGROUND)
        tk.Label(self,text='Admin HomePage',font=TFONT,bg=BACKGROUND,fg=foregroundgray).place(relx=0.5,rely=0.1,anchor='center')
        tk.Label(self,text='Welcome '+full_name,font=MFONT,bg=BACKGROUND,fg=foregroundgray).place(relx=0.5,rely=0.18,anchor='center')

        lframe = tk.LabelFrame(self,bg=BACKGROUND)
        lframe.place(relx=0.5,rely=0.5,anchor='center')

        tk.Button(lframe,text='Check Registration',width=30,bg=BACKGROUND,fg=foregroundgray,command=lambda:controller.switch_frames(CheckReg)).grid(row=0,column=1,columnspan=2,padx=15,pady=15)
        tk.Button(lframe,text='Add movies',width=30,bg=BACKGROUND,fg=foregroundgray,command=lambda:controller.switch_frames(AddMovies)).grid(row=1,column=1,columnspan=2,padx=15,pady=15)
        tk.Button(lframe,text='Update movies',width=30,bg=BACKGROUND,fg=foregroundgray,command=lambda:controller.switch_frames(UpdateRemove)).grid(row=2,column=1,columnspan=2,padx=15,pady=15)
        tk.Button(lframe,text='View User Data',width=30,bg=BACKGROUND,fg=foregroundgray,command=lambda:controller.switch_frames(ViewUsers)).grid(row=3,column=1,columnspan=2,padx=15,pady=15)

        back_btn = tk.Button(self,text='Main Page',width=20,bg=BACKGROUND,fg=foregroundgray,command=lambda:controller.switch_frames(main_app.FrontPage))
        back_btn.place(relx=0.5,rely=0.9,anchor='center')



class CheckReg(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.For_admin = ForAdmin()
        self.controller = controller
        self.configure(background=BACKGROUND)
        style = ttk.Style(self)
        style.configure('ng.TButton',foreground=foregroundpurple,background=BACKGROUND)
        tk.Label(self,text='Check Registration',font=TFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=0,column=0,columnspan=5,ipadx=60,padx=60,pady=30)

        self.search_e = tk.ttk.Entry(self,width=30)
        self.search_e.grid(row=1,column=0,columnspan=2,padx=30,pady=5,sticky='w')

        search_btn = tk.Button(self,text='Search',bg=BACKGROUND,fg=foregroundgray,command=self.searchview)
        search_btn.grid(row=1,column=1,pady=5,padx=30,sticky='e')

        sort_com = tk.Label(self,text='Sort By',font=MFONT,bg=BACKGROUND,fg=foregroundgray)
        sort_com.grid(row=1,column=3,sticky='e')
        self.sortby = tk.ttk.Combobox(self,width=18,values=['Movie','Date','Time','Tickets','Price'])
        self.sortby.current(0)
        self.sortby.bind("<<ComboboxSelected>>",self.sorting)
        self.sortby.grid(row=1,column=4,sticky='w')
        homebtn=tk.Button(self,text='Home',bg=BACKGROUND,width=13,fg=foregroundgray,command=lambda: self.controller.switch_frames(AdminHpage))
        homebtn.grid(row=13,column=2,pady=30,sticky='e')

        self.regi_details = self.For_admin.bookeddetails()

    def searchview(self):
        if self.search_e.get() == '':
            tk.messagebox.showwarning('Entry Error','You must enter name to search')
        else:
            self.values = [self.regi_details[i] for i,v in enumerate(self.regi_details) if v[1].lower().startswith(self.search_e.get())]
            self.treeFrame = tk.ttk.Frame(self)
            self.treeFrame.grid(row=3,column=0,columnspan=5,rowspan=10,padx=30)
            self.style = tk.ttk.Style(self.treeFrame)
            self.style.theme_use("clam")
            self.style.configure("Treeview", background=BACKGROUND,foreground="white")
            self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
            self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Registration','Movie','Date','Time','Tickets','Price'))
            self.treeViewF.grid(row=0,column=0,columnspan=4)
            # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
            self.treeViewF['show'] = 'headings'

            self.treeViewF.column('Registration',width=120,anchor='center')
            self.treeViewF.column('Movie',width=130,anchor='center')
            self.treeViewF.column('Date',width=80,anchor='center')
            self.treeViewF.column('Time',width=80,anchor='center')
            self.treeViewF.column('Tickets',width=50,anchor='center')
            self.treeViewF.column('Price',width=50,anchor='center')

            self.treeViewF.heading('Registration',text='Registration')
            self.treeViewF.heading('Movie',text='Movie')
            self.treeViewF.heading('Date',text='Date')
            self.treeViewF.heading('Time',text='Time')
            self.treeViewF.heading('Tickets',text='Tickets')
            self.treeViewF.heading('Price',text='Price')
            self.tree = self.treeViewF

            for values in self.values:
                self.tree.insert('', 'end', text='', value=values)

            self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,takefocus=True,command=self.treeViewF.yview)
            self.treeViewF.configure(yscrollcommand=self.scroll.set)
            self.scroll.grid(row=0,column=6,sticky='ns')



    def movienview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=3,column=0,columnspan=5,rowspan=10,padx=30)
        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])

        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Registration','Movie','Date','Time','Tickets','Price'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('Registration',width=120,anchor='center')
        self.treeViewF.column('Movie',width=130,anchor='center')
        self.treeViewF.column('Date',width=80,anchor='center')
        self.treeViewF.column('Time',width=80,anchor='center')
        self.treeViewF.column('Tickets',width=50,anchor='center')
        self.treeViewF.column('Price',width=50,anchor='center')

        self.treeViewF.heading('Registration',text='Registration')
        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Date',text='Date')
        self.treeViewF.heading('Time',text='Time')
        self.treeViewF.heading('Tickets',text='Tickets')
        self.treeViewF.heading('Price',text='Price')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbymovie():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values #Sorting data
            sort_key = lambda name: name[1]
            data.sort(key=sort_key,reverse=False)
            for values in data:
                self.tree.insert('','end',text='',value=values)


        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,takefocus=True,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def datenview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=3,column=0,columnspan=5,rowspan=10,padx=30)

        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")

        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Registration','Movie','Date','Time','Tickets','Price'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('Registration',width=120,anchor='center')
        self.treeViewF.column('Movie',width=130,anchor='center')
        self.treeViewF.column('Date',width=80,anchor='center')
        self.treeViewF.column('Time',width=80,anchor='center')
        self.treeViewF.column('Tickets',width=50,anchor='center')
        self.treeViewF.column('Price',width=50,anchor='center')

        self.treeViewF.heading('Registration',text='Registration')
        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Date',text='Date')
        self.treeViewF.heading('Time',text='Time')
        self.treeViewF.heading('Tickets',text='Tickets')
        self.treeViewF.heading('Price',text='Price')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbydate():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values #Sorting data
            sort_key = lambda name: name[2]
            data.sort(key=sort_key,reverse=False)
            for values in data:
                self.tree.insert('','end',text='',value=values)

        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def timenview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=3,column=0,columnspan=5,rowspan=10,padx=30)

        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Registration','Movie','Date','Time','Tickets','Price'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('Registration',width=120,anchor='center')
        self.treeViewF.column('Movie',width=130,anchor='center')
        self.treeViewF.column('Date',width=80,anchor='center')
        self.treeViewF.column('Time',width=80,anchor='center')
        self.treeViewF.column('Tickets',width=50,anchor='center')
        self.treeViewF.column('Price',width=50,anchor='center')

        self.treeViewF.heading('Registration',text='Registration')
        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Date',text='Date')
        self.treeViewF.heading('Time',text='Time')
        self.treeViewF.heading('Tickets',text='Tickets')
        self.treeViewF.heading('Price',text='Price')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbytime():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values #Sorting data
            sort_key = lambda name: name[3]
            data.sort(key=sort_key,reverse=False)
            for values in data:
                self.tree.insert('','end',text='',value=values)

        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def ticketnview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=3,column=0,columnspan=5,rowspan=10,padx=30)

        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Registration','Movie','Date','Time','Tickets','Price'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('Registration',width=120,anchor='center')
        self.treeViewF.column('Movie',width=130,anchor='center')
        self.treeViewF.column('Date',width=80,anchor='center')
        self.treeViewF.column('Time',width=80,anchor='center')
        self.treeViewF.column('Tickets',width=50,anchor='center')
        self.treeViewF.column('Price',width=50,anchor='center')

        self.treeViewF.heading('Registration',text='Registration')
        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Date',text='Date')
        self.treeViewF.heading('Time',text='Time')
        self.treeViewF.heading('Tickets',text='Tickets')
        self.treeViewF.heading('Price',text='Price')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbytickets():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values #Sorting data
            sort_key = lambda name: name[4]
            data.sort(key=sort_key,reverse=False)
            for values in data:
                self.tree.insert('','end',text='',value=values)


        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def pricenview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=3,column=0,columnspan=5,rowspan=10,padx=30)

        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Registration','Movie','Date','Time','Tickets','Price'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)

        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'


        self.treeViewF.column('Registration',width=120,anchor='w')
        self.treeViewF.column('Movie',width=130,anchor='center')
        self.treeViewF.column('Date',width=80,anchor='center')
        self.treeViewF.column('Time',width=80,anchor='center')
        self.treeViewF.column('Tickets',width=50,anchor='center')
        self.treeViewF.column('Price',width=50,anchor='center')

        self.treeViewF.heading('Registration',text='Registration')
        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Date',text='Date')
        self.treeViewF.heading('Time',text='Time')
        self.treeViewF.heading('Tickets',text='Tickets')
        self.treeViewF.heading('Price',text='Price')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbyprice():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values #Sorting data
            sort_key = lambda name: name[5]
            data.sort(key=sort_key,reverse=False)
            for values in data:
                self.tree.insert('','end',text='',value=values)


        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def sorting(self,event):
        if self.sortby.get() == 'Movie':
            self.movienview()
        elif self.sortby.get() == 'Date':
            self.datenview()
        elif self.sortby.get() == 'Time':
            self.timenview()
        elif self.sortby.get() == 'Tickets':
            self.ticketnview()
        elif self.sortby.get() == 'Price':
            self.pricenview()


class AddMovies(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.For_admin = ForAdmin()

        self.controller = controller
        self.configure(background=BACKGROUND)
        title_l = tk.Label(self,text='Add Movie',font=TFONT,background=BACKGROUND,foreground='white')
        title_l.grid(row=0,column=0,columnspan=5,ipadx=90,padx=90,pady=30)




        lf = tk.LabelFrame(self,background=BACKGROUND)
        lf.grid(row=1,column=0,columnspan=5,padx=100,pady=20)

        nameM = tk.Label(lf,text='Movie Name',font=BFONT,background=BACKGROUND,foreground=foregroundgray)
        nameM.grid(row=1,column=0,padx=10,pady=10)

        self.namEntry = tk.Entry(lf,font=BFONT)
        self.namEntry.grid(row=1,column=1,padx=10,pady=10)

        genreM = tk.Label(lf,text='Genre',font=BFONT,background=BACKGROUND,foreground=foregroundgray)
        genreM.grid(row=2,column=0,padx=10,pady=10)

        self.genCombo = tk.ttk.Combobox(lf,values=genres)
        self.genCombo.grid(row=2,column=1,padx=10,pady=10)

        dates_av = tk.Label(lf,text='Dates',font=BFONT,background=BACKGROUND,foreground=foregroundgray)
        dates_av.grid(row=3,column=0,padx=10,pady=10)

        self.datebox = tk.Listbox(lf,selectmode=tk.MULTIPLE,bg=BACKGROUND,fg=foregroundgray,height=6,width=20)
        self.datebox.grid(row=3,column=1,padx=10,pady=10)

        for dates in date_list:
            self.datebox.insert(tk.END,dates)


        addBtn = tk.Button(self,text='Add Movie',width=20,bg=BACKGROUND,fg='white',command=lambda:self.addButton())
        addBtn.grid(row=2,column=1,padx=20,pady=20)

        resetBtn = tk.Button(self,text='Reset',width=20,bg=BACKGROUND,fg='white',command=lambda:self.resetButton())
        resetBtn.grid(row=2,column=0,padx=90,pady=20)

        homebtn = tk.Button(self,text='Home',bg=BACKGROUND,width=20,fg='white',command=lambda:self.controller.switch_frames(AdminHpage))
        homebtn.place(relx=0.5,rely=0.75,anchor='center')

    def resetButton(self):
        self.namEntry.delete(0,tk.END)
        self.genCombo.delete(0,tk.END)
        # self.dateCombo.delete(0,tk.END)
        # self.timCombo.delete(0,tk.END)


    def addButton(self):
        # if (self.namEntry.get() and self.genCombo.get() and self.dateCombo.get() and self.timCombo.get()) == '':
        if (self.namEntry.get() and self.genCombo.get() and self.datebox.get(tk.ACTIVE)) == '':
            print('entry error')
            tk.messagebox.showwarning('Entries Incomplete','Fill all the Entries')
        else:
            try:
                json_data = {'Dates':[self.datebox.get(i) for i in self.datebox.curselection()]}
                date_available = json.dumps(json_data)

                self.For_admin.addMovies(self.namEntry.get(),self.genCombo.get(),date_available)
                # self.For_admin.addMovies(self.namEntry.get(),self.genCombo.get(),self.dateCombo.get(),self.timCombo.get())
                tk.messagebox.showinfo('Success','Movie was successfully added')
                omdbapi.imagedownload(self.namEntry.get())

            except Exception as e:
                print(e)
                tk.messagebox.showerror('Duplicate Entry','The Movie name has already been added to the database')



class UpdateRemove(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.For_admin = ForAdmin()
        self.controller = controller
        self.configure(background=BACKGROUND)
        title_label = tk.Label(self,text='Update/Remove Movie',font=TFONT,bg=BACKGROUND,fg=foregroundgray)
        title_label.grid(row=0,column=0,ipadx=10,padx=90,pady=30,columnspan=5)

        tk.Label(self,text='Movie Name',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=1,column=0,ipadx=20,padx=20,pady=5,sticky='e')

        self.movienEntry = tk.Entry(self,font=BFONT,width=19)
        self.movienEntry.grid(row=1,column=1,padx=5,pady=5,sticky='w')

        gobtn = tk.Button(self,text='Go',width=10,bg=BACKGROUND,fg=foregroundgray,command=lambda:self.searchbtn())
        gobtn.grid(row=1,column=2,padx=5,pady=5)
        homebtn = tk.Button(self,text='Home',bg=BACKGROUND,width=20,fg=foregroundgray,command=lambda: self.controller.switch_frames(AdminHpage))
        homebtn.grid(row=6,column=1,padx=15,pady=30,sticky='w')



    def afterSearch(self):
        if self.movienEntry.get() == '':
            tk.messagebox.showwarning('No Entry','You Must enter the Full Movie Name')
        else:



            lf = tk.LabelFrame(self,background=BACKGROUND)
            lf.grid(row=2,column=0,columnspan=4,padx=10,pady=10)

            genreM = tk.Label(lf,text='Genre',font=BFONT,background=BACKGROUND,foreground=foregroundgray)
            genreM.grid(row=2,column=0,padx=5,pady=5)

            self.genCombo = tk.ttk.Combobox(lf,values=genres)
            self.genCombo.grid(row=2,column=1,padx=5,pady=5)

            dates_av = tk.Label(lf,text='Dates',font=BFONT,background=BACKGROUND,foreground=foregroundgray)
            dates_av.grid(row=3,column=0,padx=10,pady=10)

            self.datebox = tk.Listbox(lf,selectmode=tk.MULTIPLE,bg=BACKGROUND,fg=foregroundgray,height=7,width=10)
            self.datebox.grid(row=3,column=1,padx=10,pady=10)

            for dates in date_list:
                self.datebox.insert(tk.END,dates)

            addBtn = tk.Button(self,text='Update Movie',width=20,bg=BACKGROUND,fg=foregroundgray,command=self.updatemovie)
            addBtn.grid(row=3,column=2,padx=5,pady=5,sticky='w')

            resetBtn = tk.Button(self,text='Delete Movie',width=20,bg=BACKGROUND,fg=foregroundgray,command=self.deletemovie)
            resetBtn.grid(row=3,column=0,padx=45,pady=5,sticky='e')

            # backbtn = tk.Button(self,text='Home',width=20,bg=BACKGROUND,fg='white',command=lambda:self.controller.switch_frames(AdminHpage))
            # backbtn.grid(row=4,column=1,padx=5,pady=15)
            return True


    def addvalues(self):
        data = self.For_admin.searchadd(self.movienEntry.get())
        if data != []:
            self.movienEntry.delete(0,tk.END)
            self.movienEntry.insert(0,data[0][0])

            self.genCombo.delete(0,tk.END)
            self.genCombo.insert(0,data[0][1])

        else:
            tk.messagebox.showerror('Name Error','Movie Name doesn\'t exist')

    def searchbtn(self):
        if self.afterSearch() is True:
            self.addvalues()

    def deletemovie(self):
        if self.movienEntry.get() == '':
            tk.messagebox.showwarning('Entry Error','You must enter the movie name')
        else:
            self.For_admin.deletemovie(self.movienEntry.get())
            self.movienEntry.delete(0,tk.END)
            self.genCombo.delete(0,tk.END)
            tk.messagebox.showinfo('Completed','Movie Successfully Deleted')

    def updatemovie(self):
        # if (self.movienEntry.get() and self.genCombo.get() and self.dateCombo.get() and self.timCombo.get()) == '':
        if (self.movienEntry.get() and self.genCombo.get()) == '':
            print('entry error')
            tk.messagebox.showwarning('Entries Incomplete','Fill all the Entries')
        else:
            try:
                json_data = {'Dates':[self.datebox.get(i) for i in self.datebox.curselection()]}
                date_available = json.dumps(json_data)

                # self.For_admin.updateaddition(self.movienEntry.get(),self.genCombo.get(),self.dateCombo.get(),self.timCombo.get())
                self.For_admin.updateaddition(self.movienEntry.get(),self.genCombo.get(),date_available)
                tk.messagebox.showinfo('Success','Movie was successfully Updated')
            except:
                tk.messagebox.showerror('Unknow Error','Value Mismatch Name not found')


class ViewUsers(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.For_admin = ForAdmin()
        self.controller = controller
        self.configure(background=BACKGROUND)

        title_l = tk.Label(self,text='View Users',font=TFONT,bg=BACKGROUND,fg=foregroundgray)
        title_l.grid(row=0,column=0,ipadx=100,padx=90,pady=30,columnspan=5)

        self.search_e = tk.ttk.Entry(self,width=30)
        self.search_e.grid(row=1,column=0,columnspan=2,padx=30,pady=5,sticky='w')

        search_btn = tk.Button(self,text='Search',bg=BACKGROUND,fg=foregroundgray,command=self.searchusers)
        search_btn.grid(row=1,column=1,pady=5,padx=30,sticky='e')

        sort_com = tk.Label(self,text='Sort By',font=MFONT,bg=BACKGROUND,fg=foregroundgray)
        sort_com.grid(row=1,column=3,sticky='e')

        # tk.Label(self,text='Sort By',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=1,column=0,padx=50,pady=5,sticky='w')
        self.sortby = tk.ttk.Combobox(self,width=18,values=['User-name','First-Name','Last-Name','Mobile'])
        self.sortby.current(0)
        self.sortby.bind("<<ComboboxSelected>>",self.sorting)
        self.sortby.grid(row=1,column=4,padx=10,pady=5)
        homebt = tk.Button(self,text='Home',bg=BACKGROUND,width=20,fg='white',command=lambda: self.controller.switch_frames(AdminHpage))
        homebt.place(relx=0.5,rely=0.8,anchor=tk.CENTER)

        self.regi_details = self.For_admin.getusers()

    def searchusers(self):
        if self.search_e.get() == '':
            tk.messagebox.showwarning('Entry Error','You must enter name to search')
        else:
            self.values = [self.regi_details[i] for i,v in enumerate(self.regi_details) if v[1].lower().startswith(self.search_e.get())]
            self.treeFrame = tk.ttk.Frame(self,style='TFrame')
            self.treeFrame.grid(row=2,column=0,columnspan=5,rowspan=10,padx=30)



            self.style = tk.ttk.Style(self.treeFrame)
            self.style.theme_use("clam")


            self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground=foregroundgray)
            self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
            self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('User-name','First-Name','Last-Name','Mobile'))
            self.treeViewF.grid(row=0,column=0,columnspan=4)
            # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
            self.treeViewF['show'] = 'headings'

            self.treeViewF.column('User-name',width=150,anchor='center')
            self.treeViewF.column('First-Name',width=120,anchor='center')
            self.treeViewF.column('Last-Name',width=120,anchor='center')
            self.treeViewF.column('Mobile',width=120,anchor='center')


            self.treeViewF.heading('User-name',text='User-name')
            self.treeViewF.heading('First-Name',text='First-Name')
            self.treeViewF.heading('Last-Name',text='Last-Name')
            self.treeViewF.heading('Mobile',text='Mobile')
            self.tree = self.treeViewF

            for values in self.values:
                self.tree.insert('', 'end', text='', value=values)

            self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
            self.treeViewF.configure(yscrollcommand=self.scroll.set)
            self.scroll.grid(row=0,column=6,sticky='ns')


    def unameview(self):
        self.treeFrame = tk.ttk.Frame(self,style='TFrame')
        self.treeFrame.grid(row=2,column=0,columnspan=5,rowspan=10,padx=30)



        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")


        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground=foregroundgray)
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('User-name','First-Name','Last-Name','Mobile'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('User-name',width=150,anchor='center')
        self.treeViewF.column('First-Name',width=120,anchor='center')
        self.treeViewF.column('Last-Name',width=120,anchor='center')
        self.treeViewF.column('Mobile',width=120,anchor='center')


        self.treeViewF.heading('User-name',text='User-name')
        self.treeViewF.heading('First-Name',text='First-Name')
        self.treeViewF.heading('Last-Name',text='Last-Name')
        self.treeViewF.heading('Mobile',text='Mobile')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbyuname():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values
            sort_key = lambda name : name[0]
            data.sort(key=sort_key)
            for values in data:
                self.tree.insert('', 'end', text='', value=values)


        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def fnameview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=2,column=0,columnspan=5,rowspan=10,padx=30)



        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")


        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('User-name','First-Name','Last-Name','Mobile'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('User-name',width=150,anchor='center')
        self.treeViewF.column('First-Name',width=120,anchor='center')
        self.treeViewF.column('Last-Name',width=120,anchor='center')
        self.treeViewF.column('Mobile',width=120,anchor='center')


        self.treeViewF.heading('User-name',text='User-name')
        self.treeViewF.heading('First-Name',text='First-Name')
        self.treeViewF.heading('Last-Name',text='Last-Name')
        self.treeViewF.heading('Mobile',text='Mobile')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbyfname():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values
            sort_key = lambda name : name[1]
            data.sort(key=sort_key)
            for values in data:
                self.tree.insert('', 'end', text='', value=values)


        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def lnameview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=2,column=0,columnspan=5,rowspan=10,padx=30)



        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")


        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('User-name','First-Name','Last-Name','Mobile'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('User-name',width=150,anchor='center')
        self.treeViewF.column('First-Name',width=120,anchor='center')
        self.treeViewF.column('Last-Name',width=120,anchor='center')
        self.treeViewF.column('Mobile',width=120,anchor='center')


        self.treeViewF.heading('User-name',text='User-name')
        self.treeViewF.heading('First-Name',text='First-Name')
        self.treeViewF.heading('Last-Name',text='Last-Name')
        self.treeViewF.heading('Mobile',text='Mobile')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbylname():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values
            sort_key = lambda name : name[2]
            data.sort(key=sort_key)
            for values in data:
                self.tree.insert('', 'end', text='', value=values)

        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def mobileview(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=2,column=0,columnspan=5,rowspan=10,padx=30)



        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")


        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])
        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('User-name','First-Name','Last-Name','Mobile'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)
        # self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('User-name',width=150,anchor='center')
        self.treeViewF.column('First-Name',width=120,anchor='center')
        self.treeViewF.column('Last-Name',width=120,anchor='center')
        self.treeViewF.column('Mobile',width=120,anchor='center')


        self.treeViewF.heading('User-name',text='User-name')
        self.treeViewF.heading('First-Name',text='First-Name')
        self.treeViewF.heading('Last-Name',text='Last-Name')
        self.treeViewF.heading('Mobile',text='Mobile')
        self.tree = self.treeViewF

        if self.search_e.get() == '':
            for values in self.For_admin.orderbymobile():
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = self.values
            sort_key = lambda name : name[3]
            data.sort(key=sort_key)
            for values in data:
                self.tree.insert('', 'end', text='', value=values)

        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=6,sticky='ns')

    def sorting(self,event):
        if self.sortby.get() == 'User-name':
            self.unameview()
        elif self.sortby.get() == 'First-Name':
            self.fnameview()
        elif self.sortby.get() == 'Last-Name':
            self.lnameview()
        elif self.sortby.get() == 'Mobile':
            self.mobileview()



if __name__ == '__main__':
    app = window()
    app.mainloop()
