"""
Problem:
Find the value of n, 1 < n < 10**7, for which totient(n) is a permutation of n
and n/totient(n) is a minimum

Note:
It can be derived from Euler's equation that n/totient = product(f/f-1) for f in prime_divisors.

So to minimize n/totient:
1. no factor should be small (if 2 is a factor, then n/totient *= 2 [= 2/(2-1)]
2. there should be as few factors as possible

Also, if n is prime, totient(n) = n-1, and totient(n) can't be a permutation of n.

Solution:
We should generate numbers with two factors where both are very near sqrt(n).

"""

def is_prime(number):
    """Returns whether a number is prime"""
    if number == 1:
        return False
    for factor in range(2, int(number**.5) + 1):
        if number % factor == 0:
            return False
    return True


def generate_primes(min, max):
    """Returns a list of prime in range(min, max)"""
    primes = []
    if min <= 2:
        primes += [2]
    if min % 2 == 0:
        min += 1
    for number in range(min, max, 2):
        if is_prime(number):
            primes.append(number)
    return primes


def are_permutations(number1, number2):
    """Returns whether two numbers have the same digits"""
    if not (number1 / number2 < 10 and number2 / number1 < 10):
        return False
    number1 = list(str(number1))
    for digit in list(str(number2)):
        if digit in number1:
            number1.remove(digit)
        else:
            return False
    return True

def totient_from_factors(number, factors):
    """Returns the totient of a number from a list of its prime factors
    using Euler's formula"""
    totient = number
    for factor in factors:
        totient *= (factor - 1)
        totient /= (factor)
    return totient



import time
time1 = time.time()


exponent = 8
upper_bound = 10**exponent
root = upper_bound **.5 #store this

#this is the ideal range around the root(maximum)
primes_in_range = generate_primes(int(root/3), int(root*3))

print "Searching..."
print "Search Space:", (int(root/3), int(root*3))


#storage for current lowest ratio
lowest_ratio = 100 #dummy value

#storage for extra data
winner = []

#choose all combinations of two primes in our ideal range, low_prime <= high_prime
for index, low_prime in enumerate(primes_in_range):
    
    #if prime > sqrt(upper_bound),
    #we have exhausted the all possibilities, and we're done!
    if low_prime > root:
        break

    for high_prime in primes_in_range[index:]:
        
        n = low_prime * high_prime

        #we have exhausted the possibilites for this low_prime
        if n > upper_bound:
            break

        totient = totient_from_factors(n, [low_prime, high_prime])

        #FIRST first if n/totient(n) is a new minimum, THEN check if n, totient(n) are just a permutation
        if float(n)/totient < lowest_ratio and are_permutations(totient, n):
            
            #if so, replace winner with the new winner
            lowest_ratio = float(n)/totient
            winner = (n, (low_prime, high_prime), totient, lowest_ratio)

            

print "Solution in %f seconds" % (time.time() - time1)
print "n: %d\nfactors: %s \ntotient: %d \nn/totient: %f" % winner
