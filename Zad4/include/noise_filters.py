import numpy as np

def bounds_check(x, y, size):
    if 0 <= x < size and 0 <= y < size:
        return True
    return False

def mean_filter(input, kernelSize):
    size = input.shape[0]
    result = np.zeros_like(input)

    for x in range(size):
        for y in range(size):
            for layer in range(3):
                tmp = list()

                for i in range(-(kernelSize // 2), (kernelSize // 2) + 1):
                    for j in range(-(kernelSize // 2), (kernelSize // 2) + 1):
                        if bounds_check(x + i, y + j, size):
                            tmp.append(input[x + i][y + j][layer])

                result[x][y][layer] = np.mean(tmp)

    return result

def median_filter(input):
    size = input.shape[0]
    result = np.zeros_like(input)

    pixelMatrix = [
        [-1, 1], [0, 1], [1, 1],
        [-1, 0], [0, 0], [1, 0],
        [-1, -1], [0, -1], [1, -1]
    ]

    for x in range(size):
        for y in range(size):
            for layer in range(3):
                tmp = list()

                for i, j in pixelMatrix:
                    if bounds_check(x + i, y + j, size):
                        tmp.append(input[x + i][y + j][layer])

                result[x][y][layer] = np.median(tmp)

    return result

def bilateral_filter(input):
    pass
