'''
import math
a = float(input("Digite um angulo"))
print("O angulo {} possui:\ncosseno {:.2f}\nSeno {:.2f}\nTangente{:.2f}" .format(a, math.cos(math.radians(a)), math.sin(math.radians(a)), math.tan(math.radians(a))))
'''

from math import radians, cos, sin, tan
a = float(input("Digite um angulo"))
print("O angulo {} possui:\ncosseno {:.2f}\nSeno {:.2f}\nTangente{:.2f}" .format(a, cos(radians(a)), sin(radians(a)), tan(radians(a))))

