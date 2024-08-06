#experiment aleatori -> previment no es pot predir el resultat
#experiment deterministes -> es pot predir el resultat

#espai mostral -> conjunt de tots els resultats possibles (Ω o E) 
#esdeveniment -> subconjunt espai mostral

#esdeveniment
    #if no passa mai
        #És impossible
    #if passa sempre
        #És segur
        
#esdeveniment A -> contrari o complementari (A amb barra a dalt) passa només quan no passa A

ex_espai_mostral = [ 1, 2, 3, 4, 5, 6 ] #dau

#esdeveniments elementals = {1},{2},{3},{4},{5},{6}
A=[2, 4, 6] #succés que surti nombre parell
A_complementari = [1,3,5]
esdeveniment_impossible = [7]

#DONATS DOS ESDEVENIMENTS A I B

#Unió de A i B = A U B -> succeix A o B o tots dos
#Intersecció A i B = A N B (u invertida) -> es produeixen A i B simultàniament

#Successos incompatibles si no poden succeir a la vegada, la intersecció és buida

A=[2, 4, 6]
B=[1,3, 4, 6]
AunioB = [ 1, 2, 3, 4, 5, 6 ]
AinterseccioB = [4,6]