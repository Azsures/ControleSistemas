import control as ct
from matplotlib import pyplot as plt
import numpy as np

s = ct.tf('s')
P_pitch = (1.151*s + 0.1774)/(s**3 + 0.739*s**2 + 0.921*s)
Hs = 1/((0.43/5)*s + 1)

list_of_params = []


#Kci = 1.2+ ((2.25)/(2.2*s)) + 1.3*s
Kci = 2+ 4/s + 6*s

print(Kci)
G2 = ct.feedback(Kci * P_pitch, Hs)
t1, y1 = ct.step_response(G2)

kc = np.linspace(0.01, 6, 40, endpoint=False)
ki = np.linspace(0.01, 6, 40, endpoint=False)
kd = np.linspace(0.01, 6, 40, endpoint=False)

temp = []
p = ct.step_info(G2)

print(f"SettlingTime:{p['SettlingTime']:.2f}")
print(f"Overshoot:{p['Overshoot']:.2f}")
print(f"RiseTime:{p['RiseTime']:.2f}")
print(f"SteadyStateError:{(p['SteadyStateValue'] - 1)/100:.2f}%")
'''
for i in kc:
    for j in ki:
        for k in kd:
            Kci = i + ((j)/s) + k*s
            G2 = ct.feedback(Kci * P_pitch, Hs)
            p = ct.step_info(G2)
            if p['SettlingTime'] < 11 and p['Overshoot'] < 11:
                temp.append([i, j, k, p['SettlingTime'], p['Overshoot']])
                if p['SettlingTime'] <= 10 and p['Overshoot'] <= 10:
                    break
'''

space = np.linspace(0.1, 6, 40, endpoint=False)
setsTimes = []
risesTimes = []
overshoots = []


#for i in list_of_params:
#    print(i)

#roots = ct.root_locus(G2)
#plt.show()

plt.title("Step Response of G(s)")
plt.plot(t1, y1)
plt.show()

