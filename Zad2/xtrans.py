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

demosaicImage = np.zeros([rawImg.shape[0], rawImg.shape[1], 3], dtype=int)

for layer in range(0, 3):
    for y in range(0, rawImg.shape[0]):
        for x in range(0, rawImg.shape[1]):
            cnt = 0
            tmp = 0

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    # print(test[i, j, layer])
                    try:
                        if xtransImage[j, i, layer] != 0:
                            cnt += 1
                            tmp += xtransImage[j, i, layer]
                    except IndexError:
                        None
            demosaicImage[y, x, layer] = tmp // cnt

cv2.imwrite("./tt2.bmp", demosaicImage)

# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)

# ax1.imshow(xtransImage)
# ax2.imshow(demosaicImage)
# ax1.axis("off")
# ax2.axis("off")
# plt.show()
