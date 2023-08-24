from datetime import datetime
import os

def day_today():
    global day_number
    day_number = datetime.today().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    return days[day_number]

def time_now():
    date = datetime.today().date() 
    time = datetime.now().strftime("%H:%M")

    return print(f"{date}: {day_today()} {time}")

def sched_acads(day):
    sched = [
    """
    Saucelit | 11:30-13:00\n\
    PE       | 13:00-14:00
        
    """, 
    "No classes today.",
    """
    Humcom   | 11:30-13:00
    Qwimms   | 13:30-15:00
    Web	     | 15:00-16:30
    """,
    "No classes today",
    """
    iPat     | 06:30-08:00
    Netw     | 08:30-10:00
    DSA      | 10:00-11:30
    """,
    "No classes today",
    "No classes today"]
        
    return print(sched[day_number])
    
def run():
    os.system('cls')
    time_now(); 
    print("\nSchedules: ")
    sched_acads(day_today())
    input("\n<enter>\n\n")
    os.system('cls')
run()