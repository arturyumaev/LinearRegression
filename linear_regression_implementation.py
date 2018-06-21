import numpy as np
from matplotlib import pyplot as plt
import random

def viz(x, y, a=None, b=None):
    plt.grid(True)
    plt.plot(x, y, "o")
    if ((a != None) and (b != None)):
        plt.plot(x, x * a + b, "r")
    plt.xlabel("x")
    plt.ylabel("y = f(x)")
    plt.show()
    
def f(x):
    return np.array([i - np.cos(2 * i) + random.randint(-10, 5) for i in x])

def get_w(x, y):

    X = np.ones((x.shape[0], 2))
    X[:, 0] = x
    y = y.reshape((-1 ,1))

    dot1 = np.dot(X.T, X)
    inv = np.linalg.inv(dot1)
    dot2 = np.dot(inv, X.T)
    dot3 = np.dot(dot2, y)

    a = dot3[0][0]
    b = dot3[1][0]

    return a, b

x = np.linspace(-10, 10, 50)
y = f(x)
a, b = get_w(x, y)
viz(x, y, a, b)
