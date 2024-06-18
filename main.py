import multiprocessing.pool
import control as ct
from matplotlib import pyplot as plt
import numpy as np
import multiprocessing

s = ct.tf('s')
P_pitch = (1.151*s + 0.1774)/(s**3 + 0.739*s**2 + 0.921*s)
Hs = 1/((0.4674/5)*s + 1)


Kc = (1.125)     #Kc <= 5.95 -> estavel; Kc > 5.95 -> oscilatorio (instavel)

G2 = ct.feedback(Kc * P_pitch, Hs)
t1, y1 = ct.step_response(G2)
t2, y2 = ct.step_response(Kc * P_pitch + Hs)

print(f"error in open loop: {100*(1 - y2[-1]):.2f}%")
print(f"error in closed loop: {100*(1 - y1[-1]):.2f}%")
print(G2)
print(ct.zeros(G2))
print(ct.poles(G2))
roots = ct.root_locus(G2)

s = ct.step_info(G2)
print("\n========================")
for i, j in s.items():
    print(f"{i}:{j:.4f}")


plt.show()

plt.plot(t1, y1)
plt.show()
'''
plt.plot(t2, y2)
plt.show()
'''
