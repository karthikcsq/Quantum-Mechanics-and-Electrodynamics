import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def P(L, E):
    theta = 1.20428 # radians
    mass_diff = 8 * 10**(-5)
    hc = 1.23984193 * 10**(-6) # eV
    P = np.square(np.sin(theta)) * np.square(np.sin(mass_diff * L * np.pi / (2*E*hc)))
    return P

def f(E):
    return 1/(4*10**6)

def P_spectrum(L, E1, E2):
    # Integrate over the probability function
    # From E1 to E2
    # Return the result
    x = np.linspace(E2, E1, 1000)
    integrals = np.array([integrate.simps((1-P(L_i, x))*f(x), x) for L_i in L])
    return integrals

# Graph the probability of oscillation as a function of distance
# From 10^3 to 10^7 in logspace


L = np.logspace(3, 7, 1000)
E1 = 8 * 10**6 # eV
E2 = 4 * 10**6 # eV
P1 = P(L, E1)
P2 = P(L, E2)
# Round to 4 decimal places
P1 = np.round(P1, 5)
P2 = np.round(P2, 5)
# fig = plt.figure(figsize=(20, 4))
# ax = fig.add_subplot(111)
# ax.set_xlabel('Distance (m)')
# ax.set_ylabel('Probability')
# ax.set_title('Probability of Oscillation')
# ax.set_xscale('log')
# ax.set_xlim(10**3, 10**7)
# plt.plot(L, P1)
# plt.plot(L, P2)

# Graph the probability spectrum of oscillation as a function of energy
# From 10^3 to 10^7 in logspace
P_spec = P_spectrum(L, E1, E2)
fig = plt.figure(figsize=(20, 4))
ax = fig.add_subplot(111)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Probability')
ax.set_title('Probability spectrum of Oscillation')
ax.set_xscale('log')
ax.set_xlim(10**3, 10**7)
plt.plot(L, P_spec)

plt.show()



