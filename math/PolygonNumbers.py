"""
A solution to the following problem:

Find the 6-cycle of 4-digit numbers such that:
- The last two digits of the nth number are the first two
  digits of the n+1th number, and the last two digits of
  the last number are the first two digits of the first number

- One number is triangular, one is square, one is pentagonal,
  one is hexagonal, one is heptagonal, and one is octagonal
  (they don't have to be in order)

Definitions:
- triangular      lambda x: x*(x + 1)/2
- square          lambda x: x*x
- pentagonal      lambda x: x*(3*x - 1)/2
- hexagonal       lambda x: x*(2*x - 1)
- heptagonal      lambda x: x*(5*x - 3)/2
- octagonal       lambda x: x*(3*x - 2)

Solution:
1. Generate all the 4-digit polygon numbers (there are less than 400)
2. For each triangular number,
    a. Find all non-triangular polygonal numbers with first two digits
        equal to the triangular number's last two digits.
    b. For each of these numbers, find all "previously-unused-based"
        polygonal numbers that "fit" after it.
    c. Repeat step 2 for all of the found numbers, and continue to
        recurse until a complete set is found.

(Note: It doesn't matter that we start with triangular numbers)

"""

def isInt(number):
    """Returns whether a number is really close to a whole number"""
    
    if abs(int(number) - number) < 0.001:
        return True
    return False


def isPolygonal(number, base):
    """
    Returns whether a number is polygonal

    Parameters:
    number - the number in question
    base - 0 for triangular, 1 for square, 2 for pentagonal, etc.
    
    """
    # the inverses of the formulae listed in the description
    inverse_formulae = [
        lambda number: 1.0/2*((8*number + 1)**.5 - 1),
        lambda number: number**.5,
        lambda number: 1.0/6*((24*number + 1)**.5 + 1),
        lambda number: 1.0/4*((8*number + 1)**.5 + 1),
        lambda number: 1/10.0*((40*number + 9)**.5 + 3),
        lambda number: 1.0/3*((3*number + 1)**.5 + 1),
    ]
    
    inverse = inverse_formulae[base](number)
    if isInt(inverse):
        return True
    return False   

def format_solution(match, used_bases):
    """Nicely formats the solution into a string"""

    string = "Solution:\n"
    for index, number in enumerate(match):
        string += str(number) + ", base " + str(used_bases[index] + 3) + "\n"
    string += "Its sum is " + str(sum(match)) + "."
    return string


def extrapolate(match, used_bases, polygons, max_depth):
    """
    A recursive function that searches 'polygons' for numbers
    that "fit" onto the end of the match, then calls itself on
    each found number.

    Definitions:
    "fit": The last two digits of the last number in 'match' are
           the first two digits of the new number.

    Parameters:
    match: A valid solution to the problem so far
    used_bases: The base of each number in match
    polygons: [triangular_numbers, squares, pentagons, etc..] (a list)
    max_depth: The length of a valid match

    """
    # if match is of desired length,
    if len(match) == max_depth:
        # check if it "wraps around" (i.e. the last number "fits" on the first number)
        if match[5] % 100 == match[0] / 100:
            #This is a solution! print it.
            print format_solution(match, used_bases)

    # for each type of polygonal number
    for base, polygon in enumerate(polygons):
        # make sure it is unused
        if base in used_bases:
            continue

        # mark this type as used
        used_bases.append(base)
        # check if there are any numbers of that type that "fit"
        # on the last number in 'match'
        for p_number in polygon:
            # if it "fits" on the end of the match,
            # add it to the match, and recurse
            if (match[len(match) - 1] % 100) == p_number/100:
                match.append(p_number)
                extrapolate(match, used_bases, polygons, max_depth)
                # the number wasn't part of a valid solution
                # remove it from the match and try the next one
                match.remove(p_number)
        # we are moving on to a new base, so this one isn't used anymore
        used_bases.remove(base)


triangle_numbers = []
squares = []
pentagons = []
hexagons = []
heptagons = []
octagons = []
polygons = [triangle_numbers, squares, pentagons, hexagons, heptagons, octagons]

# generate all polygon numbers between 1,000 and 10,000
for number in range(1000, 10000):
    for base in range(0, 6):
        if isPolygonal(number, base):
            polygons[base].append(number)

# for all triangle numbers, check for valid solutions
for triangle_number in triangle_numbers:
    extrapolate([triangle_number], [0], polygons, 6)
