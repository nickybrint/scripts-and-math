#!/usr/bin/env python
from primeLib import isPrime

"""PrimeSumFinder.py: Prints the prime less than 1000000 that can be written as
the longest sequence of consecutive primes"""

def generateLongestValidList(startIndex, primes, maxLength, ceiling):
        """generate the longest valid list of primes starting at primes[startIndex]"""
        largestPrimeSum = 0
        sum = 0

        for primeIndex in range(startIndex, len(primes)):
                #add primes to the sequence until it is greater than the ceiling
                #then return the last value of its sum that was prime and longer than the max length
                sum += primes[primeIndex]
                if sum > ceiling:
                        return maxLength, largestPrimeSum
                #if the sequence is valid and longer than all previous sequences checked by the
                #entire program, then set it to be returned
                if isPrime(sum) and primeIndex - startIndex > maxLength:
                        maxLength = primeIndex - startIndex
                        largestPrimeSum = sum
                        print sum, primeIndex, startIndex


#generate primes less than ceiling
print "generating primes..."
primes = []
ceiling = 1000000
for n in range(0, ceiling):
        if isPrime(n):
                primes.append(n)
print "generated primes from 1 to", n


#find the longest string of consecutive primes whose sum is both prime and less than the ceiling
#a sequence is called 'valid' if it fits these criteria
maxLength = 0 #length of the longest valid sequence

for startIndex in range(0, len(primes)):
        print "Checking prime list starting at", primes[startIndex]
        #get the increase in the max length sum if you had started on primes[n + 1] instead of primes[n]
        nextCost  = primes[startIndex + maxLength] - primes[startIndex]
        #get the sum of the longest sequence of primes stating at startIndex that is less than the ceiling
        maxLength, sum = generateLongestValidList(startIndex, primes, maxLength, ceiling)
        #break condition
        if sum +  nextCost > ceiling:
                print "The prime less than", ceiling, ",\nwhich can be written as the longest sum of consecutive primes,\nis", sum
                break
