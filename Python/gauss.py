import matplotlib.pyplot as plt 
import numpy             as np
from scipy.special import gamma

def gauss(x, sigma):
    return 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x/sigma)**2/2)

def plotGauss(sigma):
    n = 400
    x = np.linspace(-4.0, 4.0, num = n)
    y = gauss(x, sigma)
    z = np.zeros((n,1))
    plt.margins(0.02)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gauss Funktion, sigma = " + str(sigma))
    plt.show()
    
plotGauss(1.0)
plotGauss(2.0)
plotGauss(0.5)

    

