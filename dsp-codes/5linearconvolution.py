import math
import cmath
import matplotlib.pyplot as plt

#find dft
def DFT(x):
    N = len(x)
    X = []
    for k in range(N):
        val = 0
        for n in range(N):
            angle = -2j * math.pi * k * n / N
            val += x[n] * cmath.exp(angle)
        X.append(val)
    return X

#find idft
def IDFT(X):
    N = len(X)
    x = []
    for n in range(N):
        val = 0
        for k in range(N):
            angle = 2j * math.pi * k * n / N
            val += X[k] * cmath.exp(angle)
        x.append(val / N)
    return x


x1 = [1, 2, 3, 4, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1]
x2 = [2, 1, 0, 1, 3, 2, 1, 0, 2, 1, 3, 4, 2, 1, 0, 1]


N = len(x1) + len(x2) - 1   

# Zero padding both sequences
x1 += [0] * (N - len(x1))
x2 += [0] * (N - len(x2))


X1 = DFT(x1)
X2 = DFT(x2)

# Multiply in f domain
Y = [X1[k] * X2[k] for k in range(N)]


y = IDFT(Y)
y_real = [val.real for val in y]


plt.figure(figsize=(12, 9))

# x1[n]
plt.subplot(3, 1, 1)
plt.stem(range(len(x1)), x1)
plt.title("Input Sequence x1[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

# x2[n]
plt.subplot(3, 1, 2)
plt.stem(range(len(x2)), x2)
plt.title("Input Sequence x2[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")

# Convolution output
plt.subplot(3, 1, 3)
plt.stem(range(len(y_real)), y_real)
plt.title("Linear Convolution of x1[n] and x2[n] using DFT")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
