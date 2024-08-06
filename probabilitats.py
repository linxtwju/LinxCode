A = "parell"
B = "imparell diferent a 5"
C = "x > 2"

espai_mostral = []

for i in range(1, 7):
    espai_mostral.append(i)
    
A = [] 
B = []
C = []

for i in range(len(espai_mostral)):
    if espai_mostral[i] % 2 == 0: 
        A.append(espai_mostral[i])
    elif espai_mostral[i] % 2 == 1 and espai_mostral!=5:
        B.append(espai_mostral[i]) 
        
    
# esdeveniments a mostrar: B, AuB, AnC, B-c
