import matplotlib.pyplot as plt
import numpy             as np


def prop(n, s):
    """
    Compute the probability that the sum of rolling n dice yields s.    """
    return propAux(n, s)
    
def propAux(n, s):
    global cache
    value = cache[n, s]
    if value != 0:
        return value
    if s < n or 6 * n < s:
        return 0
    if n == 1:
        return 1.0/6.0
    result = sum([1.0/6.0 * propAux(n-1, s-k) for k in range(1,7)])
    cache[n, s] = result
    return result

def plotProbabilities(n):
    Pairs  = [ (s, prop(n, s)) for s in range(n, 6*n+1) ];
    maxVal = max([ p[1] for p in Pairs]);

    x = range(n, 6*n+1)
    y = [prop(n, s) for s in range(n, 6*n+1)]
    
    markerline, stemlines, baseline = plt.stem(x, y, '-')
    plt.setp(baseline, 'color', 'b', 'linewidth', 1)
    plt.xlabel("sum to roll")
    plt.ylabel("probability")
    plt.title("Probability of rolling a given sum with " + str(n) + " dice.")
    plt.show()


n = 1
while n != 0:
    cache = np.zeros((n+1, 6*n+1))
    plotProbabilities(n)
    n = int(input("What is the number of dice? "))
