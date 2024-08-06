bowls = ["red", "white", "black"]
dice = [1,2,3,4,5,6]

sample_space = []

for b in bowls:
    for d in dice:
        x,y = b, d
        sample_space.append((x,y))

eventA = []#obtain a red bowl and odd number
eventB = []#obtain a not white bowl and a 3 multiple
eventC = []#obtain a 2 in the dice and a black bowl
eventD = []#obtain a not white bowl and a not odd number

odd_num_dice = [1,3,5]

for d in dice:
    if d in odd_num_dice:
        eventA.append(("red", d))

for b in bowls:
    if b != "white":
        for d in dice:
            if d % 3 == 0:
                eventB.append((b, d))

for b in bowls:
    if b == "black": 
        for d in dice:
            if d == 2:
                eventC.append((b,d))

for b in bowls:
    if b != "white": 
        for d in dice:
            if d not in odd_num_dice:
                eventD.append((b,d))

print ("Sample space:", sample_space)
print ("Event A:", eventA)
print ("Event B:", eventB)
print ("Event C:", eventC)
print ("Event D:", eventD)
