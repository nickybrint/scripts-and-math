"""

Problem:
Find all [0-9] pandigital numbers such that 17 divides <d8><d9><d10>, 13 | d7d8d9, 11 | d6d7d8, etc.

For example, 4160357289 is valid, since
  17 divides 289, 13 | 728, 11 | 572, 7 | 357, 5 | 035, 3 | 603, and 2 | 160.


Solution:

We have to procedurally generate each valid pandigital.
(There are 10! 10-digit pandigitals--too many to search directly.)

1. Generate every 3-digit string that 17 divides. (i.e. the multiples of 17)
2. For each 3-digit string, generate 4-digit strings (no repeated digits),
    such that 13 divides the leftmost digits.
3. Continue doing this with each prime until we are out of primes.
4. There are only enough primes <= 17 for 9-digit numbers, but these numbers have to be pandigital.
    So by elimination, add the last digit. (Or we can repeat step 2, but with 1 as our prime.)

"""

def generate_next_tier(valid_strings, primes):
    """Replaces the contents of valid_strings with all valid numbers one digit longer"""

    valid_strings_copy = [x for x in valid_strings]
    del valid_strings[:]
    
    for number in valid_strings_copy:
        for left_digit in range(0, 10):

            # Check for repeated digits
            if str(left_digit) in number:
                continue
            
            last_three_digits = str(left_digit) + number[:2]
            
            # If concatentaion doesn't divide the prime, throw it out
            prime_index = len(number) - 2
            prime_to_check = primes[prime_index]
            if int(last_three_digits) % prime_to_check != 0:
                continue

            # It is valid, add it to the next tier
            new_number = str(left_digit) + number
            valid_strings.append(new_number)
                    


valid_strings = []
# Note: 1 is not prime but there are not enough primes for the leftmost three digits
primes = [17,13,11,7,5,3,2,1]

# Find all 3-digit numbers with unique digits that are divisible by first prime
# Note: 012 is the smallest of these numbers, and 987 is the largest
for a in range(0, 10):
    
    for b in range(0, 10):
        if b == a:
            continue
        
        for c in range(0, 10):
            if c == b or c == a:
                continue
            
            digits = [a, b, c]
            number = sum([d * 10**(2 - index) for index, d in enumerate(digits)])

            if number % primes[0] == 0:
                valid_strings.append(str(number))


# Expand the strings in valid_strings into all valid numbers
for p in primes[1:]:
    generate_next_tier(valid_strings, primes)

for s in valid_strings:
    print s
