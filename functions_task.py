import datetime
from dateutil import relativedelta

now = datetime.datetime.now()

def check_birthdate(year, month, day):
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    
    if month > 12 or day > 31:
        return False
    elif now.year != year:
        return now.year > year
    elif now.month != month:
        return now.month > month
    else:
        return now.day > day
    

def calculate_age(year, month, day):
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    
    birth = datetime.datetime(year, month, day)
    diff = relativedelta.relativedelta(now, birth)
    
    years_dif = diff.years;
    months_dif = diff.months;
    days_dif = diff.days;
    
    print("You are", years_dif, "years,", months_dif, "months, and", days_dif, "days")
    
    
year = input("Enter year of birth: ")
month = input("Enter month of birth: ")
day = input("Enter day of birth: ")

if check_birthdate(year, month, day):
    calculate_age(year, month, day)
else:
    print("Invalid Birthday!")
    