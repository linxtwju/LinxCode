from math import sqrt
# This programe calculates Pearson's lineal correlation coeficient 
#This coefficient indicates the quantitative value of correlation between two variables.
#If the value is near 1 or -1 the variables have a strong lineal dependency. 
#If the value is 1 or -1 the lineal dependency is functional.
#If the value is near 0 the variables have a weak dependency.
#If the value is 0 the variables are independents. 

#It can be programmed and can be visualized too.


def list_to_square(list):
    list_square = []
    
    for element in list: 
        list_square.append(element ** 2)
        
    return list_square

def list_per_list(list1, list2): 
    listxlist = []
    
    if len(list1) != len(list2): 
        return "The lists have not same length"
    
    for n in range(len(list1)): 
        num = list1[n] * list2[n]
        listxlist.append(num)
        
    return listxlist

def avg(list): 
    return sum(list)/len(list) 

def covariance_squared(N, sum_var_squared, avg): 
    return 1/N * sum_var_squared - (avg**2)  

def covariance(N,sum_vars_multiplied, avg_X, avg_Y):
    return 1/N * sum_vars_multiplied - avg_X * avg_Y 

def Pearson(total_covariance, covariance_squared_x, covariance_squared_y): 
    r = total_covariance / (sqrt(covariance_squared_x * covariance_squared_y))
    return r
 
def main():
    x = [10,12,14,16,18,20] #habitacions dobles
    y = [15,17,18,20,23,25] #habitacions totals

    
    x_sq = list_to_square(x)
    y_sq = list_to_square(y) 
    x_per_y = list_per_list (x,y) 

    sum(x_per_y)

    if len(x) == len(y): 
        N = len(x)
    

    x_covariance_sq = covariance_squared(N,sum(x_sq), avg(x) )
    y_covariance_sq = covariance_squared(N,sum(y_sq), avg(y) )
    tot_covariance = covariance(N, sum(x_per_y), avg(x), avg(y))

    
    return Pearson(tot_covariance, x_covariance_sq, y_covariance_sq)

main()
    
    
    
    
