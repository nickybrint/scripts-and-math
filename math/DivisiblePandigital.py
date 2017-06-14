#Pandigital Divisibility Finder:
#Finds all 0 to 9 pandigital numbers such that 17 divides d8d9d10, 13|d7d8d9, 11|d6d7d8, etc.
#ex: 4160357289 ==> 17 divides 289, 13 divides 728, 11|572, 7|357, 5|035, 3|603, and 2|160

possiblyValidNumbers = []
primes = [17,13,11,7,5,3,2]

#find all 3-digit numbers with unique digits that are divisible by first prime
for number in range(12,988):
    hasUniqueDigits = True
    for digitIndex in range(0, len(str(number))):
        otherDigits = str(number)[:digitIndex:] #remove digit from number
        if str(number)[digitIndex] in otherDigits:
            hasUniqueDigits = False
            break
        
    if hasUniqueDigits and number % primes[0] == 0:
        if number < 100:
            possiblyValidNumbers.append("0" + str(number))
        else:
            possiblyValidNumbers.append(str(number))

def checkTriple(possiblyValidNumbers, iteration, primes):
    #take leftmost two digits of each possibly valid number and determine which digits 0-9 added to the left
    #make the number possibly valid: 1) no repeated digits, and 2) divisible by the next prime
    placeholderList = []
    for number in possiblyValidNumbers:
        for leftDigit in range(0,10):
            if (not str(leftDigit) in number) and int(str(leftDigit) + number[:2]) % primes[iteration] == 0:
                    placeholderList.append(str(leftDigit) + number)
                    
    #replace old list with new one
    del possiblyValidNumbers[:]
    for number in placeholderList:
        possiblyValidNumbers.append(number)

for iteration in range(1, len(primes)):
    checkTriple(possiblyValidNumbers, iteration, primes)
    
#now the numbers in possiblyValidNumbers have 9 out of 10 digits
#add the last digit
for numberIndex in range(0, len(possiblyValidNumbers)):
    for missingDigit in range(0, 10):
        if not str(missingDigit) in possiblyValidNumbers[numberIndex]: #find the digit not in the number
            possiblyValidNumbers[numberIndex] = str(missingDigit) + possiblyValidNumbers[numberIndex]
            
print possiblyValidNumbers
print sum([int(x) for x in possiblyValidNumbers])
