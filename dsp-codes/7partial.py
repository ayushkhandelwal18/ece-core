import numpy as np
import matplotlib.pyplot as plt


def partial_fraction_manual(num, den):
    num = np.array(num, dtype=float)
    den = np.array(den, dtype=float)

    #find poles 
    poles = np.roots(den)

    #do derivative of deno
    d_den = np.polyder(den)

    #calculate residues
    residues = []
    for p in poles:
        N_val = np.polyval(num, p)
        Dp_val = np.polyval(d_den, p)
        A = N_val / Dp_val
        residues.append(A)

    return residues, poles


# X(z) = (1 + 2z^-1 + 3z^-2) / (1 - 0.5z^-1 - 0.25z^-2)
num = [1, 2, 3]
den = [1, -0.5, -0.25]

residues, poles = partial_fraction_manual(num, den)

print("\nPartial Fraction Expansion Results")
for i in range(len(residues)):
    print(f"Term {i+1}: A{i+1} = {residues[i]:.4f},   Pole p{i+1} = {poles[i]:.4f}")

#roc analysis
magnitudes = np.abs(poles)
max_radius = np.max(magnitudes)
min_radius = np.min(magnitudes)

print("\nROC Conditions")
print(f"Poles Magnitudes: {magnitudes}")
print(f"Right-sided ROC: |z| > {max_radius:.4f}")
print(f"Left-sided  ROC: |z| < {min_radius:.4f}")
print(f"Two-sided  ROC: {min_radius:.4f} < |z| < {max_radius:.4f}")


#reconstruct time-domain sequences
n = np.arange(-10, 20)

x_right = np.zeros_like(n, dtype=float)
x_left = np.zeros_like(n, dtype=float)
x_two = np.zeros_like(n, dtype=float)

for i in range(len(residues)):
    A = residues[i]
    p = poles[i]
    x_right += A * (p ** n) * (n >= 0)       # Right-sided
    x_left  += -A * (p ** n) * (n < 0)       # Left-sided
    x_two   += A * (p ** n)                  # Two-sided general



plt.figure(figsize=(11, 9))

# Pole-zero plot
plt.subplot(2,2,1)
theta = np.linspace(0,2*np.pi,400)
plt.plot(np.cos(theta), np.sin(theta), 'k--', label="Unit Circle")
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', s=120, label="Poles")
plt.scatter(np.real(residues), np.imag(residues), marker='o', color='b', s=100, label="Residues")
plt.axhline(0, color='black'); plt.axvline(0, color='black')
plt.title("Pole–Zero Plot")
plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1))
plt.grid()

#right sided
plt.subplot(2,2,2)
plt.stem(n, x_right)
plt.title("Right-sided signal (ROC: |z| > max pole)")
plt.xlabel("n"); plt.ylabel("Amplitude")

#left sided
plt.subplot(2,2,3)
plt.stem(n, x_left)
plt.title("Left-sided signal (ROC: |z| < min pole)")
plt.xlabel("n"); plt.ylabel("Amplitude")

#two sided
plt.subplot(2,2,4)
plt.stem(n, x_two)
plt.title("Two-sided signal (ROC between poles)")
plt.xlabel("n"); plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

