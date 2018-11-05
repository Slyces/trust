#!/usr/bin/env python3
from math import cos, sin, pi
r = 1.0
ro = 0.2

# surface of a circle
def circle_surface(r):
    return pi * r * r

def sphere_surface(r):
    return (4/3) * pi * r * r * r

total2d = circle_surface(r)
total_agent2d = circle_surface(r/2 + ro) - circle_surface(r/2 - ro)
rapport2d = total_agent2d / total2d * 100

total3d = sphere_surface(r)
total_agent3d = sphere_surface(r/2 + ro) - sphere_surface(r/2 - ro)
rapport3d = total_agent3d / total3d * 100

print("""\
# -------------------------------- version 2D -------------------------------- #
Surface totale : (cercle)
    {}
Surface couverte par l'agent:
    {}
Rapport:
    {:.2f} %
# -------------------------------- version 3D -------------------------------- #
Volume total : (sphere)
    {}
Volume couvert par l'agent:
    {}
Rapport:
    {:.2f} %
""".format(total2d, total_agent2d, rapport2d,
           total3d, total_agent3d, rapport3d))
