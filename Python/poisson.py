import matplotlib.pyplot as plt 

from math import exp
from math import ceil
#from math import max

def factorial(k):
    "compute n choose k"
    if k == 0:
        return 1
    return k * factorial(k - 1)

def poisson(k, lmbd):
    return exp(-lmbd) * lmbd**k / factorial(k)

def plotPoisson(lmbd):
    n      = max(10, 3 * ceil(lmbd))
    Pairs  = [(k, poisson(k, lmbd)) for k in range(n)]
    maxVal = max([p[1] for p in Pairs]);

    x = range(n)
    y = [poisson(k, lmbd) for k in range(n)]
    markerline, stemlines, baseline = plt.stem(x, y, '-')
    plt.margins(0.05)
    plt.setp(baseline, 'color', 'b', 'linewidth', 1)
    plt.xlabel("k")
    plt.ylabel("PMF")
    plt.title("Pois(" + str(lmbd) + ")")
    plt.show()

plotPoisson( 0.5)
plotPoisson( 1.0)
plotPoisson( 2.0)
plotPoisson( 4.0)
plotPoisson(10.0)
plotPoisson(20.0)
plotPoisson(55.0)
