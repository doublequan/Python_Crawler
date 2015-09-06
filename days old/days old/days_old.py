#problem: Given your birthday and current data, calculate your age in days.
#Compensate for leap days. Assume that the birthday and current date are 
#corrent dates(and no time travel). Simply put, if you were born 1 Jan 2012
#and todays date is 2 Jan 2012 you are 1 day old

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



#return true if input is a leapyear
def isLeapYear(year):
    return year % 4 == 0

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    #first, caculate the integrated year
    year = y1 + 1
    while year < y2:
        if isLeapYear(year):
            days += 366
        else:
            days += 365
        year += 1
    #second, caculate the integrated month
    if y1 == y2:
        month = m1 + 1
        while month < m2:
            days += daysOfMonths[month-1]
        if isLeapYear(y1) and m1 < 2 and m2 > 2:
            days += 1
    else:
        month = m1 + 1
        if isLeapYear(y1) and m1 < 2:
             days += 1
        while month <= 12:
            days += daysOfMonths[month-1] 
            month += 1
        month = 1
        if isLeapYear(y2) and m2 > 2:
             days += 1
        while month < m2:
            days += daysOfMonths[month-1] 
            month += 1
    #third, caculate the unintergrated month
    if y1 == y2 and m1 == m2:
        days += d2-d1
    else:
        if isLeapYear(y1) and m1 == 2:
            days += 1
        days += daysOfMonths[m1-1] - d1
        days += d2
    #end, return days
    return days

print daysBetweenDates(2000,2,1,2001,2,1)
             
