from scipy import pi
from math import e
from math import sqrt

def successio1(n):
    successio_a = []
    a0 = 0
    a1 = pi
    a2 = pi/2
    successio_a.append(a0)
    successio_a.append(a1)
    successio_a.append(a2)
    
    for i in range(3,11):
        an = (successio_a[i-1] + successio_a[i-2]) / 2
        successio_a.append(an)
   
    return successio_a[n]

    
   
# for i in range(1,11):
#     print (f"a{i} =", successio1(i) ) 
    
    
def successio2(n):
    successio_b = []
    b0 = 0
    b1 = -1
    b2 = 1
    successio_b.append(b0)
    successio_b.append(b1)
    successio_b.append(b2)
    
    for i in range(3,11):
        bn = (-successio_b[i-1] * successio_b[i-2])
        successio_b.append(bn)
   
    return successio_b[n]

# for i in range(1,11):
#     print (f"b{i} =", successio2(i) ) 


def successio3(n):
    a = (1 + 2 * n)/n
    return a

# for i in range (10000,10100): 
#     print (f"a{i} =", successio3(i))


def successio4(n):
    a = e ** successio3(n)
    return a

# for i in range (10000,10100): 
#     print (f"a{i} =", successio4(i))

def successio5(n):
    a = sqrt(successio3(n))
    return a

# for i in range (10000,10100): 
#     print (f"a{i} =", successio5(i))




successio6 = lambda n: (4*n-8)/(5*n)
successio7 = lambda n: (1000*n)/(n**2 - 2*n)
successio8 = lambda n: 2-n
successio9 = lambda n: ((5+(2*n))/(2*n))-((n+6)/(n+2)) 


successio10 = lambda n: ((1+1/n)**(4*n)) #lim e**4

for i in range (100000,100100): 
    print (f"a{i} =", successio10(i))
    
