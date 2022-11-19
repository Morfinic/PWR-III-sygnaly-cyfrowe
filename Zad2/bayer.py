import numpy as np
import matplotlib.pyplot as plt
import cv2
from demosaic import demosaic

rawImage = cv2.cvtColor(cv2.imread("img/brisket.bmp", cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
bayerImage = np.zeros([*rawImage.shape], dtype=int)

content_list = [
    [rawImage, "Raw Image"],
    [bayerImage, "Bayer Filter"],
]

# Red
bayerImage[0::2, 1::2, 0] = rawImage[0::2, 1::2, 0]
# Green
bayerImage[0::2, 0::2, 1] = rawImage[0::2, 0::2, 1]
bayerImage[1::2, 1::2, 1] = rawImage[1::2, 1::2, 1]
# Blue
bayerImage[1::2, 0::2, 2] = rawImage[1::2, 0::2, 2]

demosaicImage = demosaic(bayerImage, *bayerImage.shape)

content_list += [
    [demosaicImage, "Demosaiced Image"],
    [np.abs(rawImage - demosaicImage), "Diff"]
]

for idx, img_c in enumerate(content_list, 1):
    img, name = img_c
    plt.subplot(140 + idx)
    plt.axis("off")
    plt.title(str(name))
    plt.imshow(img)
plt.show()
