import time
import random

def functionMinimizer():
    '''
        Minimizes a function of n arguments on a discrete range, and prints the minimum
        The neat part is it actually writes another python program to do this.
        Clearly this is not the best way to do this, but I think it's cool.
        
    '''
    #create a blank python file
    file = open("code.py", "w")
    
    #define the function
    metric = raw_input("\nEnter the function you want to minimize as a python expression." +
                       "\nUse single lower-case letters (i.e. 'x', 'a') as your parameters." +
                       "\nEx: 2*b + 5 / sin(q)\n")
    #define the range
    rawRange = raw_input("\nEnter the inclusive discrete interval 'a,b' you want to search: ")
    RANGE_MIN = int(rawRange.split(',')[0])
    RANGE_MAX = int(rawRange.split(',')[1]) + 1
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    #parse the function for unique variables in the alphabet
    uniqueParameters = []
    for charIndex in range(0, len(metric)):
        #if the character is a letter, check if it is surrounded by other letters
        if metric[charIndex] in alphabet:            
            #if it is not at the beginning or end of the function
            if charIndex != 0 and charIndex != len(metric) - 1:
                #check whether the next and previous characters are letters
                if (not metric[charIndex - 1] in alphabet) and (not metric[charIndex + 1] in alphabet):
                    #if both of them aren't, this is a valid single character variable
                    if not metric[charIndex] in uniqueParameters:
                        uniqueParameters.append(metric[charIndex])                        
                        
            #if char is at the beginning of the string
            elif charIndex == 0 and charIndex != len(metric) - 1:
                #check if the next character is a letter
                if (not metric[charIndex + 1] in alphabet):
                    #if so, this is a single-letter variable
                    if not metric[charIndex] in uniqueParameters:
                        uniqueParameters.append(metric[charIndex])
            
            #if char is at the end of the string
            elif charIndex != 0 and charIndex == len(metric) - 1:
                #check if previous character is a letter
                if (not metric[charIndex - 1] in alphabet):
                    #if so, this is a single-letter variable
                    if not metric[charIndex] in uniqueParameters:
                        uniqueParameters.append(metric[charIndex])
            
            #if user literally entered one character, it is a variable
            else:
                uniqueParameters.append(metric[charIndex])

    #write our new python script that is the function
    file.write("from math import *\ndef f(list): \n")
    file.write("\t(")
    for p in uniqueParameters:
        file.write(p + ",")
    file.write(") = list\n")
    file.write("\treturn " + metric)
    #save it
    file.close()
    time.sleep(0.3)   
    #open it
    import code

    #now find the minimum value on the interval
    set = range(RANGE_MIN, RANGE_MAX)
    allArgs = []
       
    def recursion(allArgs, currentArg, numberOfParameters, depth, set):
        """generate all possible sequences with length = numberOfParameters on the set"""
        #if this is our last iteration, export the sequnce
        if depth == numberOfParameters:
            allArgs.append(currentArg[1:])
            return
        
        #else generate a sequence for all possible next numbers
        for i in set:
            newCurrentArg = [x for x in currentArg]
            newCurrentArg.append(i)
            recursion(allArgs, newCurrentArg, numberOfParameters, depth + 1, set)

    #call the recursion (if we need to (i.e. len>1)
    if len(uniqueParameters) != 1:
        recursion(allArgs, [-1], len(uniqueParameters), 0, set)
    
    #all the 1-sequences are just each character from the set
    else:
        for i in set:
            allArgs.append([i])
        
    #run the function with all possible arguments and find the smallest value
    minValue = code.f(allArgs[0])
    minArgs = allArgs[0]
    for args in allArgs[1:]:
        currentValue = code.f([float(x) for x in args])
        if currentValue < minValue:
            minValue = currentValue
            minArgs = args
            
    #we succeeded with our needlessly complicated witchcraft, now tell the user the answer
    print '\nThe Minumum:\n'
    for i in range(0, len(uniqueParameters)):
        print uniqueParameters[i], "=", minArgs[i]
    print "f(",
    for a in minArgs:
        print str(a) + ",",
    print ") = " + str(minValue)

    
if __name__ == '__main__':
    functionMinimizer()
    raw_input("Press ENTER to exit") #so user can see the result
