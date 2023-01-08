import numpy as np
import matplotlib.pyplot as plt
import cv2
from demosaic import demosaic

rawImage = cv2.cvtColor(cv2.imread("img/strus.bmp", cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
xTransImage = np.zeros([*rawImage.shape], dtype=int)

content_list = [
    [rawImage, "Raw Image"],
    [xTransImage, "X-Trans Filter"],
]

# Red
xTransImage[0::6, 2::6, 0] = rawImage[0::6, 2::6, 0]
xTransImage[0::6, 4::6, 0] = rawImage[0::6, 4::6, 0]
xTransImage[1::6, 0::6, 0] = rawImage[1::6, 0::6, 0]
xTransImage[2::6, 3::6, 0] = rawImage[2::6, 3::6, 0]
xTransImage[3::6, 1::6, 0] = rawImage[3::6, 1::6, 0]
xTransImage[3::6, 5::6, 0] = rawImage[3::6, 5::6, 0]
xTransImage[4::6, 3::6, 0] = rawImage[4::6, 3::6, 0]
xTransImage[5::6, 0::6, 0] = rawImage[5::6, 0::6, 0]

# Green
xTransImage[0::3, 0::3, 1] = rawImage[0::3, 0::3, 1]
xTransImage[1::3, 1::3, 1] = rawImage[1::3, 1::3, 1]
xTransImage[1::3, 2::3, 1] = rawImage[1::3, 2::3, 1]
xTransImage[2::3, 1::3, 1] = rawImage[2::3, 1::3, 1]
xTransImage[2::3, 2::3, 1] = rawImage[2::3, 2::3, 1]

# Blue
xTransImage[0::6, 1::6, 2] = rawImage[0::6, 0::6, 2]
xTransImage[0::6, 5::6, 2] = rawImage[0::6, 5::6, 2]
xTransImage[1::6, 3::6, 2] = rawImage[1::6, 3::6, 2]
xTransImage[2::6, 0::6, 2] = rawImage[2::6, 0::6, 2]
xTransImage[3::6, 2::6, 2] = rawImage[3::6, 2::6, 2]
xTransImage[3::6, 4::6, 2] = rawImage[3::6, 4::6, 2]
xTransImage[4::6, 0::6, 2] = rawImage[4::6, 0::6, 2]
xTransImage[5::6, 3::6, 2] = rawImage[5::6, 3::6, 2]

demosaicImage = demosaic(xTransImage, *xTransImage.shape)

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