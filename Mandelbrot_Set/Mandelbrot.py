from PIL import Image

maxiterations = 50
width, height = 300, 300
leftx, rightx, bottomy = 0.3, 0.31, 0.025


def divergenceTest(c, MAX_ITERATIONS):

    '''
        check if a point [a, b] is in the mandelbrot set
        return the number of iterations it took to diverge
        @param c = [a, b], a complex number a + bi
    '''

    
    """
    if abs(c[0]) < 0.005 or abs(c[1]) < 0.005:
        return -2
    if c[0] % 0.1 < 0.005 or c[1] % 0.1 < 0.005:
        return -1
    """
    
    z = [0, 0]
    iterations = 0
    while abs(z[0]) < 4 and abs(z[1]) < 4 and iterations < MAX_ITERATIONS:
        z = [z[0]**2 - z[1]**2 + c[0], 2*z[0]*z[1] + c[1]]
        iterations += 1
    return iterations

def fillMandelbrot(image, MAX_ITERATIONS, LEFT_X, BOTTOM_Y, RIGHT_X, PIXEL_WIDTH, IMAGE_HEIGHT, IMAGE_WIDTH):
    '''
        fills a PIL Image with the mandelbrot set on the given range
    '''
    
    for x in range(0, IMAGE_WIDTH):
        for y in range(1, IMAGE_HEIGHT + 1):
            c = [x*PIXEL_WIDTH + LEFT_X, y*PIXEL_WIDTH + BOTTOM_Y]
            iterations = divergenceTest(c, MAX_ITERATIONS)
            
            color = (0,0,0)
            if iterations < MAX_ITERATIONS:
                color = (int(iterations*(255/MAX_ITERATIONS)), int(iterations*(255/MAX_ITERATIONS)), 200)
            '''
            if iterations == -1:
                color = (255, 255, 255)
            if iterations == -2:
                color = (255, 0, 0)
            '''
            
            image.putpixel((x, IMAGE_HEIGHT - y), color)


def doRegistry():
    '''
        reads from registry.txt, which contains the last image id
        returns last image id + 1, which is the current image id
        increments the id in registry.txt
    '''
    f = open('registry.txt', 'w+')
    lines = f.readlines()
    imageNumber = ''
    if lines == []:
        imageNumber = '0'
    else:
        imageNumber = lines[0]
    f.close()
    f = open('registry.txt', 'w+')
    newImageNumber = int(imageNumber) + 1
    f.write(str(newImageNumber))
    f.close()
    return newImageNumber


def main(LEFT_X, RIGHT_X, BOTTOM_Y, IMAGE_HEIGHT, IMAGE_WIDTH, MAX_ITERATIONS):
    '''
        returns a png of the mangelbrot set
    '''
    PIXEL_WIDTH = (RIGHT_X - LEFT_X)/IMAGE_WIDTH
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), 0)
    fillMandelbrot(image, MAX_ITERATIONS, LEFT_X, BOTTOM_Y, RIGHT_X, PIXEL_WIDTH, IMAGE_HEIGHT, IMAGE_WIDTH)
    return image


if __name__ == "__main__":
    image = main(leftx, rightx, bottomy, height, width, maxiterations)
    imageID = doRegistry()
    image.save('mandelbrot' + str(imageID) + '.jpg')
    image.show()

