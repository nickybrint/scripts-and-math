import time
import random

def functionMinimizer():
    '''
        Minimizes a function of n arguments on a discrete range
        Prints the minimum value, and the corresponding arguments
    '''
    
    file = open("code.py", "w")
    metric = raw_input("\nEnter the function you want to minimize as a python expression." +
                       "\nUse single lower-case letters (i.e. 'x', 'a') as your parameters." +
                       "\nEx: 2*b + 5 / sin(q)\n")
    rawRange = raw_input("\nEnter the inclusive discrete interval 'a,b' you want to search: ")
    RANGE_MIN = int(rawRange.split(',')[0])
    RANGE_MAX = int(rawRange.split(',')[1]) + 1
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uniqueParameters = []
    for charIndex in range(0, len(metric)):
        if metric[charIndex] in alphabet:
            if charIndex != 0 and charIndex != len(metric) - 1:
                if (not metric[charIndex - 1] in alphabet) and (not metric[charIndex + 1] in alphabet):
                    if not metric[charIndex] in uniqueParameters:
                        uniqueParameters.append(metric[charIndex])
            elif charIndex == 0 and charIndex != len(metric) - 1:
                if (not metric[charIndex + 1] in alphabet):
                    if not metric[charIndex] in uniqueParameters:
                        uniqueParameters.append(metric[charIndex])
            elif charIndex != 0 and charIndex == len(metric) - 1:
                if (not metric[charIndex - 1] in alphabet):
                    if not metric[charIndex] in uniqueParameters:
                        uniqueParameters.append(metric[charIndex])
            else:
                uniqueParameters.append(metric[charIndex])


    file.write("from math import *\ndef f(list): \n")
    file.write("\t(")
    for p in uniqueParameters:
        file.write(p + ",")
    file.write(") = list\n")
    file.write("\treturn " + metric)
    file.close()
    time.sleep(0.3)
    import code

    set = range(RANGE_MIN, RANGE_MAX)
    allArgs = []

    def recursion(allArgs, currentArg, numberOfParameters, depth, set):
        if depth == numberOfParameters:
            allArgs.append(currentArg[1:])
            return
        for i in set:
            newCurrentArg = [x for x in currentArg]
            newCurrentArg.append(i)
            recursion(allArgs, newCurrentArg, numberOfParameters, depth + 1, set)

    if len(uniqueParameters) != 1:
        recursion(allArgs, [-1], len(uniqueParameters), 0, set)
    else:
        for i in set:
            allArgs.append([i])
  
    minValue = code.f(allArgs[0])
    minArgs = allArgs[0]
    for args in allArgs[1:]:
        currentValue = code.f([float(x) for x in args])
        if currentValue < minValue:
            minValue = currentValue
            minArgs = args
    print '\nThe Minumum:\n'
    for i in range(0, len(uniqueParameters)):
        print uniqueParameters[i], "=", minArgs[i]
    print "f(",
    for a in minArgs:
        print str(a) + ",",
    print ") = " + str(minValue)

    
functionMinimizer()
raw_input("Press ENTER to exit")
