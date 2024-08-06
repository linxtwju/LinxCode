import math 

def logaritm(base, de):
    return math.log(de)/math.log(base)

#with the properties, the base must be the same
def sum_logaritms(base, de1, de2): #log1 + log2
    result = logaritm (base, de1) + logaritm (base, de2)
    d = de1*de2
    result2 = logaritm (base, d)
    if result == result2:
        return result
    
def substract_logaritms(base, de1, de2): #log1 - log2
    result = round((logaritm (base, de1) - logaritm (base, de2)),5)
    d = de1/de2
    result2 = round(logaritm(base, d), 5)
    if result == result2:
        return result

def multiple_of_logaritm(base, de1, multiple): #multiple · log 
    d = de1**multiple
    return(logaritm(base, d))
    
def division_logaritm(base, de1, de2): #log1 / log2
    return logaritm (de2, de1)

def check_logaritm (base, result, de):
    if de == base ** result:
        return "Correct logaritm"
    
# print(logaritm(2, 5))
# print(sum_logaritms(2, 5, 3))
# print(substract_logaritms(2, 5, 3))
# print(multiple_of_logaritm(2,5,3))


result = math.log(3) + math.log(5) - math.log(2)
result2 = math.log(3*5/2)



print(math.log2(-4) + math.log2((-8)))



