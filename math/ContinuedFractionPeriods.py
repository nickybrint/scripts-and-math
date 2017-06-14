"""
According to Wolfram MathWorld,
    The square root of a squarefree integer has a periodic continued fraction of the form
        sqrt(n) = [a0; a1, a2, a3, ..., a2, a1, 2*a0] (Rose 1994, pg. 130)
    where the repeating portion (excluding the last term) is symmetric upon reversal,
    and the central term may appear either once or twice.

Question:
How many periodic continued fractions of sqrt(n), n <= upper_bound have an odd period?

Solution:
1. Generate all the continued fractions n <= upper_bound.
2. Count the number with odd periods.

Algorithm to generate continued fraction expansion of sqrt(27) (~ 5.196):
1. Split sqrt(27) into its whole and fractional parts.
   sqrt(27) = 5 + sqrt(27) - 5 = 5 + 1/1/(sqrt(27) - 5)
2. Consider 1/(sqrt(27) - 5). Multiply its numerator and denominator by the conjugate (sqrt(27)+5).
   1/(sqrt(27)-5) = (sqrt(27) + 5)/([sqrt(27) + 5][sqrt(27) - 5])
3. Simplify.
   (sqrt(27) + 5)/([sqrt(27) + 5][sqrt(27) - 5]) = (sqrt(27) + 5)/(27 - 25) = (sqrt(27) + 5)/2
4. Split (sqrt(27) + 5)/2 into its whole and fractional parts.
   (sqrt(27) + 5)/2 = 5 + (sqrt(27) - 5)/2
5. Repeat steps 2-4 until (sqrt(27) - 5)/2 occurs again (this is one cycle)
   
"""
upper_bound = 10000

def root_to_continued_fraction(number):
    """Returns the continued fraction expansion of sqrt(number)"""
    root = number**(0.5)
    continued_fraction = [int(root)]
    
    previous_denominator = 1

    # stored as [root, number]
    numerator_tuple = []
    # stored as [numerator_tuple, denominator]
    past_fractions = []

    # generate the next term and check if this is the end of the cycle
    is_first_iteration = True
    while True:
        if is_first_iteration:
            numerator_tuple = [root, continued_fraction[0]]
            is_first_iteration = False
        else:
            # the new numerator is the conjugate of the old one
            numerator_tuple = [root, -numerator_tuple[1]]
            
        numerator = sum(numerator_tuple)
        denominator = (number - numerator_tuple[1]**2)/previous_denominator

        # separate the fraction into whole-number and fractional parts
        whole_number_part = 0
        # while numer/denom > 1, pull out denom/denom (= 1) and put it in front
        while numerator > denominator:
            numerator -= denominator
            numerator_tuple[1] -= denominator
            whole_number_part += 1

        # check if this is the start of a new cycle; if it is, we're done!
        if [numerator_tuple, denominator] in past_fractions:
            return continued_fraction

        # else add this to the continued fraction and prepare to repeat
        continued_fraction.append(whole_number_part)
        past_fractions.append([numerator_tuple, denominator])
        previous_denominator = denominator


# Generate all numbers whose square root is irrational
squares = [x**2 for x in range(0, 100)] # i.e. the list of numbers whose square root is rational
all_numbers = range(1, upper_bound)
for number in all_numbers:
    if number in squares:
        all_numbers.remove(number)
        
non_squares = all_numbers # i.e. the set of numbers whose square root is irrational

# Count the number of continued continued_fraction expansions that have an odd period
odd_period_count = 0
for number in non_squares:
    period_length = len(root_to_continued_fraction(number)) - 1 #the first term is not part of the cycle
    if period_length % 2 == 1:
        odd_period_count += 1
print "There are %s odd-period continued fraction expansions of sqrt(n), n <= %s." % (odd_period_count, upper_bound)
