df = [
(0, 5), (2, 3), (4, 1), (0, 2), (3, 2), (5, 4), (1, 1), (5, 1), (2,5),

(0, 2), (1, 3), (4, 1), (5, 5), (1, 5), (2, 4), (2, 0), (3, 1), (5, 0),

(4, 1), (0, 4), (1, 3), (2, 1), (5, 4), (2, 2), (0, 3), (4,3), (1, 2),

(4, 2), (5, 1), (1, 3), (0, 3), (2, 0), (5, 1), (5, 2), (3, 1), (2, 3)]

#this has to count the times that appears each pair of number (the frequency)
num_dict = {}
for i in range (6):
    for j in range(6):
        num_dict[i,j] = 0


for tup in range(len(df)):
    x,y = df[tup]
    num_dict[x,y] += 1
    

print ( " x\y ", 0, 1, 2, 3, 4, 5 )
for i in range (6):
    print (" ",i, "  ", end="")
    for j in range(6):
        print (num_dict[i,j],"", end="" )
    print()

