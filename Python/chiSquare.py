import matplotlib.pyplot as plt 
import numpy             as np
from scipy.special import gamma

def Gamma(a, l, x):
    """
    compute the gamma distribution Gamma(a, l)

    Since lambda is a keyword in Python, it had to be abbreviated as l
    """
    return l / gamma(a) * (l * x) ** (a-1) * np.exp(-l * x) 

def plotChiSquare(l, w):
    n = 1000
    x = np.linspace(0.0, w, num = n)
    z = np.zeros((n,1))
    plt.margins(0.02)
    plt.plot(x, z)
    for f in l:
        y = Gamma(f/2, 2, x)
        plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("ChiSquare Distributions: n = " + str(l))
    plt.show()
    
plotChiSquare([2,3,4,5,10], 6)
plotChiSquare([3,4,5,10,30], 12)
