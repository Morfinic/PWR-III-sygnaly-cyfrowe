import matplotlib.pyplot as plt
import include.interpolate as missPixels
import include.resize_scale as res_n_scale
from PIL import Image
import numpy as np

imgOriginal = Image.open(r"./img/blad_runner.png")
imgOriginalForBilinearScaling = plt.imread(r"./img/blad_runner.png")
angle = 45
rotatedImage = res_n_scale.rotate_image(imgOriginal, angle)

contentList = [
    [imgOriginal, "Original_image"],
    [rotatedImage, f"Rotated_by_{angle}"],
]

scaledDownImage = res_n_scale.resize_nearest(imgOriginal, 0.5)
scaledUpImage = res_n_scale.resize_nearest(scaledDownImage, 4)

nearScale = [
    [scaledDownImage, f"Scaled_down_near{scaledDownImage.size[0]}"],
    [scaledUpImage, f"Scaled_up_near{scaledUpImage.size[0]}"],
]

scaledDownImageBilinear = res_n_scale.resize_bilinear(imgOriginalForBilinearScaling, 0.5)
scaledUpImageBilinear = res_n_scale.resize_bilinear(scaledDownImageBilinear, 4)

bilinearScale = [
    [scaledDownImageBilinear, f"Scaled_down_bili{scaledDownImageBilinear.shape[0]}"],
    [scaledUpImageBilinear, f"Scaled_up_bili{scaledUpImageBilinear.shape[0]}"],
]
rotateList = [
    [missPixels.nearest(rotatedImage), "Nearest_interpolation"],
    [missPixels.bilinear(rotatedImage), "Bilinear_interpolation"],
    [missPixels.bicupic(rotatedImage), "Bicubic_interpolation"],
]

for idx, img in enumerate(contentList, 1):
    image, name = img
    plt.subplot(120 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    image.save(f"./imgSaved/{name}.png", "PNG")
plt.show()

for idx, img in enumerate(nearScale, 1):
    image, name = img
    plt.subplot(120 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    image.save(f"./imgSaved/{name}.png", "PNG")
plt.show()

for idx, img in enumerate(bilinearScale, 1):
    image, name = img
    plt.subplot(120 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    plt.imsave(f"./imgSaved/{name}.png", image)
plt.show()

for idx, img in enumerate(rotateList, 1):
    image, name = img
    plt.subplot(130 + idx)
    plt.title(str(name))
    plt.imshow(image)
    plt.axis("off")
    plt.imsave(f"./imgSaved/{name}.png", image.astype(np.uint8))
plt.show()
