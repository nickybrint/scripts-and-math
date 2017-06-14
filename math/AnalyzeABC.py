#This script solves this CTF (Capture-the-Flag) puzzle I was doing
#Flag is hidden in 'abc.txt'
from PIL import Image

arrayLen = 528601
width = 929         #528601 has only two prime factors, 929 and 569; these must then be the dimensions of the image
height = arrayLen / width #i.e. 569

#create a list of all the rgb values in the file
f = open('abc.txt')
line = f.readlines()[0]
rgbStrings = line.split('), (')
rgbStrings[0] = "255, 255, 255"
rgbStrings[arrayLen - 1] = "255, 255, 255"


#convert the list from strings to int tuples
rgbTuples = []
n = 0
for rgbString in rgbStrings:
    rgbTriple = rgbString.split(", ")
    i = 0
    for value in rgbTriple:
        rgbTriple[i] = int(value)
        i += 1
    rgbTuples.append(tuple(rgbTriple))
    n += 1

#print an image with the rgb values
image = Image.new('RGB', (width, height), 0) #create blank image
x = 0
y = 0
for rgbTuple in rgbTuples:
    image.putpixel((x, y), rgbTuple)
    x += 1
    if x >= width: #if reached the end of a row, move to the next
        x = 0
        y += 1
        
image.save('flag.png')
image.show()
