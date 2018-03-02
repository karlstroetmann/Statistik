import matplotlib.pyplot as plt 

def propAnC(n):
    result = 1.0;
    for k in range(365 - n + 1, 365+1):
        result *= k / 365
    return result

probabilities = [0];
for n in range(2, 100):
    p = 1.0 - propAnC(n);
    probabilities += [p];
    print("n = ", n, ":", p);

n = 57
x = range(1,n)
y = [0] + [1.0 - propAnC(k) for k in range(2,n)]
markerline, stemlines, baseline = plt.stem(x, y, '-')
fifty = [0.5 for k in range(1, n+1)]
plt.plot(fifty, color = 'r')

plt.margins(0.02)
plt.xticks(range(1, n, 3))
plt.xlabel("number of persons")
plt.ylabel("probability")
plt.title("Probability of a birthday match")
plt.show()


