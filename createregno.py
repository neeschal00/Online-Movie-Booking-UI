"""Module consisting of function to generate registration number for booking and and get dates of next 6 days"""
from datetime import datetime,timedelta


def generatereg():
    current_dt = datetime.now()
    # print(current_dt)
    formatting_dt = current_dt.strftime('%Y%m%d%H%M%S%f')
    return formatting_dt

def getdates(): #To get the date list of next 6 days
    current_dt = datetime.now().date()
    date_list = []
    for i in range(1,7):
        dates = current_dt + timedelta(days=int(i))
        formatted_date = dates.strftime('%m/%d/%Y')
        date_list.append(formatted_date)
    return date_list


# print(getdates())


