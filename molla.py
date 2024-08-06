k = lambda N,m : N/m 

F_5g = 0.245
L_5g = 0.0098

F_10g = 0.294
L_10g = 0.0118

F_20g = 0.392
L_20g = 0.0157


print ("5g",k(F_5g, L_5g))
print ("10g",k(F_10g, L_10g))
print ("20g",k(F_20g, L_20g))

constant_k = (k(F_5g, L_5g) + k(F_10g, L_10g)+ k(F_20g, L_20g))/3

N = lambda k,m : k * m 
P = N(constant_k, 0.029)

g = 9.8
massa = lambda Pes,g :  Pes/g 


pes = lambda m: m*g

print( pes (100), pes (150), pes (250))

print ((k(pes (100), 16) + k( pes (150), 24)+ k(pes (250), 41))/3)