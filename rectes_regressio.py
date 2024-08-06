import correlacio_lineal_Pearson as c
from correlacio_lineal_Pearson import avg
import sympy as sp

def regression_lines(x,y, m = 0, n = 0):
    x_sq = c.list_to_square(x)
    y_sq = c.list_to_square(y)
    x·y = c.list_per_list(x,y)
    
    oX2 = c.covariance_squared(len(x), sum(x_sq), avg(x))
    oY2 = c.covariance_squared(len(y), sum(y_sq), avg(y))
    oXY = c.covariance(len(x),sum(x·y), avg(x), avg(y) )
    
    if m != 0:
        m = m
    else: 
        m = sp.Symbol("m")
    
    if n != 0: 
        n = n
    else:
        n = sp.Symbol("n") 
    
    #These are a and b values of the regression line of Y over X
    b1 = oXY/oX2
    a1 = avg(y) - b1 * avg(x) 
    
    regression_line1_y_x = a1*m + b1 #This is ax - b, as x is used, we use m
    print (regression_line1_y_x)
    
    #These are a and b values of the regression line of X over Y
    b2 = oXY/oY2
    a2 = avg(x) - b1 * avg(y)   
    
    regression_line2_x_y = (a2)*n + b2 #This is an - b , as x is used, we use n
    print(regression_line2_x_y)
    
    return (regression_line1_y_x, regression_line2_x_y)

x = [182, 187, 190, 197, 201, 203] # registrats
y = [80, 85, 92, 94, 100, 105] #afiliats

#quan hi hagi 209000 registrats, quants afiliats? 

#quan hi hagi 120000 afiliats, quants afiliats? 

rl_y_x, rl_x_y = regression_lines(x,y, m = 209000, n = 120000)

print (rl_y_x)
print (rl_x_y)
