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

#16input sequence
x = [1, 2, 3, 4, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1]   
N = len(x)


X = DFT(x)
x_reconstructed = IDFT(X)


n = range(N)
k = range(N)
X_mag = [abs(val) for val in X]
X_phase = [cmath.phase(val) for val in X]


plt.figure(figsize=(12, 8))

#Input Sequence
plt.subplot(2, 2, 1)
plt.stem(n, x)
plt.title("Input Sequence")
plt.xlabel("n")
plt.ylabel("Amplitude")

#DFT Magnitude Spectrum
plt.subplot(2, 2, 2)
plt.stem(k, X_mag)
plt.title("DFT Magnitude Spectrum")
plt.xlabel("k")
plt.ylabel("|X[k]|")

#DFT Phase Spectrum
plt.subplot(2, 2, 3)
plt.stem(k, X_phase)
plt.title("DFT Phase Spectrum")
plt.xlabel("k")
plt.ylabel("Phase (radians)")

#Reconstructed Sequence (IDFT)
plt.subplot(2, 2, 4)
plt.stem(n, [val.real for val in x_reconstructed])
plt.title("Reconstructed Sequence (IDFT)")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
