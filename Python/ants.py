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

def probability(k):
    return choose(1000, k) * choose(39000, 200 - k) / choose(40000, 200)

for k in range(20):
    print(k, round(1.0 * probability(k), 6))

probabilites = [1.0 * probability(k) for k in range(15)]
zeros        = [0.0                  for k in range(15)]
plt.plot(probabilites, marker = '.', linestyle = 'none')
plt.plot(zeros, color = 'r')              
plt.margins(0.02)
plt.xlabel("number of marked ants")
plt.ylabel("probability")
plt.title("Probability of catching k marked ants")
plt.show()
