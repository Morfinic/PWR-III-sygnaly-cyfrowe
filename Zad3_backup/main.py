import matplotlib.pyplot as plt
from PIL import Image
import math
import include.interpolate
import numpy as np


@include.interpolate.time_it
def resize_image(image, k):
    imageLength = image.size[0]
    newLength = int(imageLength * k)
    newImage = Image.new("RGB", (newLength, newLength))

    for x in range(newLength):
        for y in range(newLength):
            oldX = int(x / k)
            oldY = int(y / k)
            oldPixel = image.getpixel((oldX, oldY))

            newImage.putpixel((x, y), oldPixel)

    return newImage


@include.interpolate.time_it
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


imgOriginal = Image.open(r"./img/blad_runner.png")
scaledDownImage = resize_image(imgOriginal, 0.5)
scaledUpImage = resize_image(scaledDownImage, 4)
angle = 45
# 36 231 2137
rotatedImage = rotate_image(imgOriginal, angle)

contentList = [
    [imgOriginal, "Original_image"],
    [scaledDownImage, f"Scaled_down_{scaledDownImage.size[0]}"],
    [scaledUpImage, f"Scaled_up_{scaledUpImage.size[0]}"],
    [rotatedImage, f"Rotated_by_{angle}"],
]

interList = [
    [include.interpolate.nearest(rotatedImage), "Nearest interpolation"],
    [include.interpolate.bilinear(rotatedImage), "Bilinear interpolation"],
    [include.interpolate.bicupic(rotatedImage), "Bicubic interpolation"],
]

for idx, img in enumerate(contentList, 1):
    image, name = img
    plt.subplot(140 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    image.save(f"./imgSaved/{name}.png", "PNG")
plt.show()

for idx, img in enumerate(interList, 1):
    image, name = img
    plt.subplot(130 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    plt.imsave(f"./imgSaved/{name}.png", image.astype(np.uint8))
plt.show()
