import numpy             as np
import matplotlib.pyplot as plt
import math 

def FR(x):
    g    = 9.8
    v0   = 300
    Rmax = v0 * v0 / g
    return 2 / math.pi * np.arcsin(x/Rmax)

def PR(x):
    g    = 9.8
    v0   = 300
    Rmax = v0 * v0 / g
    return 2 / (math.pi * Rmax) / np.sqrt(1 - (x/Rmax)**2)

def plotFR():
    g    = 9.8
    v0   = 300
    Rmax = v0 * v0 / g
    x    = np.linspace(0.0, Rmax, num=1000)
    y    = FR(x)
    plt.margins(0.05)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("F_R(x)")
    plt.title("Schußweite R_max = " + str(Rmax))
    plt.show()

def plotPR():
    g    = 9.8
    v0   = 300
    Rmax = v0 * v0 / g
    x    = np.linspace(0.0, Rmax * 0.99, num=1000)
    y    = PR(x)
    plt.margins(0.05)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("F_R(x)")
    plt.title("Wahrscheinlichkeits-Dichte R_max = " + str(Rmax))
    plt.show()
    
plotFR()
plotPR()
