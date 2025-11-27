import numpy as np
import matplotlib.pyplot as plt

# X(z) = (1 + 0.5z^-1) / (1 - 0.25z^-1 - 0.125z^-2)
num = [1, 0.5]             # numerator coeff
den = [1, -0.25, -0.125]   # denominator coeff

# find poles and zeros
zeros = np.roots(num)
poles = np.roots(den)
gain = num[0] / den[0]

print("Z-Transform from Transfer Function")
print(f"Numerator Coefficients (N(z)): {num}")
print(f"Denominator Coefficients (D(z)): {den}")
print(f"Zeros: {zeros}")
print(f"Poles: {poles}")
print(f"Gain: {gain}")

#From given Poles and Zeros
given_zeros = [0.2, -0.9]
given_poles = [0.8, 0.3]
gain = 1.0

# num & den from given poles and zeroes
num_poly = np.poly(given_zeros) * gain
den_poly = np.poly(given_poles)

print("\nRational Z-Transform from Given Poles and Zeros")
print(f"Given Zeros: {given_zeros}")
print(f"Given Poles: {given_poles}")
print(f"Numerator Polynomial (N(z)): {num_poly}")
print(f"Denominator Polynomial (D(z)): {den_poly}")



plt.figure(figsize=(8, 6))
# Unit circle
theta = np.linspace(0, 2*np.pi, 500)
plt.plot(np.cos(theta), np.sin(theta), 'k--', label='Unit Circle')

# Plot poles and zeros
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', s=100, label='Zeros (from TF)')

plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', s=100, label='Poles (from TF)')
plt.scatter(np.real(given_zeros), np.imag(given_zeros), marker='o', color='g', s=80, label='Given Zeros')
plt.scatter(np.real(given_poles), np.imag(given_poles), marker='x', color='m', s=80, label='Given Poles')

plt.title("Pole–Zero Plot in Z-plane")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend(loc="upper right", bbox_to_anchor=(1, 1))
plt.grid(True)
plt.axis('equal')


max_pole_mag = np.max(np.abs(poles))
print("\nROC for Z-Transform from Transfer Function")
print(f"Poles Magnitudes: {np.abs(poles)}")
print(f"ROC: |z| > {max_pole_mag:.4f} (for causal system)")

max_given_mag = np.max(np.abs(given_poles))
print("\nROC for Rational Z-Transform from Given Poles and Zeros")
print(f"Given Poles Magnitudes: {np.abs(given_poles)}")
print(f"ROC: |z| > {max_given_mag:.4f}  (for causal system)")
plt.show()