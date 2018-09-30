import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("students_scores.csv", delimiter=',', dtype=np.float128)
X = np.array(data['X'])
y = np.array(data['y'])

alpha = 0.01
theta = [0, 0]


def gradient(X, y, theta):
    m = len(y)
    for i in range(0, 2000):
        for k in range(0, m):
            theta[0] -= alpha / m * (hypothesis(X[k], theta) - y[k])
            theta[1] -= alpha / m * (hypothesis(X[k], theta) - y[k]) * X[k]
    return theta


def hypothesis(X, theta):
    return theta[0] + X * theta[1]


th = gradient(X, y, theta)

print(th)

plt.plot(X, hypothesis(X, th))
plt.scatter(X, y)
plt.show()
