import numpy as np
import matplotlib.pyplot as plt

imgNoNoise = plt.imread("pics/Leopard-1.jpg")
imgNoise = plt.imread("pics/Leopard-with-noise.jpg")
diff = np.abs(imgNoNoise - imgNoise)

imgSet = [[imgNoNoise, imgNoise, diff]]
titles = [["Leopard", "Leopard_with_noise", "Diff"]]

for i in range(0, 1):
    for j in range(0, 3):
        plt.subplot(i + 1, 3, j + 1)
        plt.imshow(imgSet[i][j])
        plt.axis("off")
        plt.title(titles[i][j])

plt.show()
