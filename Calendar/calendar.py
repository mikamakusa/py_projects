"""
Command Line Calendar
"""

from time import sleep, strftime

fname = input("Enter your first name : ")
calendar = {}


def welcome(name):
    print("Welcome %s" % name)
    print("Calendar starting...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("Current time: " + strftime("%H:%M:%S"))
    sleep(1)
    print("What do you like to do?")


def start_calendar():
    welcome(fname)
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to delete, X to Exit:")
        user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print("Calendar empty.")
            else:
                print(calendar)
        elif user_choice == "U":
            date = input("What date ? ")
            update = input("Enter the update : ")
            calendar[date] = update
            print("Update successful")
            print(calendar)
        elif user_choice == "A":
            event = input("Enter Event: ")
            date = input("Enter date (MM/DD/YY): ")
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("date invalid!")
                try_again = input("Try Again ? Y for yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                elif try_again == "N":
                    start == False
                else:
                    start == False
            elif date in calendar:
                calendar[date] += event + ","
            else:
                calendar[date] = event
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print("Calendar Empty")
            else:
                event = input("What event?")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print("Calendar Event Successful")
                    else:
                        print("Incorrect Event")
        elif user_choice == "X":
            start == False
        else:
            print("Invalid Command")
            start == False


start_calendar()
