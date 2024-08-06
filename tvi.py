from math import pi
from sympy import *

area_cercle = lambda r : r**2 * pi

divide_by_pi = lambda x : x/pi

result = area_cercle(2)
print (result)
print (str(int(divide_by_pi(result))) + "π")


