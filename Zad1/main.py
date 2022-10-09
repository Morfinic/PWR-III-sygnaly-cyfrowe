import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(121, projection = "polar")
ax2 = fig.add_subplot(122)
ax2.set_xlim([-1.5, 1.5])
ax2.set_ylim([-1.5, 1.5])

n = 5
radians = np.linspace(0, 2*np.pi, 256)
frames = np.linspace(-32, 32, 64)

while True:
    for frame in frames:
        for rad in radians:
            radius = np.sin(n*rad + (frame*np.pi)/10)
            x=np.cos(rad)*radius
            y=np.sin(rad)*radius

            ax1.plot(rad, radius, "o")
            ax2.plot(x, y, "*")
        plt.pause(0.1)
        ax1.clear()
        ax2.clear()

