#This programme serves to measure the covariance in with intervals data

#Create the framework
# df = {}

# for npassatgers in intervals_passatgers_en_milers:
#     for retards in intervals_percentatge_vols_amb_retard:
#         df[npassatgers, retards] = 0 
df = {((0, 10), (0, 2)): 0, ((0, 10), (2, 4)): 3, ((0, 10), (4, 6)): 1, ((0, 10), (6, 8)): 2, ((0, 10), (8, 10)): 0,
 ((10, 20), (0, 2)): 2, ((10, 20), (2, 4)): 0, ((10, 20), (4, 6)): 1, ((10, 20), (6, 8)): 2, ((10, 20), (8, 10)): 1,
 ((20, 30), (0, 2)): 0, ((20, 30), (2, 4)): 2, ((20, 30), (4, 6)): 4, ((20, 30), (6, 8)): 0, ((20, 30), (8, 10)): 1
 , ((30, 40), (0, 2)): 2, ((30, 40), (2, 4)): 0, ((30, 40), (4, 6)): 1, ((30, 40), (6, 8)): 0, ((30, 40), (8, 10)): 3}

def marques_classe(interval_list):
    mc = []
    
    for interval in interval_list: 
        a,b = interval
        MC = a+ ((b-a)/ len(interval))
        mc.append(MC)
        
    return mc

def mesura_frequencies(list1, list2, dataframe):#first x
    
    frequencia_i = []
    for x in list1:
        f = 0
        for y in list2:
            f += dataframe[x,y]
                        
        frequencia_i.append(f)
    
    
    frequencia_j = [] 
    for y in list2:
        f = 0
        for x in list1:
            f += dataframe[x,y]
            
        frequencia_j.append(f)
    
    
    total_fr_i = 0
    total_fr_j = 0
        
    for fr in frequencia_i:
        total_fr_i += fr
    
    for fr in frequencia_j:
        total_fr_j += fr
    
    if total_fr_i == total_fr_j:
        fr_ij = total_fr_i
    else:
        return "Something was miscalculated with the frequencies"
    
    
    
    return (frequencia_i, frequencia_j, fr_ij)       #fr_ij  

def mitjanes(mcx,mcy, freq_ij):
    
    fr_i = freq_ij[0]
    fr_j = freq_ij[1]
    fr_ij = freq_ij[2]
           
    x_i·f_i = []
    y_j·f_j = []
    
    length_check = False  
    
    # check if the lists have the same length
    if len(mcx) == len(fr_i):
        if len(mcy) == len(fr_j):
            length_check = True                         
    
    
    for n in range(len(mcx)):
        f_i = mcx[n] * fr_i[n]
        x_i·f_i.append(f_i)
    
    for n in range(len(mcy)):   
        f_j = mcy[n] * fr_j[n]
        y_j·f_j.append(f_j)
    
    sum_x_i·f_i = 0
    sum_y_j·f_j = 0 
    
    for m in x_i·f_i:
        sum_x_i·f_i += m
    for m in y_j·f_j:
        sum_y_j·f_j += m
        
    mitjana_x = sum_x_i·f_i / fr_ij
    mitjana_y = sum_y_j·f_j / fr_ij
    
    return (mitjana_x, mitjana_y)
   
def covariancia(freq_ij,mcx,mcy, df, list1, list2):
    fr_ij = freq_ij[2]
    
    x,y = mitjanes(mcx, mcy, freq_ij)
    
    mostra_total = 0
    for i in range(len(mcx)):
        for j in range(len(mcy)):
            mostra_total += (mcx[i] * mcy[j] * df[list1[i],list2[j]] )     
            
            
    covar = (1/fr_ij * mostra_total) - (x * y)
    
    return covar

 
def main():
    intervals_passatgers_en_milers = [(0,10),(10,20),(20,30),(30,40)] #x
    intervals_percentatge_vols_amb_retard = [(0,2),(2,4),(4,6),(6,8),(8,10)] #y

    passatgers = intervals_passatgers_en_milers #x
    retards = intervals_percentatge_vols_amb_retard#y
    
    mcx = marques_classe(intervals_passatgers_en_milers)
    mcy = marques_classe(intervals_percentatge_vols_amb_retard)

    freq_ij = mesura_frequencies(passatgers, retards, df)
    
    print ("Passatgers:",passatgers)
    print ("Vols amb retard:",retards)
    print ("MCX:", mcx )
    print ("MCY:", mcy )
    print(freq_ij)
    
    
    
    
    print  (covariancia(freq_ij, mcx, mcy, df, passatgers, retards))

main()   