import numpy as np
import matplotlib.pyplot as plt
import cv2

rawImg = cv2.imread("img/strus.bmp", cv2.IMREAD_COLOR)
cv2.cvtColor(rawImg, cv2.COLOR_BGR2RGB)
bayerImage = np.zeros([rawImg.shape[0], rawImg.shape[1], 3])

# Red
bayerImage[0::2, 1::2, 0] = rawImg[0::2, 1::2, 0]
# Green
bayerImage[0::2, 0::2, 1] = rawImg[0::2, 0::2, 1]
bayerImage[1::2, 1::2, 1] = rawImg[1::2, 1::2, 1]
# Blue
bayerImage[1::2, 0::2, 2] = rawImg[1::2, 0::2, 2]

demosaicImage = np.zeros([rawImg.shape[0], rawImg.shape[1], 3], dtype=int)

tempRed = np.pad(bayerImage[:, :, 0], 1)
tempRed[tempRed == 0] = np.nan
tempGreen = np.pad(bayerImage[:, :, 1], 1)
tempGreen[tempGreen == 0] = np.nan
tempBlue = np.pad(bayerImage[:, :, 2], 1)
tempBlue[tempBlue == 0] = np.nan

for i, layer in enumerate([tempRed, tempGreen, tempBlue]):
    for y in range(1, rawImg.shape[0] + 1, 1):
        for x in range(1, rawImg.shape[1] + 1, 1):
            # cnt = 0
            # tmp = 0

            # for i in range(x - 1, x + 2, 1):
            #     for j in range(y - 1, y + 2, 1):
            #         try:
            #             if bayerImage[j, i, layer] != 0:
            #                 cnt += 1
            #                 tmp += bayerImage[j, i, layer]
            #         except IndexError:
            #             None

            demosaicImage[y - 1, x - 1, i] = int(
                np.nanmean(layer[y - 1 : y + 2, x - 1 : x + 2])
            )

cv2.imwrite("./t.bmp", demosaicImage)

# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax2 = fig.add_subplot(122)

# ax1.imshow(bayerImage)
# ax2.imshow(demosaicImage)
# ax1.axis("off")
# ax2.axis("off")
# plt.show()
