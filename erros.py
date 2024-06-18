import control as ct
import numpy as np
from matplotlib import pyplot as plt
import sympy

s = sympy.Symbol('s')

Erros = []

P_pitch = (1.151*s + 0.1774)/(s**3 + 0.739*s**2 + 0.921*s)

expr3 = sympy.limit(P_pitch, s, 0)
print(expr3)
