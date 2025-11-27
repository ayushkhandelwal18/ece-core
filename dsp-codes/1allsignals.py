import numpy as np
import matplotlib.pyplot as plt



n = np.arange(-10, 11)# Discrete time axis from -10 to 10

# Unit Step Signal u[n]
u = np.where(n >= 0, 1, 0)

# Unit Impulse δ[n]
imp = np.where(n == 0, 1, 0)

# Ramp Signal r[n]
r = np.where(n >= 0, n, 0)

# Exponential Signal e^(an)
a = 0.3
exp_pos = np.exp(a * n)     # exponential growth
exp_neg = np.exp(-a * n)    # exponential decay

# Discrete sine & cosine
Fs = 50       # Sampling frequency
f = 5         # signal frequency
n2 = np.arange(0, 50)
sin_sig = np.sin(2 * np.pi * f * n2 / Fs)
cos_sig = np.cos(2 * np.pi * f * n2 / Fs)


plt.subplot(4,2,1)
plt.stem(n, u)
plt.title("Unit Step u[n]")
plt.grid(True)

plt.subplot(4,2,2)
plt.stem(n, imp)
plt.title("Impulse δ[n]")
plt.grid(True)

plt.subplot(4,2,3)
plt.stem(n, r)
plt.title("Ramp r[n]")
plt.grid(True)

plt.subplot(4,2,4)
plt.stem(n, exp_pos)
plt.title("Exponential e^(0.3n)")
plt.grid(True)

plt.subplot(4,2,5)
plt.stem(n, exp_neg)
plt.title("Exponential e^(-0.3n)")
plt.grid(True)

plt.subplot(4,2,6)
plt.stem(n2, sin_sig)
plt.title("Discrete Sine")
plt.grid(True)

plt.subplot(4,2,7)
plt.stem(n2, cos_sig)
plt.title("Discrete Cosine")
plt.grid(True)


plt.tight_layout()
plt.show()
