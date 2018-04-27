from scipy.stats import norm

mu     = 100
sigma  =  15
genius = 140

p = 1 - norm.cdf(genius, mu, sigma)
print(p)

for n in range(1, 1000):
    print(n, ":", 1 - (1 - p)**n)
