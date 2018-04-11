import matplotlib.pyplot as plt 
import numpy             as np

def Logistic(mu, s, x):
    """
    compute the logistic distribution Log(mu, s)
    """
    return 1 / (1 + np.exp(-(x - mu)/s)) 

def pLogistic(mu, s, x):
    """
    compute the probability density of the logistic distribution Log(mu, s)
    """
    r = np.exp(-(x - mu)/s)
    return r / (1 + r) ** 2 / s


def plotLogistic(mu, s):
    n = 1000
    x = np.linspace(-10.0, 10.0, num = n)
    y = Logistic(mu, s, x)
    p = pLogistic(mu, s, x)
    z = np.zeros((n,1))
    plt.margins(0.05)
    plt.plot(x, y)
    plt.plot(x, p)
    plt.plot(x, z)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Logistic(" + str(mu) + ", " + str(s) + ")")
    plt.show()
    
plotLogistic(0.0, 1.0)
plotLogistic(0.0, 0.5)
plotLogistic(0.0, 2.0)


    

