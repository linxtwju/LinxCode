from math import sqrt

notas_filosofia = [5,4,9,8,10,9,8,3,5,10,5,9] #xi  notas filosofia
notas_matematicas = [8,6,5,6,10,6,10,2,7,4,8,10] #yi notas matemáticas

def avg(list): 
    return sum(list)/len(list) 

def covariance_squared(N, sum_var_squared, avg): 
    return 1/N * sum_var_squared - (avg**2)  

def covariancexy(N,sum_vars_multiplied, avg_X, avg_Y):
    return 1/N * sum_vars_multiplied - avg_X * avg_Y 


def correlation_coeficient(covariancexy, covariance_simplex, covariance_simpley):#Pearson
    return covariancexy / (covariance_simplex * covariance_simpley ) 

def prepare_data(x,y): 
    total_x = sum(x)#suma de xi
    total_y = sum(y)#suma de yi

    if len(x) == len(y):
        n = len(x) #tamaño de muestra
    else:
        return "El tamaño de las muestras no coincide"

    x_sq = [] #xi_2 
    y_sq = [] #yi_2
    for data in x:
        x_sq.append(data**2)
    for data in y:
        y_sq.append(data**2)
    
    total_x_sq = sum(x_sq) #suma de las x2
    total_y_sq = sum(y_sq) #suma de las y2
    
    x·y = [] #x multiplicadas por y
    for i in range(n):
        x·y.append(x[i]*y[i])
    total_x·y = sum(x·y)    
    
    
    data = {"x":x,"t_x": total_x , "y":y,"t_y": total_y , "x2": x_sq,"t_x2": total_x_sq 
            , "y2": y_sq,"t_y2": total_y_sq , "x·y": x·y, "t_x·y": total_x·y
            , "avgx": avg(x), "avgy": avg(y), "n":n}    
    
    return data

def calculate_covariances(x,y, cov_to_return = "cov_xy"):
    data_dict = prepare_data(x, y)
    dd = data_dict
    
    
    cov_sq_x = covariance_squared(dd["n"], dd["t_x2"], dd["avgx"] )
    cov_sq_y = covariance_squared(dd["n"], dd["t_y2"], dd["avgy"] )
    cov_x = sqrt(cov_sq_x)
    cov_y = sqrt(cov_sq_y)
    cov_xy = covariancexy(dd["n"], dd ["t_x·y"], dd["avgx"], dd ["avgy"])
    cc = cov_xy / (cov_x * cov_y)
    
    
    covariance_dict = {"cov_sq_x":cov_sq_x, "cov_sq_y":cov_sq_y
                       , "cov_x":cov_x, "cov_y":cov_y, "cov_xy" : cov_xy, "cc" : cc}
    
    return covariance_dict

def regression_line_y(x,y):
    d_cov = calculate_covariances(x,y)
    cov_xy = d_cov["cov_xy"]
    cov_x2 = d_cov["cov_sq_x"]
    b = cov_xy / cov_x2 
    a = avg(y) - (b * avg(x))
    
    return f"y = {a} + {b}x"

def regression_line_x(x,y):
    cov_xy = calculate_covariances(x,y)
    cov_y2 = calculate_covariances(x, y, "cov_sq_y")
    b = cov_xy / cov_y2 
    a = avg(x) - (b * avg(y))
    
    return f"x = {a} + {b}y"

def regression_prediction_y (x_value,x,y):
    d_cov = calculate_covariances(x,y)
    cov_xy = d_cov["cov_xy"]
    cov_x2 = d_cov["cov_sq_x"]
    b = cov_xy / cov_x2 
    a = avg(y) - (b * avg(x))
    
    y = a + (b*x_value)
    return y

def regression_prediction_x (y_value,x,y):
    cov_xy = calculate_covariances(x,y)
    cov_y2 = calculate_covariances(x, y, "cov_sq_y")
    b = cov_xy / cov_y2 
    a = avg(x) - (b * avg(y))
    
    x = a + (b*y_value)
    return x

def correlation_coeficient_interpretation(cc):#Pearson
    if -1 > cc > 1:
        return "Not valid coeficient of Pearson"
    elif cc == -1:
        return "Variables are linear correlated, the cloud of points is disposed in a decreasing line "
    elif cc == 1:
        return "Variables are linear correlated, the cloud of points is disposed in a growing line "
    elif cc == 0:
        return "Weak correlation, independent variables"
    elif cc < 0:
        return "Negative or inverse correlation"
    elif cc > 0:
        return "Positive or direct correlation"

expenses_on_advertising = [1,2,3,4,5,6]
eoa = expenses_on_advertising
obtained_sales = [10, 17, 30, 28, 39, 47]
os = obtained_sales

dict_expenses_sales = prepare_data(eoa, os)



edat = [0,3,6,9,12,15,18,21,24]
pes = [3.5,6.25,8.00,9.2,10.2,11.0,11.6,12.05,12.6]

# print(prepare_data(edat,pes))
# print (calculate_covariances(edat, pes))
print(regression_line_y(edat, pes))
# print(regression_prediction_y(85, pesos, tensio))