"""Collection of queries in each method to be used by the Admin's and User's module to perform several Functionalities"""
from sqdb.connections import Database


class ForUser:
    def __init__(self):
        self.database = Database()

    def enteruserdata(self,username,firstn,lastn,mobno,confirmp):
        if username == '':
            return False
        else:
            valuues = (username,firstn,lastn,mobno,confirmp)
            queri = f"Insert into userdata values {valuues}"
            self.database.normalexec(queri)
            return True

    def checkusername(self,username):
        queri = "select username from userdata"
        datas = self.database.get_all_data(queri)
        for names in datas:
            if names[0] == username:
                return True
            else:
                return False

    def check_Credentials(self,creds=tuple): #fetching the credentials i.e. uname and password
        queri = """select username,confirmpassword from userdata
                where username = %s and confirmpassword = %s"""
        values = creds
        data = self.database.fetch_data(queri,values)
        return data

    def display_movies(self):
        queri = "select movie_name,movie_genre from moviedetail" #for viewing
        data = self.database.get_all_data(queri)
        return data

    def getmoviename(self): #exists or not
        queri = "select movie_name from moviedetail"
        data = self.database.get_all_data(queri)
        return data

    def getmoviedetails(self,name):
        value = name
        queri =  f"select movie_name,movie_genre,dates from moviedetail where movie_name = '{value}'"
        data = self.database.get_all_data(queri)
        return data

    def bookmovie(self,regno,movie,date,time,ticket,price):
        valuues = (regno,movie,date,time,ticket,price)
        queri = f"Insert into bookedmovie (registrationN,movie_name,date_booked,time_booked,tickets,price) values {valuues}"
        self.database.normalexec(queri)

    def regcheck(self,registration):
        regno = registration
        queri = f"Select * from bookedmovie where registrationN = {regno}"
        data = self.database.get_all_data(queri)
        return data

    def getbookingdata(self):
        queri = "Select * from bookedmovie"
        data = self.database.get_all_data(queri)
        return data

    def deleteregi(self,registration):
        regno = registration
        if regno == '':
            return False
        else:
            queri = f"Delete from bookedmovie where registrationN = {regno}"
            self.database.normalexec(queri) #
            return True


    def updatebooking(self,nmovie,ndate,ntime,nticket,nprice,registration):
        values = (nmovie,ndate,ntime,nticket,nprice,registration)
        queri = "Update bookedmovie set movie_name = %s,date_booked = %s, time_booked = %s, tickets = %s, price = %s where registrationN = %s"
        self.database.normalexecvalues(queri,values)

    def searchmovie(self,moviename):
        if moviename == '':
            return False
        else:
            queri = "Select movie_name,movie_genre from moviedetail where movie_name like %s"
            value = (str(moviename) + "%",)
            data = self.database.fetch_data(queri,value)
            return data

    def getmoviedata(self):
        queri = "Select movie_name,movie_genre from moviedetail"
        data = self.database.get_all_data(queri)
        return data

    def orderbymovie(self):
        queri = "Select movie_name,movie_genre from moviedetail order by movie_name"
        data = self.database.get_all_data(queri)
        return data

    def orderbygenre(self):
        queri = "Select movie_name,movie_genre from moviedetail order by movie_genre"
        data = self.database.get_all_data(queri)
        return data

    def getuserdata(self,username):
        value = username
        queri = f"select username,firstname,lastname from userdata where username = '{value}'"
        data = self.database.get_all_data(queri)
        return data



class ForAdmin:
    def __init__(self):
        self.database = Database()

    def enteradmindata(self,username,firstn,lastn,mobno,confirmp):
        valuues = (username,firstn,lastn,mobno,confirmp)
        queri = f"Insert into admindata values{valuues}"
        self.database.normalexec(queri)

    def checkusername(self,username):
        queri = "select username from admindata"
        datas = self.database.get_all_data(queri)
        for names in datas:
            if names[0] == username:
                return True
            else:
                return False

    def getadmindata(self,username):
        value = username
        queri = f"select username,firstname,lastname from admindata where username = '{value}'"
        data = self.database.get_all_data(queri)
        return data

    def check_Credentials(self,creds=tuple): #fetching the credentials i.e. uname and password
        queri = """select username,confirmpassword from admindata
                where username = %s and confirmpassword = %s"""
        values = creds
        data = self.database.fetch_data(queri,values)
        return data

    def addMovies(self,name,genre,dates):
        valuees = (name,genre,dates)
        query = f"Insert into moviedetail (movie_name,movie_genre,dates) values {valuees}"
        self.database.normalexec(query)

    def searchadd(self,name):
        movien = name
        queri = f"Select movie_name,movie_genre from moviedetail where movie_name = '{movien}'"
        data = self.database.get_all_data(queri)
        return data

    def deletemovie(self,name):
        movien = name
        if movien == '':
            return False
        else:
            queri = f"Delete from moviedetail where movie_name = '{movien}'"
            self.database.normalexec(queri)
            return True

    def updateaddition(self,name,genre,dates):
        values = (name,genre,dates,name)
        queri = "Update moviedetail set movie_name = %s,movie_genre = %s,dates = %s where movie_name = %s"
        self.database.normalexecvalues(queri,values)
        return True

    def checkbooked(self):
        queri = "Select movie_name,date_booked,time_booked,tickets,price from bookedmovie"
        data = self.database.get_all_data(queri)
        return data

    def bookeddetails(self):
        queri = "Select * from bookedmovie"
        data = self.database.get_all_data(queri)
        return data

    def orderbymovie(self):
        queri = "Select * from bookedmovie order by movie_name"
        data = self.database.get_all_data(queri)
        return data

    def orderbydate(self):
        queri = "Select * from bookedmovie order by date_booked"
        data = self.database.get_all_data(queri)
        return data

    def orderbytime(self):
        queri = "Select * from bookedmovie order by time_booked"
        data = self.database.get_all_data(queri)
        return data

    def orderbytickets(self):
        queri = "Select * from bookedmovie order by tickets"
        data = self.database.get_all_data(queri)
        return data

    def orderbyprice(self):
        queri = "Select * from bookedmovie order by price"
        data = self.database.get_all_data(queri)
        return data

    def getusers(self):
        queri = "Select username,firstname,lastname,mobilenumber from userdata"
        data = self.database.get_all_data(queri)
        return data

    def orderbyuname(self):
        queri = "Select username,firstname,lastname,mobilenumber from userdata order by username"
        data = self.database.get_all_data(queri)
        return data

    def orderbyfname(self):
        queri = "Select username,firstname,lastname,mobilenumber from userdata order by firstname"
        data = self.database.get_all_data(queri)
        return data

    def orderbylname(self):
        queri = "Select username,firstname,lastname,mobilenumber from userdata order by lastname"
        data = self.database.get_all_data(queri)
        return data

    def orderbymobile(self):
        queri = "Select username,firstname,lastname,mobilenumber from userdata order by mobilenumber"
        data = self.database.get_all_data(queri)
        return data






