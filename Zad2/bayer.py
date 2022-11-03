import numpy as np
import matplotlib.pyplot as plt
import cv2

rawImg = cv2.imread("img/strus.bmp", cv2.IMREAD_COLOR)
cv2.cvtColor(rawImg, cv2.COLOR_BGR2RGB)
bayerImage = np.zeros([rawImg.shape[0], rawImg.shape[1], 3], dtype=int)

# Red
bayerImage[0::2, 1::2, 0] = rawImg[0::2, 1::2, 0]
# Green
bayerImage[0::2, 0::2, 1] = rawImg[0::2, 0::2, 1]
bayerImage[1::2, 1::2, 1] = rawImg[1::2, 1::2, 1]
# Blue
bayerImage[1::2, 0::2, 2] = rawImg[1::2, 0::2, 2]

plt.imshow(bayerImage)
plt.axis("off")
plt.show()
