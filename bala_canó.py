from projectil import *

ang1 = 30#º
ang2 = 45#º
ang3 = 60#º
velocitat_inicial = 50#m/s

angles = [ang1,ang2,ang3]

v_components_per_angle = []

for angle in angles:
    v0x,v0y = velocitats(velocitat_inicial, angle)
    v0x = round(v0x)
    v0y = round(v0y)

    v_components_per_angle.append([v0x, v0y])
    
# for i in range(len(angles)):
#     print (str(angles[i]), str(v_components_per_angle[i]), "(vx,vy)")
    
     
db = [[[" ?" for x in range(len(angles))] for i in range(3)]for m in range(5)] 
 
x = 0
y = 1
vx = 2
vy = 3
t = 4

inicial = 0
max = 1
final = 2

for i in range(len(angles)):
    r = " 0"
    db[x][0][i] = r
    db[y][0][i] = r
    db[t][0][i] = r

    db[vy][1][i] = r

    db[y][2][i] = r
    db[vx][2][i] = r
    db[vy][2][i] = r

for i in range(len(v_components_per_angle)):
    db [vx][0][i] = str(v_components_per_angle[i][0])
    db [vy][0][i] = str(v_components_per_angle[i][1])

def show_db(db):
    angles_line = "     30    45    60 " 
    
    print ( "              0" , "                  1", "                  2   ")
    print ( "  "+ angles_line * 3 )
    
    vertical = ["x ", "y ", "vx", "vy", "t "]
    for i in range(len(db)):
        print (vertical [i], db[i]) 

for ideg in range(len(angles)):
    cy = int(db[y][final][ideg])
    cy0 = int(db[y0][inicial][ideg])
    cv0y= int(db[vy][inicial][ideg])
    
    
    ct = component_y_temps(cy, cy0, cv0y, g)
    ct = round(ct,2)
    db[t][final][ideg] = str(ct)

for ideg in range(len(angles)):
    
    cx0 = float(db[x0][inicial][ideg])
    cv0x= float(db[vx][inicial][ideg])
    ct = float(db[t][final][ideg])
    
    
    cx = component_x(cx0, cv0x, ct)
    cx = round(cx,2)
    db[x][final][ideg] = str(cx)

for ideg in range(len(angles)):
    
    cx0 = float(db[x0][inicial][ideg])
    cv0x= float(db[vx][inicial][ideg])
    ct = float(db[t][final][ideg])
    
    
    cx = component_x(cx0, cv0x, ct)
    cx = round(cx,2)
    db[x][final][ideg] = str(cx)

# for ideg in range(len(angles)):
    
#     cy = float(db[y][final][ideg])
#     cv1y= float(db[vy][max][ideg])
#     ct = float(db[t][final][ideg])
    
    
    
#     cy1 = component_y0(cy, cv1y, ct, g)
#     cy1 = round(cy0)
#     db[y][inicial][ideg] = str(cy1)

# for ideg in range(len(angles)):
    
#     cy1 = float(db[y][max][ideg])
#     cv0y= float(db[vy][inicial][ideg])
#     ct = float(db[t][final][ideg])
    
    
    
#     cy0 = component_y(cy1, cv0y, ct, g)
#     cy0 = round(cy0)
#     db[y][inicial][ideg] = str(cy0)




 



show_db(db)

 



