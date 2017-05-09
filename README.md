# scripts_and_math
After I decided I wanted to do CS, these are some of the things I played around with for a couple of months.

## Mandelbrot_Set
#### MandelbrotExplorer.py
A UI where the user can zoom in on the Mandelbrot Set and save an image to file.
#### Mandelbrot.py
Generates an image of the Mandelbrot set and saves it to file with a unique filename.
#### ./img
Some cool images I generated with these.

## scripts
#### XKCDWallpaper*.py
A hack to easily change your windows wallpaper. Downloads an XKCD comic, (puts it on top of a neat gradient background), and saves it in your C:/Users/Public folder twice. All you have to do is set your wallpaper to slideshow between those two images, and then if you run the script again, it changes the images, and when the slideshow changes, your wallpaper changes.
#### FunctionMinimizer.py
A python script that minimizes a function by writing *another python script*. I was curious whether python could do this, and the answer is yes!

## Chaotic_Pendulum
#### SimplePendulum.py
A simulation of a simple pendulum.
#### DoublePendulum.py
A draggable simulation of a double pendulum. (This is how I learned about the Lagrangian! if you care)
#### PhysicalDoublePendulum.py
A simulation of a 'physical' double pendulum (i.e. with solid bars)
#### CircleRotation.py
What happens if you replace a line with a circle.

## math
#### analyzeABC.py
The solution to a Capture the Flag. Generates flag.png from abc.txt.
#### DivisiblePandigital.py
Finds all 0 to 9 pandigital numbers such that 17 (the 7th prime) divides (digit8),(digit9),(digit10) 13|d7d8d9, 11|d6d7d8, etc.
###
ex: 4160357289 ==> 17 divides 289, 13|728, 11|572, 7|357, 5|035, 3|603, and 2|160
#### PathfindingChallenge.py
Uses Djikstra's Algoriithm to find the highest-valued path through a triangle of numbers.
#### PrimeSumFinder.py
Prints the prime less than 1,000,000 that can be written as the longest sequence of consecutive primes.
#### calendarLib.py
Calculates the day of the week, the number of days since 3-10-17, and what the most recent XKCD comic number is.
#### permLib.py
Generates all permutations of a entire set and all n-combinations of a set.
#### primeLib.py
Checks if a number is prime, saves a list of primes less than n to file, and reads such a file into a list.
