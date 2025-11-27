import numpy as np
import matplotlib.pyplot as plt

#Complex Exponential
k = np.arange(0, 30) # discrete index
Fs = 50      # sampling freq
f = 5        # signal freq
w = 2 * np.pi * f / Fs
x = np.exp(1j * w * k)# complex exponential e^(jwk)

x_real = np.real(x)# Real part → cosine
x_imag = np.imag(x)# Imag part → sine

plt.subplot(2,1,1)
plt.stem(k, x_real)
plt.title("Real Part of Complex Exponential (cos(ωk))")
plt.grid(True)

plt.subplot(2,1,2)
plt.stem(k, x_imag)
plt.title("Imaginary Part of Complex Exponential (sin(ωk))")
plt.grid(True)

plt.tight_layout()
plt.show()

# ---------------- Impulse & Step Response ----------------
h1 = np.array([1, -0.5, 0.25])     # system 1
h2 = np.array([1, 1.6, 3, 2.5])    # system 2

N = 20
n = np.arange(N)  # 0 to 19 - 20 samples

# create impulse and step inputs
impulse = np.zeros(N) # impulse array with N zeroes 
impulse[0] = 1     #  make the value 1 of first element of array impulse means at 0      

step = np.ones(N)   # step array with N one    

def manual_convolution(x, h):
    Nx = len(x)
    Nh = len(h)
    Ny = Nx + Nh - 1
    y = [0] * Ny               # output array initialized with zeros

    for n in range(Ny):        # loop over output index
        total = 0
        for k in range(Nx):    # loop over input samples
            if 0 <= n-k < Nh:  # valid index check
                total += x[k] * h[n-k]
        y[n] = total
    return y

# convolution gives system response
imp_h1 = manual_convolution(impulse, h1)[:N]
step_h1 = manual_convolution(step, h1)[:N]

imp_h2 = manual_convolution(impulse, h2)[:N]
step_h2 = manual_convolution(step, h2)[:N]



plt.subplot(3,2,1)
plt.stem(h1)
plt.title("System h1[n]")

plt.subplot(3,2,2)
plt.stem(h2)
plt.title("System h2[n]")

plt.subplot(3,2,3)
plt.stem(n, imp_h1)
plt.title("Impulse Response of h1")

plt.subplot(3,2,4)
plt.stem(n, step_h1)
plt.title("Step Response of h1")

plt.subplot(3,2,5)
plt.stem(n, imp_h2)
plt.title("Impulse Response of h2")

plt.subplot(3,2,6)
plt.stem(n, step_h2)
plt.title("Step Response of h2")

plt.tight_layout()
plt.show()
