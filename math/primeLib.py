#prime library
import math
def isPrime(n):
    """Returns whether a number n is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def generatePrimeList(filename, n):
    """Saves a list of primes less than n to file"""
    f = open(filename, "w")
    for number in range(0, n):
        if isPrime(number):
            f.write(str(number) + "\n")
    f.close()

def getNumbersFromFile(filename):
    """Takes a file containing "<number>\n" and returns a list of the numbers."""
    f = open(filename)
    lines = f.readlines()
    primes = []
    for line in lines:
        prime = int(line.split("\n")[0])
        primes.append(prime)
    return primes

