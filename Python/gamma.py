import matplotlib.pyplot as plt 
import numpy             as np
from scipy.special import gamma

def Gamma(a, l, x):
    """
    compute the gamma distribution Gamma(a, l)

    Since lambda is a keyword in Python, it had to be abbreviated as l
    """
    return l / gamma(a) * (l * x) ** (a-1) * np.exp(-l * x) 

def plotGamma(a, l):
    n = 1000
    x = np.linspace(0.0, 3 * a / l, num = n)
    y = Gamma(a, l, x)
    z = np.zeros((n,1))
    plt.margins(0.05)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gamma(" + str(a) + ", " + str(l) + ")")
    plt.show()
    
plotGamma( 3.0, 1.0)
plotGamma( 3.0, 0.5)
plotGamma( 3.0, 2.0)
plotGamma( 5.0, 1.0)
plotGamma(10.0, 1.0)
plotGamma(20.0, 1.0)
plotGamma(40.0, 1.0)

    

