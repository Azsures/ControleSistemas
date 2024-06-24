import control as ct
from matplotlib import pyplot as plt
import numpy as np

s = ct.tf('s')
P_pitch = (1.151*s + 0.1774)/(s**3 + 0.739*s**2 + 0.921*s)
Hs = 1/((0.4674/5)*s + 1)

list_of_params = []

K = np.linspace(0.1, 11, 100)
a = np.linspace(0.1, 11, 100)

Kc = (1.125)     #Kc <= 5.95 -> estavel; Kc > 5.95 -> oscilatorio (instavel)
#Kci = K*(s + a)/s

G2 = ct.feedback(Kc * P_pitch, Hs)
t1, y1 = ct.step_response(G2)


p = ct.step_info(G2)
for i, j in p.items():
    print(f"{i}:{j:.4f}")

space = np.linspace(0.1, 11, 100, endpoint=False)
setsTimes = []
risesTimes = []
overshoots = []

for k in K:
    for j in a:
        G2 = ct.feedback((k*(s + j)/s) * P_pitch, Hs)
        p = ct.step_info(G2)
        risesTimes.append(p['RiseTime'])
        setsTimes.append(p['SettlingTime'])
        overshoots.append(p['Overshoot'])
        list_of_params.append([f"Rise time: {p['RiseTime']}", f"Settling Time: {p['SettlingTime']}"])

#for i in list_of_params:
#    print(i)

#roots = ct.root_locus(G2)
#plt.show()
plt.title("Step Response of G(s)")
plt.plot(t1, y1)
plt.show()
plt.plot(space, risesTimes)
plt.title("Rise Time x Kc")
plt.show()
plt.plot(space, setsTimes)
plt.title("Settling Time x Kc")
plt.show()
plt.plot(space, overshoots)
plt.title("Overshoots x Kc")
plt.show()
