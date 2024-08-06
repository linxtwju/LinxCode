from math import pi
from math import sqrt 

ixpi = []
i_pi = []
pi_i = [0]

sqrt(2)
pr = 2*pi

for i in range(100):
    ixpi.append(i*pi)
    i_pi.append(i/pi)
    if i != 0:
        pi_i.append(pi/i)


df = [ixpi, i_pi, pi_i]

def showdf (df):    
    print ("i   ixpi    i/pi    pi/i" )

    for n in range(len(ixpi)):
        print (f"{n}     {ixpi[n]}       {i_pi[n]}       {pi_i[n]}")
    
#if L = 1 and L = 2·pi·r, then r:     
r = 1/(2*pi)

#if L = 1 and L = pi·d, then d:
d = 1/pi  

#if A = 1 and A = pi·r2, then r:
r1 = sqrt(1/pi)
#

#
print(*pi)
