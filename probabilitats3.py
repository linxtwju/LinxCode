def complementary(sample_space, event):
    complementary_list = []
    for element in sample_space:
        if element not in event:
            complementary_list.append(element)
    return complementary_list

def intersection(event1, event2):
    intersection_list = []
    for element in event1:
        if element in event2:
            intersection_list.append(element)
    return intersection_list

def union(event1, event2):
    union_list = []
    for element in event1:
        union_list.append(element)
    for element in event2:
        if element not in union_list:
            union_list.append(element)
    return union_list

def minus(event1, event2):
    minus_list = []
    for element in event1:
        if element not in event2:
            minus_list.append(element)
    return minus_list



sample_space = ("a","b","c","d","e","f","g","h","i","j")
ss = sample_space

#events
eA = ("a","e","f","g","j")
eB = ("a","e","i")
eC = ("a","c","e","g")
eD = ("b","c","d","e","f")
list_events = [eA, eB, eC, eD]

#operations
oA = [] #A intersection with complementary of B
oB = [] #complementary of A intersection with complementary of B
oC = [] #B union with complementary of (C intersection D)
oD = [] #C union with complementary of D
oE = [] #D minus (B intersection C)
oF = [] #(A union B) minus (C intersection D)


ceB = [] #complementary event B
for l in ss:
    if l not in eB: 
        ceB.append(l)
        
for e in eA: 
    if e in ceB:
        oA.append(e)        

ceA = complementary(ss, eA)
oB = intersection(ceA, ceB)

CiD = intersection(eC, eD)
ceCiD = complementary(ss, CiD)
oC = union(eB, ceCiD)

ceD = complementary(ss,eD)
oD = union (eC, ceD)

BiC = intersection(eB, eC)
oE = minus(eD, BiC)

oF = minus(union(eA,eB), intersection(eC,eD))
        
        
print("a: ", oA)
print("b: ", oB)
print("c: ", oC)
print("d: ", oD)
print("e: ", oE)
print("f: ", oF)

            

