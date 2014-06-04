import datetime
from datetime import datetime
import time
import os
import Tkinter
import tkMessageBox


def findNumDays(month , year):
    if month <= 7:
        if month % 2 == 1:
            return 31
        else:
            if month == 2:
                if year % 4 == 0:
                    return 29
                else:
                    return 28
            else:
                return 30
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30

def deltaCheck(day , month , year):
    daysInYear = 365
    daysLeft = 0
    if year % 4 == 0:
        daysInYear = 366
    if month == 12:
        daysLeft = daysInYear - day
    else:
        while day < findNumDays(month , year):
            daysLeft = daysLeft + 1
            day = day + 1
        month = month + 1
        while month < 12:
            daysLeft = daysLeft + findNumDays(month , year)
            month = month + 1
#    daysLeft = daysLeft - 1
#    minutesLeft = datetime.minute()
#    hoursLeft = datetime.hour()
#    if hoursLeft > 24:
#        daysLeft = daysLeft - 1
#        hours = hour - 24
    daysLeft = str(daysLeft)
#    daysLeft = daysLeft + " " + str(hoursLeft) + ":" + str(minutesLeft)
    return daysLeft

def report():
	if getStateVar() == 1:
		f = open(HOMEDIR + "/anniversary/config.txt" , 'r')
		monthGoal = int(f.readline())
		dayGoal = int(f.readline())
		f.close()
	else:
		monthGoal = input("Month of Anniversary: ")
		dayGoal = input("Day of Anniversary: ")
	date = str(datetime.now())
	year = int(date[0] + date[1] + date[2] + date[3])
	month = int(date[5] + date[6])
	day = int(date[8] + date[9])
	numDays = findNumDays(month , year)
	hour = int(date[11] + date[12])
	minute = int
	daysLeft = numDays - day + dayGoal
	timeLeft = deltaCheck(day , month , year)
	MESSAGE = "Days to next monthy: " + str(daysLeft) + "\nTime to next anniversary: " + str(timeLeft) + "\nAnniversary: " + str(monthGoal) + "/" + str(dayGoal)
	if day == dayGoal:
		if month == monthGoal:
			MESSAGE = "Today is your anniversary!" + "\nAnniversary: " + str(monthGoal) + "/" + str(dayGoal)
		else:
			MESSAGE = "Today is your monthy!" + "\nAnniversary: " + str(monthGoal) + "/" + str(dayGoal)
	#print MESSAGE
#	f = open(HOMEDIR + "/anniversary/output.txt" , 'w')
#	f.write(MESSAGE)
#	f.close()
#	top = Tkinter.Tk()
	tkMessageBox.showinfo("AnniversaryReminder" , MESSAGE)
#	top.mainloop()


def getStateVar():
	PATH = HOMEDIR + '/anniversary'
	if os.path.exists(PATH) == False:
		print("Consider reinstalling or manually put a blankfile called config.txt into ~/anniverary")
		return 0
	else:
		f = open(HOMEDIR + '/anniversary/config.txt' , 'r')
		if f.readline() != '':
			f.close()
			return 1
		f.close()
		y = 1
		n = 0
		if input("Your anniversary date is not set. Set now? (y/n) ") == 1:
			month = input("Month of Anniversary: ")
			day = input("Day of Anniversary: ")
			f = open(HOMEDIR + '/anniversary/config.txt' , 'w')
			f.write(str(month) + '\n')
			f.write(str(day) + '\n')
			f.close()
			return 1
		else:
			return 0

HOMEDIR = os.path.expanduser('~')
report()
