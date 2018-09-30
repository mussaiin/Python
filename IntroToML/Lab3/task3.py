import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.io

data = scipy.io.loadmat("digits.mat")
x = data['X']
y = data['y']
x.shape
# numExamples = x.shape[0] # 5000 examples
# numFeatures = x.shape[1] # 400 features
# numLabels = 10 # digits from 0 to 9
y.shape


def displayData(row):
    dx = x[row].reshape((20, 20)).T
    plt.imshow(dx)

displayData(4000)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y):
    m = X.shape[0]
    h = sigmoid(X * theta);
    J=(float(-1)/m)*((y.T.dot(np.log(h))) + ((1 - y.T).dot(np.log(1 - h))))
    return J

def cost_gradient(theta, X, y):
    m = X.shape[0]
    h = sigmoid(X * theta);
    grad = (float(1)/m)*((h-y).T.dot(X))
    return grad

classifiers = np.zeros(shape=(numLabels, numFeatures + 1))

X = np.ones(shape=(x.shape[0], x.shape[1] + 1))
X[:, 1:] = x