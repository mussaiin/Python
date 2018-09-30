import numpy
import matplotlib.pyplot as plot

s = numpy.loadtxt('iris.data', delimiter=',', dtype=str)

x = s[:, 0]
y = s[:, 2]
c = []
for i in s[:, 4]:
    if i == 'Iris-setosa':
        c.append('red')
    elif i == 'Iris-versicolor':
        c.append('blue')
    else:
        c.append('black')

plot.scatter(x, y, c=c)
plot.show()
