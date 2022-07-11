from functools import wraps 
from datetime import date

def legal_drinking_age(legal_age):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            age = func(*args, **kwargs)
            if age < legal_age:
                print('You are not allowed to drink')
            return age
        return wrapper
    return decor

@legal_drinking_age(6570) # in days
def age_checker():    
    print('Enter your birthday')
    year = int(input('Birth year:'))
    month = int(input('Birth month ( in number ):'))
    day = int(input('Birth day:'))
    birthday = date(year, month, day)
    today = date.today()
    print(today - birthday)
    td = (today - birthday).days
    return td
    
    
age_checker()