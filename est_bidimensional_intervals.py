df = [[0 for i in range(4)]for j in range(5)]

#I have to explain what is this
df = [[3, 1, 1, 0], [1, 3, 4, 1], [0, 1, 4, 1], [0, 1, 3, 5], [0, 0, 1, 5]]

sample = 0
for j in range(len(df)):
    sample += sum(df[j])
    
n = sample
x = [1,2,3,4]
y = [55, 65, 75, 85, 95]

x_f = 0
for j in range(len(df)):    #pes 
    for i in range(len(df[j])):     #talles
        x_f += df[j][i] * x[i]

y_f = 0      
for j in range(len(df)):    #pes 
    for i in range(len(df[j])):     #talles
        y_f += df[j][i] * y[j]
        
avgx = x_f / n        
avgy = y_f / n        

x_y_f = 0
for j in range(len(df)):    #pes 
    for i in range(len(df[j])):     #talles
        x_y_f += df[j][i] * x[i] * y[j]        

covar_xy = (x_y_f/n) - (avgx*avgy)

x2_f = 0
for j in range(len(df)):    #pes 
    for i in range(len(df[j])):     #talles
        x2_f += df[j][i] * x[i] * x[i]


print(x2_f)