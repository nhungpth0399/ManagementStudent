import datetime
import invalidDoB


def get_ID():

    id = int(input())

    while True:
        #student = self.search_student(id)
        student = False
        if id <= 170000 or id >= 179999 or student != False:
            print("ID mistake, please re-enter ID: ")
            id = int(input())
        else:
            break

    return id

def get_fname():

    fna = input()
    while True:
        if (fna.isalpha() == False):
            while True:
                fna = input("Re-enter First Name: ")
        else:
            break

    fname = fna.title()
    return fname

def get_lname():

    lna = input()
    lname = lna.title()
    return lname

def get_gender():
    print("Enter one of the following options: Male, Female or Intersex:")
    gender = input()
    while True:
        if gender != "Male" and gender != "Female" and gender != "Intersex":
            print("Gender mistake, please re-enter gender: ")
            gender = input()
        else:
            break
    return gender

def get_phone():

    phonenb = int(input())
    while True:
        if len(str(phonenb)) != 11:
            print("Re-enter phone: ")
            phonenb = int(input())
        else:
            break
    return phonenb

def get_dob():
    
    value = input()
    day, month, year = list(map(int, value.split("/")))
    a = invalidDoB.check_date(year, month, day)
    while a == False:
        value = input("Re-enter Date of birth: ")
        day, month, year = list(map(int, value.split("/")))
        a = invalidDoB.check_date(year, month, day)
    return str(value)

def get_midterm():

    mid = float(input())
    while mid < 0 or mid > 10:
        print("Mid-term score mistake, please re-enter: ")
        mid = float(input())
    return mid

def get_final():

    final = float(input())
    while final < 0 or final > 10:
        print("Final score mistake, please re-enter: ")
        final = float(input())
    return final


