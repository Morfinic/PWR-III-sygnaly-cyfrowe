import numpy as np
from include.time_it import time_it

def boundsCheck(x, y, size):
    if x >= 0 and x <= size - 1 and y >= 0 and y <= size - 1:
        return True
    return False


@time_it
def bicupic(image):
    size = image.size[0]
    image = np.array(image)
    newImage = np.zeros((size, size, 3), dtype=int)

    pixelList = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [-1, 0], [-1, 1]]

    for x in range(size):
        for y in range(size):
            for layer in range(3):
                if image[x][y][layer] != 0:
                    newImage[x][y][layer] = image[x][y][layer]
                    continue
                clrVal = 0
                clrCnt = 0
                for i, j in pixelList:
                    if (
                        boundsCheck(x + i, y + j, size)
                        and image[x + i][y + j][layer] != 0
                    ):
                        clrVal += image[x + i][y + j][layer]
                        clrCnt += 1
                if clrCnt == 0:
                    continue
                newImage[x][y][layer] = clrVal // clrCnt

    return newImage


@time_it
def bilinear(image):
    size = image.size[0]
    image = np.array(image)
    newImage = np.zeros((size, size, 3), dtype=int)

    pixelList = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    for x in range(size):
        for y in range(size):
            for layer in range(3):
                if image[x][y][layer] != 0:
                    newImage[x][y][layer] = image[x][y][layer]
                    continue
                clrVal = 0
                clrCnt = 0
                for i, j in pixelList:
                    if (
                        boundsCheck(x + i, y + j, size)
                        and image[x + i][y + j][layer] != 0
                    ):
                        clrVal += image[x + i][y + j][layer]
                        clrCnt += 1
                if clrCnt == 0:
                    continue
                newImage[x][y][layer] = clrVal // clrCnt

    return newImage


@time_it
def nearest(image):
    size = image.size[0]
    image = np.array(image)
    newImage = np.zeros((size, size, 3), dtype=int)

    for x in range(size):
        for y in range(size):
            for layer in range(3):
                if image[x][y][layer] != 0:
                    newImage[x][y][layer] = image[x][y][layer]
                    continue
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (
                            boundsCheck(x + i, y + j, size)
                            and image[x + i][y + j][layer] != 0
                        ):
                            newImage[x][y][layer] = image[x + i][y + j][layer]

    return newImage
