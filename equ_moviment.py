def eq_x (t):
    return 6.25 * t

def eq_y (t):
    return (-4.9*((t)**2)+7.94 * t + 2.05)

for i in range (0,15):
    i = i/10 
    
    print("x", i, ":",eq_x(i))
    # print("y", i, ":",eq_y(i)) 
