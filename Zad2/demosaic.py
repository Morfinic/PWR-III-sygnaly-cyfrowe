
import numpy as np
def demosaic(img, height, width, dim):
    tmp_array = np.zeros([height, width, dim], dtype=int)
    for layer in range(0, 3):
        for y in range(0, height):
            for x in range(0, width):
                cnt, tmp = 0, 0
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if height > j >= 0 and width > i >= 0 and img[j, i, layer] != 0:
                            cnt += 1
                            tmp += img[j, i, layer]
                try:
                    tmp_array[y, x, layer] = tmp // cnt
                except ZeroDivisionError:
                    pass
    return tmp_array
