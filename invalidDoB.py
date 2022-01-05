
import datetime

def check_date(year, month, day):
    correctDate = None
    try:
        newDate = datetime.datetime(year, month, day)
        correctDate = True
        print("DoB valid")
    except ValueError:
        correctDate = False
        print("DoB is invalid, Please re-enter: ")
    return correctDate