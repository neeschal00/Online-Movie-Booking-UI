""" The User module That consists of all the classes and methods used and ran in the User's Part"""

import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox
import main_app
# from collegeadmin import *
from sqdb.conditionalquery import *
from createregno import *
from omdbapi import *
import webbrowser

from PIL import ImageTk,Image
import os

BACKGROUND = '#24262E' #Hash color code
foregroundpurple = '#b368c8'
foregroundgray = '#a4a9b4'
orgcolor = '#B28360'
darkgray = '#1D2021'
blued = '#7096EE'


TFONT = ('Bauhaus 93',28,'bold') #Title font
MFONT = ('Britannic Bold',14)
BFONT = ('Arial Rounded MT Bold',10) #Base Font

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

        self.switch_frames(BookMovie)

    def switch_frames(self,class_name):

        new_frame = class_name(self.container,self)
        new_frame.grid(row=0,column=0,sticky='nsew')
        new_frame.tkraise() #raising each frame

class BackUser(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.configure(background=BACKGROUND)

        self.For_user = ForUser()


        tk.Label(self,text='Sign Up User',font=TFONT,bg=BACKGROUND,fg=foregroundpurple).place(relx=0.5,rely=0.1,anchor='center')

        signLf = tk.LabelFrame(self,bg=BACKGROUND)
        signLf.place(relx=0.1,rely=0.2,x=45,anchor='nw')

        tk.Label(signLf,text='User-name',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        self.unameEntry = tk.Entry(signLf,font=BFONT)
        self.unameEntry.grid(row=0,column=1,padx=10,pady=10)

        tk.Label(signLf,text='First Name',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        self.nameEntry = tk.Entry(signLf,font=BFONT)
        self.nameEntry.grid(row=1,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Last Name',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        self.lnameEntry = tk.Entry(signLf,font=BFONT)
        self.lnameEntry.grid(row=2,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Mobile Number',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        self.numberEntry = tk.Entry(signLf,font=BFONT)
        self.numberEntry.grid(row=3,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Password',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        self.passwrdEntry = tk.Entry(signLf,show='*',font=BFONT)
        self.passwrdEntry.grid(row=4,column=1,padx=10,pady=10)

        tk.Label(signLf,text='Confirm Password',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        self.conPaswrdEntry = tk.Entry(signLf,show='*',font=BFONT)
        self.conPaswrdEntry.grid(row=5,column=1,padx=10,pady=10)

        backbtn = tk.Button(self,text='Back',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:controller.switch_frames(main_app.FrontPage))
        backbtn.place(relx=0.3,rely=0.62,x=80,y=80,anchor='center')

        resetbtn = tk.Button(self,text='Reset',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.resetBtn())
        resetbtn.place(relx=0.2,rely=0.52,y=80,anchor='nw')

        signupbtn = tk.Button(self,text='Sign Up ',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.finalcheck())
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
            False
        else:
            print('Done')
            return True

    def checkno(self):
        try:
            val = int(self.numberEntry.get())
            if len(self.numberEntry.get()) != 10:
                tk.messagebox.showwarning('Number Error','The number should be 10 characters long')
                return False
            else:
                print('come back to this chckno fun later')
                return True

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
                    self.For_user.enteruserdata(self.unameEntry.get(),self.nameEntry.get(),self.lnameEntry.get(),self.numberEntry.get(),self.conPaswrdEntry.get())
                    tk.messagebox.showinfo('Success','Your account has been set up')
                except Exception as e:
                    print(e)
                    tk.messagebox.showwarning('User-name Error','The username already exists in the system')
            else:
                print('can\'t touch this')

class SingnInU(tk.Frame):
    username = None
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.For_user = ForUser() #creating object of the class

        self.controller = controller
        self.configure(background=BACKGROUND)
        tk.Label(self,text='Sign In User',font=TFONT,bg=BACKGROUND,fg=foregroundpurple).place(relx=0.5,rely=0.1,anchor='center')
        signInLf = tk.LabelFrame(self,bg=BACKGROUND)
        signInLf.place(relx=0.2,rely=0.2,x=45,anchor='nw')

        tk.Label(signInLf,text='User-name',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        self.unameEntry = tk.Entry(signInLf,font=BFONT)
        self.unameEntry.grid(row=0,column=1,padx=10,pady=10)

        tk.Label(signInLf,text='Password',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        self.passwrdEntry = tk.Entry(signInLf,show='*',font=BFONT)
        self.passwrdEntry.grid(row=1,column=1,padx=10,pady=10)

        signinbtn = tk.Button(self,text='Sign In ',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.checkCreds())
        signinbtn.place(relx=0.2,rely=0.4,x=240,anchor='nw')

        backbtn = tk.Button(self,text='Back',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.controller.switch_frames(main_app.FrontPage))
        backbtn.place(relx=0.2,rely=0.4,x=60,anchor='nw')

    def checkCreds(self):
        credentials = (self.unameEntry.get(),self.passwrdEntry.get())
        if self.For_user.check_Credentials(credentials) == []: #fetching all data and if it returns empty list no such name exists
            tk.messagebox.showerror('Login Error','Chcek User-name and Password')
        else:
            tk.messagebox.showinfo('Login Confirmation','You\'ve Successfully Logged In')
            SingnInU.username = self.unameEntry.get()
            self.controller.switch_frames(UserHpage)




class UserHpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.for_user = ForUser()
        self.userdetails = self.for_user.getuserdata(SingnInU.username)

        fullnameGen = lambda fn,ln : fn.title() + ' ' + ln.title() #Making the full name
        full_name = fullnameGen(self.userdetails[0][1],self.userdetails[0][2])

        self.configure(background=BACKGROUND)
        tk.Label(self,text='User HomePage',font=TFONT,bg=BACKGROUND,fg=foregroundpurple).place(relx=0.5,rely=0.1,anchor='center')
        tk.Label(self,text='Welcome '+full_name,font=MFONT,bg=BACKGROUND,fg=foregroundpurple).place(relx=0.5,rely=0.18,anchor='center')

        lframe = tk.LabelFrame(self,bg=BACKGROUND)
        lframe.place(relx=0.5,rely=0.5,anchor='center')


        tk.Button(lframe,text='Book Movies',width=30,bg=BACKGROUND,fg=foregroundpurple,command=lambda:controller.switch_frames(BookMovie)).grid(row=0,column=1,columnspan=2,padx=15,pady=15)
        tk.Button(lframe,text='Change Booking',width=30,bg=BACKGROUND,fg=foregroundpurple,command=lambda:controller.switch_frames(ChangeBooking)).grid(row=2,column=1,columnspan=2,padx=15,pady=15)
        tk.Button(lframe,text='View Movies',width=30,bg=BACKGROUND,fg=foregroundpurple,command=lambda:controller.switch_frames(ViewMoviesUser)).grid(row=3,column=1,columnspan=2,padx=15,pady=15)

        back_btn = tk.Button(self,text='Main Page',width=20,bg=BACKGROUND,fg=foregroundpurple,command=lambda:controller.switch_frames(main_app.FrontPage))
        back_btn.place(relx=0.5,rely=0.9,anchor='center')


class BookMovie(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.for_user = ForUser()
        movie_names = [name[0] for name in self.for_user.getmoviename()] #getting the list of available movies


        self.regiNum = generatereg() #getting the registration number with dt module

        self.controller = controller
        self.configure(background=BACKGROUND)
        tk.Label(self,text='Book Movies',font=TFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=0,column=0,columnspan=5,ipadx=90,padx=90,pady=20)

        lframe = tk.LabelFrame(self,bg=BACKGROUND)
        lframe.grid(row=1,column=0,columnspan=5,padx=90,pady=10)

        tk.Label(lframe,text='Movie',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=0,column=0,padx=10,pady=5,sticky='w')



        self.movieEntry = tk.ttk.Combobox(lframe,width=18,values=movie_names)
        self.movieEntry.bind("<<ComboboxSelected>>",self.moviedetails)
        self.movieEntry.grid(row=0,column=1,padx=10,pady=5)

        tk.Label(lframe,text='Date',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=1,column=0,padx=10,pady=5,sticky='w')
        self.dateEntry = tk.ttk.Combobox(lframe,width=15,values=date_list)
        self.dateEntry.grid(row=1,column=1,padx=10,pady=5)

        tk.Label(lframe,text='Time',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=2,column=0,padx=10,pady=5,sticky='w')
        self.timeEntry = tk.ttk.Combobox(lframe,width=15,values=time_list)
        self.timeEntry.grid(row=2,column=1,padx=10,pady=5)

        tk.Label(lframe,text='Tickets',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=3,column=0,padx=10,pady=5,sticky='w')
        self.ticketsEntry = tk.ttk.Combobox(lframe,width=5,font=BFONT,values=[1,2,3,4,5])
        self.ticketsEntry.grid(row=3,column=1,padx=10,pady=5)

        bookbtn = tk.Button(self,text='Book Movie',width=15,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.CompleteConfirmation())
        bookbtn.grid(row=2,column=2,padx=30,pady=25,sticky='w')
        homebtn = tk.Button(self,text='Home',width=15,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.controller.switch_frames(UserHpage))
        homebtn.grid(row=2,column=1,padx=40,pady=25,sticky='e')

    def moviedetails(self,event):
        availablelisting = self.for_user.getmoviedetails(self.movieEntry.get())
        print(availablelisting)
        date_data = json.loads(availablelisting[0][2])
        # print(date_data['Dates'])
        self.dateEntry.configure(values=date_data['Dates'])






    def showbill(self):

        self.totalprice = str(int(self.ticketsEntry.get())*100) #getting the total price of the tickets

        root = tk.Toplevel()
        root.configure(bg=BACKGROUND)
        root.geometry('600x600')

        try:
            try:
                width,height = 600,600

                self.canvas = tk.Canvas(root,bg=darkgray,width=width, height=height)
                self.canvas.pack()

                pil_img = Image.open(os.path.join(os.getcwd(),'movieposter',self.movieEntry.get()+'blur'+'.jpg'))
                self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
                self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
            except:
                print('Blur image not found')

            img_p = Image.open(os.path.join(os.getcwd(),'movieposter',self.movieEntry.get()+'.jpg'))
            img_var = ImageTk.PhotoImage(image=img_p)

            pimg = tk.Label(root, image=img_var,bg=BACKGROUND)
            pimg.configure(image=img_var)

            pimg.place(relx=0.5,rely=0.2,anchor='center')
        except:
            print('Image Couldn\'t be downloaded')

        newlframe = tk.LabelFrame(root,bg=darkgray)
        newlframe.place(relx=0.5,rely=0.7,anchor='center',width=310,height=300)

        tk.Label(newlframe,text='Movie Booked Successfully',font=BFONT,bg=darkgray,fg=blued).grid(row=0,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text='Registration No.: '+ self.regiNum,font=BFONT,bg=darkgray,fg=blued).grid(row=1,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text=self.movieEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=2,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text='Date: '+ self.dateEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=3,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text='Time: '+self.timeEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=4,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text='Tickets: '+self.ticketsEntry.get() ,font=BFONT,bg=darkgray,fg=blued).grid(row=5,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text='Total Price: NRS.'+ self.totalprice,font=BFONT,bg=darkgray,fg=blued).grid(row=6,column=0,padx=5,pady=5,sticky='ew')
        tk.Label(newlframe,text='Please don\'t forget Your Registration number',font=('Italic',5),bg=darkgray,fg=blued).grid(row=7,column=0,padx=10,pady=10,sticky='ew')
        tk.Button(newlframe,text='Exit',width=10,bg=darkgray,fg=blued,command=lambda:root.destroy()).grid(row=8,column=0,padx=5,pady=5)

        root.mainloop()


    def CompleteConfirmation(self):
        if (self.movieEntry.get() and self.dateEntry.get() and self.timeEntry.get() and self.ticketsEntry.get()) == '':
            tk.messagebox.showwarning('Entry error','Fill all the Entries')
        else:
            try:
                imagdownload(self.movieEntry.get())
            except:
                print('Couldn\'t connect')
            totalprice = str(int(self.ticketsEntry.get())*100)
            self.for_user.bookmovie(self.regiNum,self.movieEntry.get(),self.dateEntry.get(),self.timeEntry.get(),self.ticketsEntry.get(),totalprice)

            tk.messagebox.showinfo('Done','Movie Booked Successfully')
            blurimg(self.movieEntry.get())
            self.showbill()


class ChangeBooking(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.for_user = ForUser()
        self.movie_names = [name[0] for name in self.for_user.getmoviename()] #getting the list of available movies

        self.controller = controller
        self.configure(background=BACKGROUND)
        title_l = tk.Label(self,text='Update/Delete Bookings',font=TFONT,bg=BACKGROUND,fg=foregroundpurple)
        title_l.grid(row=0,column=0,ipadx=10,padx=90,pady=30,columnspan=5)

        tk.Label(self,text='Registration No.:',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=1,column=0,padx=10,pady=10,sticky='e')
        tk.Button(self,text='Go',width=10,bg=BACKGROUND,fg=foregroundpurple,command=self.searchreg).grid(row=1,column=2,padx=10,pady=5)
        homebtn = tk.Button(self,text='Home',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.controller.switch_frames(UserHpage))
        homebtn.place(relx=0.5,rely=0.8,anchor='center')

        self.regnoEntry = tk.Entry(self,font=BFONT)
        self.regnoEntry.grid(row=1,column=1,pady=10,sticky='w')

    @staticmethod
    def binarysearch(data,searchvalue):
        begin_index = 0
        end_index = len(data) - 1

        while begin_index <= end_index: #as long as lower
            mid_point = begin_index + (end_index - begin_index)//2 #getting the mid point should be between begin and rest
            mid_point_value = data[mid_point][0] #getting the mid point value
            # print(data[mid_point][0])
            if mid_point_value == searchvalue:
                return data[mid_point] #returning the position of the midpoint if it matches

            elif searchvalue < mid_point_value:
                end_index = mid_point - 1

            else:
                begin_index = mid_point + 1
        return None

    def searchreg(self):
        if self.regnoEntry.get() == '':
            messagebox.showwarning('Entry Incomplete','The Registration Number must be entered to proceed')
        else:
            self.booked_data = self.for_user.getbookingdata()
            sort_key = lambda name: name[0]
            self.booked_data.sort(key=sort_key,reverse=False)
            print(ChangeBooking.binarysearch(self.booked_data,self.regnoEntry.get()))

            # if self.for_user.regcheck(self.regnoEntry.get()) == []:
            if ChangeBooking.binarysearch(self.booked_data,self.regnoEntry.get()) == None:
                messagebox.showerror('Invalid','Invalid Registration Number')
            else:
                lframe = tk.LabelFrame(self,bg=BACKGROUND)
                lframe.grid(row=2,column=0,columnspan=4,padx=50,pady=10)

                movie_l = tk.Label(lframe,text='Movie',font=BFONT,bg=BACKGROUND,fg=foregroundpurple)
                movie_l.grid(row=0,column=0,padx=10,pady=5,sticky='w')
                self.movieEntry = tk.ttk.Combobox(lframe,width=18,values=self.movie_names)
                self.movieEntry.bind("<<ComboboxSelected>>",self.moviedetails)
                self.movieEntry.grid(row=0,column=1,padx=10,pady=5)

                tk.Label(lframe,text='Date',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=1,column=0,padx=10,pady=5,sticky='w')
                self.dateEntry = tk.ttk.Combobox(lframe,width=15,values=date_list)
                self.dateEntry.grid(row=1,column=1,padx=10,pady=5)

                tk.Label(lframe,text='Time',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=2,column=0,padx=10,pady=5,sticky='w')
                self.timeEntry = tk.ttk.Combobox(lframe,width=15,values=time_list)
                self.timeEntry.grid(row=2,column=1,padx=10,pady=5)

                tk.Label(lframe,text='Tickets',font=BFONT,bg=BACKGROUND,fg=foregroundpurple).grid(row=3,column=0,padx=10,pady=5,sticky='w')
                self.ticketsEntry = tk.ttk.Combobox(lframe,width=5,font=BFONT,values=[1,2,3,4,5])
                self.ticketsEntry.grid(row=3,column=1,padx=10,pady=5)

                updatebtn = tk.Button(self,text='Update Booking',width=15,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.updatereg())
                updatebtn.grid(row=3,column=0,padx=80,pady=5,sticky='e')
                deletebtn = tk.Button(self,text='Delete Booking',width=15,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.deletereg())
                deletebtn.grid(row=3,column=2,padx=10,pady=5,sticky='w')

                # data = self.for_user.regcheck(self.regnoEntry.get())
                data = ChangeBooking.binarysearch(self.booked_data,self.regnoEntry.get())
                # print(data)
                availablelisting = self.for_user.getmoviedetails(data[1])
                # print(availablelisting)
                date_data = json.loads(availablelisting[0][2])
                # print(date_data['Dates'])
                self.dateEntry.configure(values=date_data['Dates'])
                if data != []:
                    self.movieEntry.delete(0,tk.END)
                    self.movieEntry.insert(0,data[1])

                    self.dateEntry.delete(0,tk.END)
                    self.dateEntry.insert(0,data[2])


                    self.timeEntry.delete(0,tk.END)
                    self.timeEntry.insert(0,data[3])

                    self.ticketsEntry.delete(0,tk.END)
                    self.ticketsEntry.insert(0,data[4])
                else:
                    tk.messagebox.showerror('Registration Error','Registration Number doesn\'t exist in the system')

    def moviedetails(self,event):
        availablelisting = self.for_user.getmoviedetails(self.movieEntry.get())
        print(availablelisting)
        date_data = json.loads(availablelisting[0][2])
        # print(date_data['Dates'])
        self.dateEntry.configure(values=date_data['Dates'])

    def deletereg(self):
        if self.regnoEntry.get() =='':
            tk.messagebox.showwarning('Incomplete Entry','Registration number is required to delete')
        else:
            answer = tk.messagebox.askquestion('Confirmation','Are you sure you want to delete your registration?')
            if answer == 'yes':
                self.for_user.deleteregi(self.regnoEntry.get()) #deleting query
                tk.messagebox.showinfo('Delete confirmation','Your registration has been deleted successfully.')
                self.regnoEntry.delete(0,tk.END)
                self.movieEntry.delete(0,tk.END)
                self.dateEntry.delete(0,tk.END)
                self.timeEntry.delete(0,tk.END)
                self.ticketsEntry.delete(0,tk.END)
            else:
                print('ok')

    def updatereg(self):
        if (self.movieEntry.get() and self.dateEntry.get() and self.timeEntry.get() and self.ticketsEntry.get()) == '':
            tk.messagebox.showwarning('Entry error','Fill all the Entries')
        else:
            price = str(int(self.ticketsEntry.get()) * 100)
            self.for_user.updatebooking(self.movieEntry.get(),self.dateEntry.get(),self.timeEntry.get(),self.ticketsEntry.get(),price,self.regnoEntry.get())
            tk.messagebox.showinfo('Booking update','Booking was updated successfully')


            self.totalprice = str(int(self.ticketsEntry.get())*100) #getting the total price of the tickets

            root = tk.Toplevel()
            root.configure(bg=BACKGROUND)
            root.geometry('600x600')

            width,height = 600,600

            self.canvas = tk.Canvas(root, width=width, height=height)
            self.canvas.pack()

            pil_img = Image.open(os.path.join(os.getcwd(),'movieposter',self.movieEntry.get()+'blur'+'.jpg'))
            self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
            self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

            try:
                img_p = Image.open(os.path.join(os.getcwd(),'movieposter',self.movieEntry.get()+'.jpg'))
                img_var = ImageTk.PhotoImage(image=img_p)

                pimg = tk.Label(self.canvas, image=img_var,bg=BACKGROUND)
                pimg.configure(image=img_var)

                pimg.place(relx=0.5,rely=0.2,anchor='center')
            except:
                print('Image Couldn\'t be downloaded')

            newlframe = tk.LabelFrame(self.canvas,bg=darkgray)
            newlframe.place(relx=0.5,rely=0.65,anchor='center',width=260,height=260)

            tk.Label(newlframe,text='Booking updated Successfully',font=BFONT,bg=darkgray,fg=blued).grid(row=0,column=0,padx=15,pady=5,sticky='ew')
            # tk.Label(newlframe,text='Registration No.: '+ self.regnoEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=1,column=0,padx=5,pady=5,sticky='w')
            tk.Label(newlframe,text=self.movieEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=2,column=0,padx=15,pady=5,sticky='ew')
            tk.Label(newlframe,text='Date: '+ self.dateEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=3,column=0,padx=15,pady=5,sticky='ew')
            tk.Label(newlframe,text='Time: '+self.timeEntry.get(),font=BFONT,bg=darkgray,fg=blued).grid(row=4,column=0,padx=15,pady=5,sticky='ew')
            tk.Label(newlframe,text='Tickets: '+self.ticketsEntry.get() ,font=BFONT,bg=darkgray,fg=blued).grid(row=5,column=0,padx=15,pady=5,sticky='ew')
            tk.Label(newlframe,text='Total Price: NRS.'+ self.totalprice,font=BFONT,bg=darkgray,fg=blued).grid(row=6,column=0,padx=15,pady=5,sticky='ew')
            tk.Label(newlframe,text='Please don\'t forget Your Registration number',font=('Italic',5),bg=darkgray,fg=blued).grid(row=7,column=0,padx=15,pady=10,sticky='ew')
            tk.Button(newlframe,text='Exit',width=10,bg=darkgray,fg=blued,command=lambda:
                root.destroy()).grid(row=8,column=0,padx=5,pady=5)

            root.mainloop()




class ViewMoviesUser(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller


        self.for_user = ForUser()

        self.configure(background=BACKGROUND)




        title_l = tk.Label(self,text='Available Movies',font=TFONT,bg=BACKGROUND,fg=foregroundpurple)
        title_l.grid(row=0,column=0,ipadx=100,padx=90,pady=30,columnspan=5)

        self.movieEntry = tk.ttk.Entry(self,width=30)
        self.movieEntry.grid(row=1,column=0,columnspan=2,padx=30,pady=5,sticky='w')

        search_btn = tk.Button(self,text='Search',bg=BACKGROUND,fg=foregroundpurple,command=self.searchdata)
        search_btn.grid(row=1,column=1,pady=5,padx=30,sticky='e')

        sort_com = tk.Label(self,text='Sort By',font=MFONT,bg=BACKGROUND,fg=foregroundpurple)
        sort_com.grid(row=1,column=3,sticky='e')

        # tk.Label(self,text='Sort By',font=BFONT,bg=BACKGROUND,fg=foregroundgray).grid(row=1,column=0,padx=50,pady=5,sticky='w')
        self.sortby = tk.ttk.Combobox(self,width=18,values=['Movie Name','Genre'])
        self.sortby.current(0)
        self.sortby.bind("<<ComboboxSelected>>",self.sorting)
        self.sortby.grid(row=1,column=4,padx=10,pady=5,sticky='w')
        homebt = tk.Button(self,text='Home',bg=BACKGROUND,width=20,fg=foregroundpurple,command=lambda: self.controller.switch_frames(UserHpage))
        homebt.place(relx=0.5,rely=0.8,anchor=tk.CENTER)


        # tk.Label(self,text='OR',font=('Italic',5),bg=BACKGROUND,fg=foregroundpurple).grid(row=2,column=1,padx=10,pady=10,sticky='w')
        # tk.Button(self,text='View Movies',width=10,bg=BACKGROUND,fg=foregroundpurple,command=self.views).grid(row=3,column=1,padx=5,pady=5)
        # tk.Button(self,text='Home',width=10,bg=BACKGROUND,fg=foregroundpurple,command=lambda:self.controller.switch_frames(UserHpage)).grid(row=20,column=1,padx=5,pady=5)

    @staticmethod
    def insertion_sort(sequence,num):

        for i in range(1,len(sequence)):
            while sequence[i-1][num] > sequence[i][num] and i>0: #loop condition and to avoid negative index
                sequence[i-1],sequence[i] = sequence[i],sequence[i-1]
                i = i-1 #incrementally moving backwards
        return sequence


    def searchdata(self):
        if self.movieEntry.get() == '':
            tk.messagebox.showwarning('Entry Unfilled','The Movie name must be searched')
        else:
            try:
                self.treeFrame.destroy()
            except Exception as e:
                print(e)
            self.treeFrame = tk.Frame(self,background=BACKGROUND)
            self.treeFrame.grid(row=4,column=0,columnspan=5,rowspan=10,padx=30,pady=30)

            self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Movie','Genre'),style="Treeview")
            self.style = tk.ttk.Style()

            self.style.theme_use("clam")
            self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground=foregroundgray)
            self.style.map('Treeview',background=[('selected',orgcolor)])


            self.treeViewF.grid(row=0,column=0,columnspan=4)
            self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)
            self.treeViewF['show'] = 'headings'

            self.treeViewF.column('Movie',width=150,anchor='center')
            self.treeViewF.column('Genre',width=150,anchor='center')

            self.treeViewF.heading('Movie',text='Movie')
            self.treeViewF.heading('Genre',text='Genre')
            self.tree = self.treeViewF


            for values in self.for_user.searchmovie(self.movieEntry.get()):
                self.tree.insert('', 'end', text='', value=values)



            self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
            self.treeViewF.configure(yscrollcommand=self.scroll.set)
            self.scroll.grid(row=0,column=5,sticky='ns')


    def movieNView(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=5,column=0,columnspan=5,rowspan=10,padx=30,pady=30)

        self.style = tk.ttk.Style(self.treeFrame)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background=BACKGROUND,fieldbackground=BACKGROUND,foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])

        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Movie','Genre'))

        self.treeViewF.grid(row=0,column=0,columnspan=4)

        self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)

        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('Movie',width=150,anchor='center')
        self.treeViewF.column('Genre',width=150,anchor='center')


        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Genre',text='Genre')

        self.tree = self.treeViewF

        if self.movieEntry.get() == '':
            for values in ViewMoviesUser.insertion_sort(self.for_user.getmoviedata(),0):
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = ViewMoviesUser.insertion_sort(self.for_user.searchmovie(self.movieEntry.get()),0) #Sorting data
            for values in data:
                self.tree.insert('','end',text='',value=values)

        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=5,sticky='ns')

    def genreView(self):
        self.treeFrame = tk.ttk.Frame(self)
        self.treeFrame.grid(row=5,column=0,columnspan=5,rowspan=10,padx=30,pady=30)

        self.canvas = tk.Canvas(self)

        self.style = tk.ttk.Style(self.treeFrame)

        self.style.theme_use("clam")
        self.style.configure("Treeview", background='#24262E',fieldbackground='#24262E',foreground="white")
        self.style.map('Treeview',background=[('selected','#B28360')],foreground=[('selected','black')])

        self.treeViewF = tk.ttk.Treeview(self.treeFrame,column=('Movie','Genre'))
        self.treeViewF.grid(row=0,column=0,columnspan=4)

        self.treeViewF.bind('<<TreeviewSelect>>',self.onclick)

        self.treeViewF['show'] = 'headings'

        self.treeViewF.column('Movie',width=150,anchor='center')
        self.treeViewF.column('Genre',width=150,anchor='center')

        self.treeViewF.heading('Movie',text='Movie')
        self.treeViewF.heading('Genre',text='Genre')

        self.tree = self.treeViewF

        if self.movieEntry.get() == '':
            for values in ViewMoviesUser.insertion_sort(self.for_user.getmoviedata(),1):
                self.tree.insert('', 'end', text='', value=values)
        else:
            data = ViewMoviesUser.insertion_sort(self.for_user.searchmovie(self.movieEntry.get()),1) #Sorting data
            for values in data:
                self.tree.insert('','end',text='',value=values)

        self.scroll = tk.ttk.Scrollbar(self.treeFrame,orient=tk.VERTICAL,command=self.treeViewF.yview)
        self.treeViewF.configure(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0,column=5,sticky='ns')




    def sorting(self,event): #getting the event from the binding in combobox
        if self.sortby.get() == 'Movie Name':
            self.movieNView()
        elif self.sortby.get() == 'Genre':
            self.genreView()

    def onclick(self,event):
        print('selected items: ')
        # print(self.treeViewF.selection())
        curitem = self.treeViewF.focus()  #getting the current selected item
        self.moviename = self.treeViewF.item(curitem)['values'][0]
        self.moviedata = moviedata(self.moviename) #getting the movie data
        if self.moviedata is False:
            tk.messagebox.showerror('Can\'t Connect','There seems to be a problem with the network or name')
        else:
            if self.moviedata == {}:
                tk.messagebox.showerror('Movie Not Found','The name was too long or unreqnizable or is in foreign language')
            else:
                self.popupdetails()
            # print(self.moviedata)


    def popupdetails(self):
        rook = tk.Toplevel()
        rook.geometry('650x600')
        rook.configure(background='#1D2021')
        #696969
        print(self.moviename)

        titlel = tk.Label(rook,text=self.moviedata['title'],foreground=blued,bg='#1D2021',font=('Times','18'))
        titlel.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

        year_l = tk.Label(rook,text='Year: '+self.moviedata['year'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        year_l.grid(row=1,column=1,padx=10,pady=5,sticky='w')

        rated_l = tk.Label(rook,text='Rated: '+self.moviedata['rated'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        rated_l.grid(row=2,column=1,padx=10,sticky='w')

        runtime_l =tk.Label(rook,text='Runtime: '+self.moviedata['runtime'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        runtime_l.grid(row=3,column=1,padx=10,sticky='w')

        genre_l = tk.Label(rook,text='Genre: '+self.moviedata['genre'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        genre_l.grid(row=4,column=1,padx=10,sticky='w')

        director_l = tk.Label(rook,text='Director: '+self.moviedata['director'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        director_l.grid(row=5,column=1,padx=10,sticky='w')

        language_l = tk.Label(rook,text='Language: '+self.moviedata['language'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        language_l.grid(row=6,column=1,padx=10,sticky='w')

        tk.Label(rook,bg='#1D2021').grid(row=7,column=1)
        tk.Label(rook,bg='#1D2021').grid(row=8,column=1)

        if len(self.moviedata['writer'].split(',')) < 5:
            writer_l = tk.Label(rook,text='Writer: '+self.moviedata['writer'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
            writer_l.grid(row=9,column=0,columnspan=5,padx=5,sticky='w')
        else:
            writers = self.moviedata['writer'].split(',')
            writer_l = tk.Label(rook,text='Writer: '+writers[0]+writers[1]+writers[2]+'...',foreground='#7096EE',bg='#1D2021',font=('Times','11'))
            writer_l.grid(row=9,column=0,columnspan=5,padx=5,sticky='w')

        if len(self.moviedata['actors'].split(',')) < 5:
            actors_l = tk.Label(rook,text='Actors: '+self.moviedata['actors'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
            actors_l.grid(row=10,column=0,columnspan=5,padx=5,sticky='w')
        else:
            actors = self.moviedata['actors'].split(',')
            actors_l = tk.Label(rook,text='Actors: '+actors[0]+actors[1]+actors[2]+'...',foreground='#7096EE',bg='#1D2021',font=('Times','11'))
            actors_l.grid(row=10,column=0,columnspan=5,padx=5,sticky='w')


        awards_l = tk.Label(rook,text='Awards: '+self.moviedata['awards'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        awards_l.grid(row=11,column=0,columnspan=5,padx=5,sticky='w')

        ratings_l = tk.Label(rook,text='Ratings',foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        ratings_l.grid(row=12,column=1)

        IMdb_l = tk.Label(rook,text='IMdb: '+self.moviedata['imdb_rating'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        IMdb_l.grid(row=13,column=0,sticky='w')

        rottent_l = tk.Label(rook,text=self.moviedata['ratings'][1]['source']+': ' +self.moviedata['ratings'][1]['value'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
        rottent_l.grid(row=13,column=1)

        try:
            meta_l = tk.Label(rook,text=self.moviedata['ratings'][2]['source']+': ' +self.moviedata['ratings'][2]['value'],foreground='#7096EE',bg='#1D2021',font=('Times','11'))
            meta_l.grid(row=13,column=2,sticky='e')
        except IndexError as e:
            print(e)


        imdb_id = self.moviedata['imdb_id']
        self.imdb_link = 'https://www.imdb.com/title/' + imdb_id


        imdb_b = tk.Button(rook,text='Visit IMDb',bg=BACKGROUND,fg='#7096EE',command=self.openimdb)
        imdb_b.grid(row=14,column=1)

        img_p = Image.open(os.path.join(os.getcwd(),'movieposter',self.moviename+'.jpg'))
        img_var = ImageTk.PhotoImage(image=img_p)

        pimg = tk.Label(rook, image=img_var)
        pimg.configure(image=img_var)

        pimg.grid(row=1,column=0,rowspan=7)

        rook.mainloop()

    def openimdb(self):
        webbrowser.open(self.imdb_link,new=1)






if __name__ == '__main__':
    app = window()
    app.mainloop()


