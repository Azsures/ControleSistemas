import control as ct
from matplotlib import pyplot as plt
import numpy as np

s = ct.tf('s')
P_pitch = (1.151*s + 0.1774)/(s**3 + 0.739*s**2 + 0.921*s)
Hs = 1/((0.4674/5)*s + 1)

list_of_params = []

Kc = (1.125)     #Kc <= 5.95 -> estavel; Kc > 5.95 -> oscilatorio (instavel)

G2 = ct.feedback(Kc * P_pitch, Hs)
t1, y1 = ct.step_response(G2)


s = ct.step_info(G2)
for i, j in s.items():
    print(f"{i}:{j:.4f}")

space = np.linspace(0.1, 6, 40, endpoint=False)
setsTimes = []
risesTimes = []
overshoots = []

for i in space:
    G2 = ct.feedback(i * P_pitch, Hs)
    s = ct.step_info(G2)
    risesTimes.append(s['RiseTime'])
    setsTimes.append(s['SettlingTime'])
    overshoots.append(s['Overshoot'])
    list_of_params.append([f"Rise time: {s['RiseTime']}", f"Settling Time: {s['SettlingTime']}"])

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
