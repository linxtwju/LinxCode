import math 

def equation_2nd_grade(a,b,c):
    x1 = (-b + math.sqrt(((b)**2) - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt((b)**2 - 4*a*c))/(2*a)
    
    return (x1, x2)


print(equation_2nd_grade(4.9 ,-10,-10))


    
    