import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math


def resize_image(image, imageLength: int, newLength: int):
    newImage = Image.new("RGB", (newLength, newLength))

    k = imageLength / newLength

    for x in range(newLength):
        for y in range(newLength):
            oldX = int(x * k)
            oldY = int(y * k)
            oldPixel = image.getpixel((oldX, oldY))

            newImage.putpixel((x, y), oldPixel)

    return newImage


def rotate_image(image, angle):
    width, height = image.size
    center = (width / 2, height / 2)
    rotatedImage = Image.new("RGB", (width, height))
    angle = angle * -1

    for x in range(width):
        for y in range(height):
            newX = (
                (x - center[0]) * math.cos(math.radians(angle))
                - (y - center[1]) * math.sin(math.radians(angle))
                + center[0]
            )
            newY = (
                (x - center[0]) * math.sin(math.radians(angle))
                + (y - center[1]) * math.cos(math.radians(angle))
                + center[1]
            )

            if newX >= 0 and newX < width and newY >= 0 and newY < height:
                rotatedImage.putpixel((int(newX), int(newY)), image.getpixel((x, y)))

    return rotatedImage


imgOriginal = Image.open(r"./img/blad_runner.png")
scaledDownImage = resize_image(imgOriginal, 512, 206)
scaledUpImage = resize_image(scaledDownImage, 206, 1024)
angle = 2137
# 36 231 2137
rotatedImage = rotate_image(imgOriginal, angle)

contentList = [
    [imgOriginal, "Original_image"],
    [scaledDownImage, "Scaled_down"],
    [scaledUpImage, "Scaled_up"],
    [rotatedImage, f"Rotated_by_{angle}"],
]

for idx, img in enumerate(contentList, 1):
    image, name = img
    plt.subplot(140 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    image.save(f"./imgSaved/{name}.png", "PNG")
plt.show()
