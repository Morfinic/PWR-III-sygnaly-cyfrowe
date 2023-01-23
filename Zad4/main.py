import numpy as np
import matplotlib.pyplot as plt
import cv2
from include.noise_filters import mean_filter, median_filter

imgNoNoise = plt.imread("pics/Leopard-1.jpg")
imgNoise = plt.imread("pics/Leopard-with-noise.jpg")
diff = np.abs(imgNoNoise - imgNoise)
medianNoiseRemove = median_filter(imgNoise)
medianFilterDiff = np.abs(imgNoise - medianNoiseRemove)
meanNoiseRemove = mean_filter(imgNoise, 5)
meanFilterDiff = np.abs(imgNoise - meanNoiseRemove)

imgSet = [
    [imgNoNoise, imgNoise, diff], 
    [medianNoiseRemove, medianFilterDiff],
    [meanNoiseRemove, meanFilterDiff]
    ]
titles = [
    ["Leopard", "Leopard_with_noise", "Diff"], 
    ["median_filter", "diff_median_filter"],
    ["mean_filter", "diff_mean_filter"]
    ]

for i in range(0, len(imgSet)):
    for j in range(0, len(imgSet[i])):
        plt.subplot(1, len(imgSet[i]), j + 1)
        plt.imshow(imgSet[i][j])
        plt.axis("off")
        plt.title(titles[i][j])
    plt.show()

plt.subplot(141)
plt.imshow(imgNoNoise)
plt.subplot(142)
plt.imshow(imgNoise)
plt.subplot(143)
plt.imshow(medianNoiseRemove)
plt.subplot(144)
plt.imshow(meanNoiseRemove)
plt.show()