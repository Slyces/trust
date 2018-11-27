from random import random, gauss
import numpy as np

n = 10e5
p_g = 0.1
p_o = 0.4
p_b = 0.05
p_i = 0.45

uniform = lambda a, b: a + random() * abs(a - b)
g = lambda : gauss(uniform(5, 10), 1.0)
o = lambda : gauss(uniform(0, 5), 1.0)
b = lambda : gauss(uniform(-10, 0), 2.0)
i = lambda : uniform(-5, 5)

values = []
for k in "gobi":
    values += [globals()[k]() for i in range(int(globals()["p_" + k] * n))]

print(np.mean(values))
