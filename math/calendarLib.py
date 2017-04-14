import time
def getDayOfWeek(date): #date is [d,m,y] (ints)
    #print "Today's Date: " + str(date[1]) + "/" + str(date[0]) + "/" + str(date[2])
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
        months[1] = 29
    #1/1/2000 was a saturday
    numLeapsSince = (date[2] / 4) + 1 #number of leap februarys since 1/1/2000
    weekShift = date[2] + numLeapsSince #weekShift for january first of this year
    for i in range(0, len(months)): #weekshift for first of the month
        if i + 1 >= date[1]:
            break
        weekShift += months[i]
    weekShift += date[0] - 1 #weekshift for today
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    #print "Day of Week: " + days[(6 + weekShift) % 7]
    return (6 + weekShift) % 7

def getDaysSince(date): #date formate is [d,m,y] (ints)
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
        months[1] = 29
    numLeapsSince = (date[2] / 4) + 1 #number of leap februarys since 1/1/2000
    daysSince = 365*(date[2] - numLeapsSince) + 366*numLeapsSince
    for i in range(0, len(months)): #weekshift for first of the month
        if i + 1 >= date[1]:
            break
        daysSince += months[i]
    daysSince += date[0] - 1
    #XKCD 1809 pub: 3/10/17
    return daysSince - 6278

def howManyXKCDs():
    #XKCD 1809 published friday 3/10/17
    date = [int(time.strftime("%d")),int(time.strftime("%m")),int(time.strftime("%y"))]
    daysSince = getDaysSince(date)
    dayOfWeek = getDayOfWeek(date)
    numXKCDs = (daysSince / 7)*3
    numXKCDs += (dayOfWeek + 1) / 2
    return numXKCDs + 1809
    

#print "XKCD Number is " + str(howManyXKCDs())
    
