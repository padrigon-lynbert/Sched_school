from datetime import datetime

def day_today():
    day_number = datetime.today().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    return days[day_number]

def time_now():
    date = datetime.today().date() 
    time = datetime.now().strftime("%H:%M")

    return print(f"{date}: {day_today()} {time}")

def sched_acads(day):
    if day == "Monday":
        print


time_now()
# day_today()

# tdelta = datetime.timedelta(days=7)
# print(date + tdelta)

# bday = datetime.date(2024, 6, 20)
# til_bday = bday - date

# print(til_bday)