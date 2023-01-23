import math
import numpy as np
from include.time_it import time_it


@time_it
def resize_nearest(image, k: int):
    baseSize = image.shape[0]
    newSize = int(baseSize * k)
    newImage = np.zeros((newSize, newSize, 3))

    for x in range(newSize):
        for y in range(newSize):
            oldX = int(np.round(x / k))
            oldY = int(np.round(y / k))

            if oldX >= baseSize:
                oldX = baseSize - 1
            if oldY >= baseSize:
                oldY = baseSize - 1

            newImage[x, y] = image[oldX, oldY]

    return newImage


# Ojcze nasz, zadziałaj
@time_it
def resize_bilinear(image, k: int):
    baseSize = image.shape[0]
    newSize = int(baseSize * k)
    newImage = np.zeros((newSize, newSize, 3))

    for i in range(newSize):
        for j in range(newSize):
            orig_i, orig_j = i / k, j / k
            i_int, j_int = int(orig_i), int(orig_j)
            i_frac, j_frac = orig_i - i_int, orig_j - j_int

            if (
                i_int >= 0
                and i_int < baseSize - 1
                and j_int >= 0
                and j_int < baseSize - 1
            ):
                p = (
                    (1 - i_frac) * (1 - j_frac) * image[i_int, j_int]
                    + i_frac * (1 - j_frac) * image[i_int + 1, j_int]
                    + (1 - i_frac) * j_frac * image[i_int, j_int + 1]
                    + i_frac * j_frac * image[i_int + 1, j_int + 1]
                )
            else:
                p = image[i_int, j_int]

            newImage[i, j] = p

    return newImage


@time_it
def rotate_image(image, angle: int):
    # Obliczanie zmiennych do czytelniejszych oblczeń
    angle = math.radians(angle)
    sin = math.sin(angle)
    cos = math.cos(angle)
    width, height, dim = image.shape
    # Liczenie danych nowego rozmiaru
    # Rozmiar
    newWidth = round(abs(width * cos) + abs(height * sin)) + 1
    newHeight = round(abs(height * cos) + abs(width * sin)) + 1
    # Środek oryginalnego zdjęcia
    centerOgW = round(((height + 1) / 2) - 1)
    centerOgH = round(((width + 1) / 2) - 1)
    # Środek nowego zdjęcia
    centerNewH = round(((newHeight + 1) / 2) - 1)
    centerNewW = round(((newWidth + 1) / 2) - 1)
    # Tworzenie zdjęcia o nowych rozmiarach
    rotatedImage = np.zeros((newWidth, newHeight, dim))

    for x in range(width):
        for y in range(height):
            yOg = width - 1 - x - centerOgH
            xOg = height - 1 - y - centerOgW

            yNew = centerNewH - round(xOg * sin + yOg * cos)
            xNew = centerNewW - round(xOg * cos - yOg * sin)

            if 0 <= xNew < newWidth and 0 <= yNew < newHeight:
                rotatedImage[yNew, xNew] = image[y, x]

    return rotatedImage
