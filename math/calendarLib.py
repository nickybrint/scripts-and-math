import time
def getDayOfWeek(date):
    """Returns the day of the week of the input
    
    Parameter:
    date = [day, month, 2-digit year]
    ex: March 10, 2017 --> [10, 3, 17]
    """

    months = [31,28,31,30,31,30,31,31,30,31,30,31] #months of THIS year
    
    if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
        months[1] = 29    
    numLeapsSince = (date[2] / 4) + 1 #number of leap februarys since 1/1/2000
    weekShift = date[2] + numLeapsSince #weekShift for january first of this year
    for i in range(0, len(months)): #weekshift for first of the month
        if i + 1 >= date[1]:
            break
        weekShift += months[i]
    weekShift += date[0] - 1 #weekshift for today
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    #[1, 1, 00] was a saturday
    return (6 + weekShift) % 7

def getDaysSince(date):
    """Returns the number of days since March 10, 2017
    
    Parameter:
    date = [day, month, 2-digit year]
    ex: March 10, 2017 --> [10, 3, 17]
    """
    
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    #calculate the number of days since [1, 1, 00]
    if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
        months[1] = 29
    numLeapsSince = (date[2] / 4) + 1 #number of leap februarys since 1/1/2000
    daysSince = 365*(date[2] - numLeapsSince) + 366*numLeapsSince
    for i in range(0, len(months)): #weekshift for first of the month
        if i + 1 >= date[1]:
            break
        daysSince += months[i]
    daysSince += date[0] - 1
    
    #XKCD 1809 pub: [10, 3, 17], 6278 days after [1, 1, 00]
    return daysSince - 6278 

def howManyXKCDs():
    """Returns the most recent XKCD number. (XKCD is only published on Monday, Wednesday, and Friday)"""
    #XKCD 1809 was published Friday, March 10, 2017
    date = [int(time.strftime("%d")),int(time.strftime("%m")),int(time.strftime("%y"))]
    daysSince = getDaysSince(date)
    dayOfWeek = getDayOfWeek(date)
    numXKCDs = (daysSince / 7)*3
    numXKCDs += (dayOfWeek + 1) / 2
    return numXKCDs + 1809
    
if __name__ == "__main__":
    print "XKCD Number is " + str(howManyXKCDs())
    
