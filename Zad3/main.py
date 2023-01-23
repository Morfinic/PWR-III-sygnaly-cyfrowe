import matplotlib.pyplot as plt
import include.interpolate as interpolate
from include.resize_scale import rotate_image, resize_nearest, resize_bilinear

imgOriginal = plt.imread(r"./img/blad_runner.png")
angle = 45
rotatedImage = rotate_image(imgOriginal, angle)
scaleDownNear = resize_nearest(imgOriginal, 0.5)
scaleUpNear = resize_nearest(scaleDownNear, 4)
scaleDownBilinear = resize_bilinear(imgOriginal, 0.5)
scaleUpBilinear = resize_bilinear(scaleDownBilinear, 4)
rotatedNear = interpolate.nearest(rotatedImage)
rotatedBilinear = interpolate.bilinear(rotatedImage)
rotatedBicubic = interpolate.bicupic(rotatedImage)

theList = (
    ((imgOriginal, "Original_image"), (rotatedImage, f"Img_rotated_by_{angle}")),
    ((scaleDownNear, f"Scaled_near_to_{scaleDownNear.shape[0]}"), (scaleUpNear, f"Scaled_near_to_{scaleUpNear.shape[0]}")),
    ((scaleDownBilinear, f"Scaled_bilinear_to_{scaleDownBilinear.shape[0]}"), (scaleUpBilinear, f"Scaled_bilinear_to_{scaleUpBilinear.shape[0]}")),
    (
        (rotatedNear, "Rotated_near"),
        (rotatedBilinear, "Rotated_Bilinear"),
        (rotatedBicubic, "Rotated_bicubic"),
    ),
)

for elem in theList:
    cnt = 1
    for img, title in elem:
        plt.subplot(1, len(elem), cnt)
        plt.title(title)
        plt.imshow(img)
        plt.axis("off")
        cnt += 1
        plt.imsave(f"./imgSaved/{title}.png", img)
    plt.show()
