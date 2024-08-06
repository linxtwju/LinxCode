import math

def equation_2nd_grade(a,b,c):
    discriminant = (b**2) - (4*a*c)
    root = math.sqrt(discriminant) 
    y1 = (-b + root) / (2*a)
    y2 = (-b - root) / (2*a)
    # x1 = (-b + (math.sqrt(((b)**2) - 4*a*c)))/(2*a)
    # x2 = (-b - (math.sqrt(((b)**2 - 4*a*c))))/(2*a)
    
    
    return (y1, y2)

def degrees_to_radians(degrees):
    return degrees*2*math.pi/360

def velocitats(velocitat,angle):#retorna la velocitat vx i vy
    angle_rad = degrees_to_radians(angle)
    
    vx = velocitat * math.cos(angle_rad)
    vy = velocitat * math.sin(angle_rad)

    return vx,vy

def component_x(x0,v0x, t):
    x = x0 + v0x * t
    return x

def component_y(y0, v0y, t, a):
    y = y0 + v0y * t + 1/2 * a * (t **2)
    return y

def component_y0(y, v0y,t,a):
    if y ==0 and v0y==0: 
        y1 = -1/2 * a * t**2
        return y1

def component_y_temps(y, y0, v0y, a):
    s = -(1/2)*a
    g = -v0y
    e = -y0 + y
    
    
    
    
    t1 , t2 = equation_2nd_grade(s,g,e)
   

    
    if t1 > 0:
        if t2 > 0:
            return t1,t2
        else:
            return t1
    elif t2 > 0:
        return t2
    else:
        return "Invalid equation"
    
    
def component_temps_vy_hmax( v0y, g,  vy=0):
    return v0y/g
    

g = 9.8

def ej2():
    v0x = 40#m/s
    v0y = 60#m/s
    
    v1y = 0
    v2x = v0x
    
    
    
    t_hmax = component_temps_vy_hmax(v0y,g)
    print (t_hmax)
    y_max = component_y(0,v0y,t_hmax, (-g))
    
    
    t = component_y_temps(0,0,v0y, (-g))
    print(t)
    x = component_x(0,v0x, t)
    
    print (f"L'altura máxima és {y_max} i l'abast horitzontal és {x}" )
           
ej2()
    













angle = 50#º
velocitat_inicial = 20#m/s
x0 = 0#m
#x = ?
y = 0#m
y0 = 0#m
velocitat_final = 0#m/s
vx = 0
vy = 0
v1y = 0


g = -9.80665#m/s2

# xl=[]
# yl=[]
# vx_=[]
# vy_ = []
# t_ = []
def db_creation():
    t = component_y_temps(y, y0, v0y, g)
    x= component_x(x0,v0x, t)
    v0x,v0y = velocitats(velocitat_inicial,angle)#m/s 
    
    x_ = [x0,[],x]
    y_ = [y0,[],y]
    t_ = [0,[],t]
    vx_ = [v0x,[],vx]
    vy_ = [v0y,v1y,vy]

    print("x_:", x_)   
    print("y_:",y_)
    print ("vx_:",vx_)
    print ("vy_:",vy_)
    print ("t_:",t_)
    
    

    








    
        
    
    




    