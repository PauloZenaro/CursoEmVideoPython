'''
co = float(input("Digite o cateto oposto"))
ca = float(input("Digite o cateto adjacente"))
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print(hip)
'''
'''
from math import hypot
co = float(input("Digite o cateto oposto"))
ca = float(input("Digite o cateto adjacente"))
print(hypot(ca,co))
'''

import math
co = float(input("Digite o cateto oposto"))
ca = float(input("Digite o cateto adjacente"))
hip = math.hypot(co, ca)
print("{}" .format(hip))