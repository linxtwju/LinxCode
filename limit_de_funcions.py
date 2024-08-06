funcio1 = lambda x: (6-x)/(2-x)
funcio2 = lambda x: (6*(x**4)+1)/(2*(x**4)+1)
funcio3 = lambda x: (-(6*(x**4)+1))/(2*(x**3)+1)

print("+infinit")
for i in range(4000000,5000000, 50000):
    print (i, ":", funcio2(i))

print()
print("-infinit")
for i in range(-4000000,-5000000, -50000):
    print (i, ":", funcio2(i))
    
print("+infinit")
for i in range(4000000,5000000, 50000):
    print (i, ":", funcio3(i))

print()
print("-infinit")
for i in range(-4000000,-5000000, -50000):
    print (i, ":", funcio3(i))