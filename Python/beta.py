import matplotlib.pyplot as plt 
import numpy             as np
from scipy.special import gamma

def choose(n, k):
    "compute n choose k"
    if k < 0 or n < k:
        return 0
    if k > n - k:
        k = n - k
    result = frc.Fraction(1)
    for i in range(0, k):
        result *= (n - i)
    for i in range(1, k+1):
        result /= i
    return result

def beta(a, b, x):
    c = gamma(a) * gamma(b) / gamma(a + b)
    return gamma(a+b) / (gamma(a) * gamma(b)) * x**(a-1) * (1 - x)**(b-1)

def plotBeta(a, b):
    n = 100
    x = np.linspace(0.01, 0.99, num = n)
    y = beta(a, b, x)
    z = np.zeros((n,1))
    plt.margins(0.05)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Beta(" + str(a) + ", " + str(b) + ")")
    plt.show()
    
plotBeta(2.0, 2.0)
plotBeta(1.0, 1.0)
plotBeta(2.0, 1.0)
plotBeta(1.0, 2.0)
plotBeta(0.5, 0.5)
plotBeta(2.0, 5.0)
plotBeta(6.0, 6.0)

    

