import numpy as np
import matplotlib.pyplot as plt
import cv2

rawImg = cv2.imread("img/strus.bmp", cv2.IMREAD_COLOR)
cv2.cvtColor(rawImg, cv2.COLOR_BGR2RGB)
xtransImage = np.zeros([rawImg.shape[0], rawImg.shape[1], 3], dtype=int)

# Red
xtransImage[0::6, 2::6, 0] = rawImg[0::6, 2::6, 0]
xtransImage[0::6, 4::6, 0] = rawImg[0::6, 4::6, 0]
xtransImage[1::6, 0::6, 0] = rawImg[1::6, 0::6, 0]
xtransImage[2::6, 3::6, 0] = rawImg[2::6, 3::6, 0]
xtransImage[3::6, 1::6, 0] = rawImg[3::6, 1::6, 0]
xtransImage[3::6, 5::6, 0] = rawImg[3::6, 5::6, 0]
xtransImage[4::6, 3::6, 0] = rawImg[4::6, 3::6, 0]
xtransImage[5::6, 0::6, 0] = rawImg[5::6, 0::6, 0]

# Green
xtransImage[0::3, 0::3, 1] = rawImg[0::3, 0::3, 1]
xtransImage[1::3, 1::3, 1] = rawImg[1::3, 1::3, 1]
xtransImage[1::3, 2::3, 1] = rawImg[1::3, 2::3, 1]
xtransImage[2::3, 1::3, 1] = rawImg[2::3, 1::3, 1]
xtransImage[2::3, 2::3, 1] = rawImg[2::3, 2::3, 1]

# Blue
xtransImage[0::6, 1::6, 2] = rawImg[0::6, 0::6, 2]
xtransImage[0::6, 5::6, 2] = rawImg[0::6, 5::6, 2]
xtransImage[1::6, 3::6, 2] = rawImg[1::6, 3::6, 2]
xtransImage[2::6, 0::6, 2] = rawImg[2::6, 0::6, 2]
xtransImage[3::6, 2::6, 2] = rawImg[3::6, 2::6, 2]
xtransImage[3::6, 4::6, 2] = rawImg[3::6, 4::6, 2]
xtransImage[4::6, 0::6, 2] = rawImg[4::6, 0::6, 2]
xtransImage[5::6, 3::6, 2] = rawImg[5::6, 3::6, 2]

plt.imshow(xtransImage)
plt.axis("off")
plt.show()
