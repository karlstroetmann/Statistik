import matplotlib.pyplot as plt 
import numpy             as np
from scipy.special import gamma

def chiSquare(n, x):
    """
    compute the gamma distribution Gamma(a, l)

    Since lambda is a keyword in Python, it had to be abbreviated as l
    """
    An = 2 ** (n / 2) * gamma(n/2)
    return 1 / An * x ** (n/2-1) * np.exp(-x/2) 

def plotChiSquare(l, w):
    n = 1000
    x = np.linspace(0.0, w, num = n)
    z = np.zeros((n,1))
    plt.margins(0.02)
    plt.plot(x, z)
    for f in l:
        y = chiSquare(f, x)
        plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("ChiSquare Distributions: n = " + str(l))
#    plt.title("ChiSquare Distribution with 1 degree of freedom.")
    plt.show()

plotChiSquare([1], 6)
plotChiSquare([2], 10)
plotChiSquare([3,4,5,10], 18)
plotChiSquare([30], 62)
