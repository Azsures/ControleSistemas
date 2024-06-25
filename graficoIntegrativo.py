import control as ct
from matplotlib import pyplot as plt
import numpy as np

s = ct.tf('s')
P_pitch = (1.151*s + 0.1774)/(s**3 + 0.739*s**2 + 0.921*s)
Hs = 1/((0.4674/5)*s + 1)

list_of_params = []

K = np.linspace(0.1, 11, 100)
A = np.linspace(0.1, 11, 100)

Kc = (1.125)     #Kc <= 5.95 -> estavel; Kc > 5.95 -> oscilatorio (instavel)

G2 = ct.feedback(Kc * P_pitch, Hs)
t1, y1 = ct.step_response(G2)


p = ct.step_info(G2)
for i, j in p.items():
    print(f"{i}:{j:.4f}")

space = np.linspace(0.1, 6, 40, endpoint=False)
ks = []
As = []

for k in K:
    for a in A:
        G2 = ct.feedback((k*(s + a)/s) * P_pitch, Hs)
        p = ct.step_info(G2)
        if p['SteadyStateValue'] == 1 and p['SettlingTime'] <= 800 and p['RiseTime'] > 0.05:
            ks.append(k)
            As.append(a)

#for i in list_of_params:
#    print(i)

#roots = ct.root_locus(G2)
#plt.show()
plt.title("K x a")
plt.plot(ks, As, 'rx')
plt.show()

