from math import sqrt
# This programe calculates Pearson's lineal correlation coeficient 
#This coefficient indicates the quantitative value of correlation between two variables.
#If the value is near 1 or -1 the variables have a strong lineal dependency. 
#If the value is 1 or -1 the lineal dependency is functional.
#If the value is near 0 the variables have a weak dependency.
#If the value is 0 the variables are independents. 

#It can be programmed and can be visualized too.


def sample_to_square(sample):
    sample_squared = []
    
    for element in sample: 
        sample_squared.append(element ** 2)
        
    return sample_squared

def sample_per_sample(sample1, sample2): 
    samplexsample = []
    
    if len(sample1) != len(sample2): 
        return "The lists have not same length"
    
    for n in range(len(sample1)): 
        num = sample1[n] * sample2[n]
        samplexsample.append(num)
        
    return samplexsample

def avg(sample): 
    return sum(sample)/len(sample) 

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

    
    x_sq = sample_to_square(x)
    y_sq = sample_to_square(y) 
    x_per_y = sample_per_sample(x,y) 

    sum(x_per_y)

    if len(x) == len(y): 
        N = len(x)
    

    x_covariance_sq = covariance_squared(N,sum(x_sq), avg(x) )
    y_covariance_sq = covariance_squared(N,sum(y_sq), avg(y) )
    tot_covariance = covariance(N, sum(x_per_y), avg(x), avg(y))

    
    return Pearson(tot_covariance, x_covariance_sq, y_covariance_sq)

main()
    
    
    
    
