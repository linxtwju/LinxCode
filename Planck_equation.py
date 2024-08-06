import units as u
#constante de Planck
h = 6.626e-34 #J·s

f = 0 #Hz
#Relación Planck-Einstein
E = h*f

energy = lambda f : f*h

#velocidad de la luz
c = 299792458 #m/s

l = 0
#Relación longitud de onda(m) * frecuencia (Hz) = velocidad de la luz (m/s)
_c = l * f

frequency = lambda l: c / l



#variables
f = 2e24

longitud_anaranjada_min = 590 #nm
longitud_anaranjada_max = 635 #nm

longitud_verde_min = 520 #nm
longitud_verde_max = 560 #nm

#Luz más energética? 



l_n_min = u.nm_to_m(longitud_anaranjada_min)
l_n_max = u.nm_to_m(longitud_anaranjada_max)

l_v_min = u.nm_to_m(longitud_verde_min)
l_v_max = u.nm_to_m(longitud_verde_max)
    

f_n_min = frequency (l_n_min)
f_n_max = frequency (l_n_max)
f_v_min = frequency (l_v_min)
f_v_max = frequency (l_v_max)

frequencies_example = [f_n_min, f_n_max, f_v_min, f_v_max]

for hz in range(15):
    print (hz, "Hz ->",energy(hz), "J")
    
    
#Es mas energética la luz verde

