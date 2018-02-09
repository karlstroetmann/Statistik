import matplotlib.pyplot as plt 
import fractions         as frc 

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

def bin(n, k, p):
    return choose(n, k) * p**k * (1-p)** (n-k)

def plotBinomial(n, p = 0.5):
    Pairs  = [(k, bin(n, k, p)) for k in range(n+1)]
    maxVal = max([p[1] for p in Pairs]);

    x = range(n+1)
    y = [bin(n, k, p) for k in range(n+1)]
    markerline, stemlines, baseline = plt.stem(x, y, '-')
    plt.margins(0.05)
    plt.setp(baseline, 'color', 'b', 'linewidth', 1)
    plt.xlabel("k")
    plt.ylabel("PMF")
    plt.title("Bin(" + str(n) + ", " + str(p) + ")")
    plt.show()

plotBinomial(10,  1/2)
plotBinomial(10,  1/3)
plotBinomial(10,  1/9)
plotBinomial(100, 1/2)
plotBinomial(100, 1/3)
plotBinomial(100, 1/9)
