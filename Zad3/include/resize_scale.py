from PIL import Image
import math
import numpy as np
from include.time_it import time_it

@time_it
def resize_nearest(image, k):
    baseSize = image.size[0]
    newSize = int(baseSize * k)
    newImage = Image.new("RGB", (newSize, newSize))

    for x in range(newSize):
        for y in range(newSize):
            oldX = int(np.round(x / k))
            oldY = int(np.round(y / k))


            if oldX >= baseSize:
                oldX = baseSize - 1
            if oldY >= baseSize:
                oldY = baseSize - 1

            pixel = image.getpixel((oldX, oldY))
            newImage.putpixel((x, y), pixel)

    return newImage

# Ojcze nasz któryś jest w niebie, święć się imie twoje, przyjdź królestwo twoje
@time_it
def resize_bilinear(image, k):
    baseSize = image.shape[0]
    newSize = int(baseSize * k)
    newImage = np.zeros((newSize, newSize, 3))

    for i in range(newSize):
        for j in range(newSize):
            orig_i, orig_j = i / k, j / k
            i_int, j_int = int(orig_i), int(orig_j)
            i_frac, j_frac = orig_i - i_int, orig_j - j_int

            if i_int >= 0 and i_int < baseSize - 1 and j_int >= 0 and j_int < baseSize - 1:
                p = (1 - i_frac) * (1 - j_frac) * image[i_int, j_int] + \
                    i_frac * (1 - j_frac) * image[i_int + 1, j_int] + \
                    (1 - i_frac) * j_frac * image[i_int, j_int + 1] + \
                    i_frac * j_frac * image[i_int + 1, j_int + 1]
            else:
                p = image[i_int, j_int]
            
            newImage[i, j] = p
    
    return newImage

@time_it
def rotate_image(image, angle):
    angle = math.radians(angle)
    sin = math.sin(angle)
    cos = math.cos(angle)
    width, height = image.size
    center = (width / 2, height / 2)
    rotatedImage = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            newX = (x - center[0]) * cos - (y - center[1]) * sin + center[0]
            newY = (x - center[0]) * sin + (y - center[1]) * cos + center[1]

            if newX >= 0 and newX < width and newY >= 0 and newY < height:
                rotatedImage.putpixel((int(newX), int(newY)), image.getpixel((x, y)))

    return rotatedImage

