import urllib
import time
import random
from PIL import Image
import datetime
import sys

"""
This script goes to the most recent xkcd comic, downloads the image, pastes it on an image with a sweet gradient, then adds it to a folder twice
If you have no other images in this folder, and set your wallpaper to slideshow,
running this script will change your wallpaper to the new image (when the slideshow changes)
Notes:  -Has support for "large" images (which are stored differently)
        -No support for images from XKCD blog posts
"""


#panel of user settings
doGradient = True
gradientColors = [(135, 213, 50), (235, 199, 116), (186, 65, 118), (58, 179, 180)] #user colors 
gradientNodes = [(0.3,0.1), (0.1,0.4), (0.3,0.65), (0.65,0.4)] #areas where these colors are maximized



#This function pastes the image in the center of a blank image of aspect ratio 16:9
#assumes 16:9 aspect ratio
def addBorders(name, name2, gradientColors, gradientNodes, doGradient):
    im = Image.open(name) 
    w, h = im.size
    screenW, screenH = 1920/2, 1080/2 #minimum resolution of outputted image
    aspectRatio = float(screenW)/screenH
    imagePadding = 1.2                #the proportion of total screen size to max image dimension
    
    if float(w) / float(h) > aspectRatio:
        if w > screenW/1.2:
            print "This comic is BIG. The wallpaper may be a minute."
            totalSize = (int(imagePadding * w), int(imagePadding* w / aspectRatio))
        else:
            totalSize = (screenW, screenH)
    else:
        if h > screenH/1.2:
            print "This comic is BIG. The wallpaper may be a minute."
            totalSize = (int(imagePadding * h * aspectRatio), int(imagePadding * h))
        else:
            totalSize = (screenW, screenH)

    totalW, totalH = totalSize
    newim = Image.new("RGB", totalSize, (0,0,0)) #create blank "longer" image of color 0,0,0
    width, height = totalSize
    
    if doGradient:
        makeGradient(totalH, totalW, gradientColors, gradientNodes, newim)
    
    #put "im" halfway in "newim"
    newim.paste(im, ((totalW - w)/2, (totalH - h)/2)) 
    newim.save(name)
    newim.save(name2)

def makeGradient(totalH, totalW, nodeColors, nodePositions, im):
    #generate a gradient with n colors at n nodes
    progress = 10
    print "Generating gradient..."
    print "Progress: (0%)",
    for y in range(0,totalH):
        for x in range(0,totalW):
            color = [0,0,0]
            changeColor(totalH, totalW, x, y, color, nodeColors, nodePositions)
            im.putpixel((x, y), (int(color[0]), int(color[1]), int(color[2])))
            
            #do progress bar
            if 100*(y + 1)/totalH  >= progress:
                sys.stdout.write("=")
                if progress % 20 == 0:
                    sys.stdout.write("(" + str(progress) + "%)")
                progress += 10
                

    #does gradient color
def changeColor(totalH, totalW, x, y, color, nodeColors, nodes):
    #Warning: lots of math
    dists = []
    for node in nodes:
        #cartesian distance from node to (x,y)
        dist = ((x - node[0]*totalW)**2 + (y - node[1]*totalH)**2)**.5 + 100 #the 100 "smoothes" out the nodes
        dists.append(dist)

    #Here is an explanation: we want totalDist (td) such that td/d1 + td/d2 + ... = 1. Then td = 1/(1/d1 + 1/d2 + ...)    
    denominator = 0
    for distance in dists:
        denominator += 1.0/distance
    totalDist = 1.0 / denominator  
    for n in range(0,3):
        for i in range(0, len(dists)):
            color[n] += nodeColors[i][n]*(totalDist/dists[i])


def doSave(link, gradientColors, gradientNodes, doGradient):
    #saved like this to ignore jpg/png conversion issues
    #taken from http://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
    resource = urllib.urlopen(link)
    output = open("C:\Users\Public\image_01.png","wb")
    output.write(resource.read())
    output.close()
    addBorders("C:\Users\Public\image_01.png", "C:\Users\Public\image_02.png", gradientColors, gradientNodes, doGradient)
    print "\nWallpaper Set!"
    time.sleep(0.5)


def main():
    url = "https://xkcd.com/" #goes to today's XKCD
    print "Target: " + url
    site = urllib.urlopen(url).readlines() #list of each line in site's html

    #xkcd saves "large" images in a different place
    #so we need to know if it is "large"

    large = False
    for item in site:
        if "/large/" in item:
            print "Large Image!"
            large = True

    for item in site:
        if large:
            if "http://xkcd.com" in item:                                       #if it's a link
                link = item.split('"><img')[0].split('="')[1].split('">')[0]    #this is where the link is--trust me
                print "--->" + link  #this is the link to the full-size image page
                newSite = urllib.urlopen(link).readlines()
                for newItem in newSite:
                    if "http://imgs" in newItem:
                        link = newItem.split('"><')[0].split('="')[1].split('">')[0]       #this is the link to the large image
                        print "Image: " + link
                        doSave(link, gradientColors, gradientNodes, doGradient)

        elif "https://imgs" in item:                        #normal xkcd images are stored here 
            link = item[item.index("https://imgs"):]        #this is the link to the image
            print "Image: " + link,
            doSave(link, gradientColors, gradientNodes, doGradient)

main()
