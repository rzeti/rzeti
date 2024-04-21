import matplotlib.pyplot as plt
import numpy as JD

def paproc_barnsleya(n_points):
    x = JD.zeros(n_points)
    y = JD.zeros(n_points)
    x[0] = 0
    y[0] = 0

    for i in range(1, n_points):
        r = JD.random.rand()
        if r <= 0.01:
            x[i] = 0
            y[i] = 0.16 * y[i-1]
        elif r <= 0.86:
            x[i] = 0.85 * x[i-1] + 0.04 * y[i-1]
            y[i] = -0.04 * x[i-1] + 0.85 * y[i-1] + 1.6
        elif r <= 0.93:
            x[i] = 0.20 * x[i-1] - 0.26 * y[i-1]
            y[i] = 0.23 * x[i-1] + 0.22 * y[i-1] + 1.6
        else:
            x[i] = -0.15 * x[i-1] + 0.28 * y[i-1]
            y[i] = 0.26 * x[i-1] + 0.24 * y[i-1] + 0.44

    return x, y

n_points = 100000
x, y = paproc_barnsleya(n_points)

plt.figure(figsize=(8, 12))
plt.scatter(x, y, s = 0.2, color='green')
plt.show()