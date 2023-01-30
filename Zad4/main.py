import numpy as np
import matplotlib.pyplot as plt
from include.noise_filters import mean_filter, median_filter
from cv2 import bilateralFilter

imgNoNoise = plt.imread("pics/Leopard-1.jpg")
imgNoise = plt.imread("pics/Leopard-with-noise.jpg")
diff = np.abs(imgNoNoise - imgNoise)
medianNoiseRemove = median_filter(imgNoise)
medianFilterDiff = np.abs(imgNoNoise - medianNoiseRemove)**2
meanNoiseRemove = mean_filter(imgNoise, 5)
meanFilterDiff = np.abs(imgNoNoise - meanNoiseRemove)**2
bilateralFilterImg = bilateralFilter(imgNoise, 15, 75, 75)
bilateralDiff = np.abs(imgNoNoise - bilateralFilterImg)**2

imgSet = [
    [imgNoNoise, imgNoise, diff], 
    [medianNoiseRemove, medianFilterDiff],
    [meanNoiseRemove, meanFilterDiff],
    [bilateralFilterImg, bilateralDiff]
    ]
titles = [
    ["Leopard", "Leopard_with_noise", "Diff"], 
    ["median_filter", "diff_median_filter"],
    ["mean_filter", "diff_mean_filter"],
    ["bilateral_filter", "bilateral_diff"]
    ]

for i in range(0, len(imgSet)):
    for j in range(0, len(imgSet[i])):
        plt.subplot(1, len(imgSet[i]), j + 1)
        plt.imshow(imgSet[i][j])
        plt.axis("off")
        plt.title(titles[i][j])
        plt.imsave(f"./picSaved/{titles[i][j]}.png", imgSet[i][j])
    plt.show()

# Wyświetlenie do porównania
# plt.subplot(1, 2, 1)
# plt.imshow(imgNoise)
# plt.axis("off")
# plt.subplot(1, 2, 2)
# plt.imshow(medianNoiseRemove)
# plt.axis("off")
# plt.show()