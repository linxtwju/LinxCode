from math import pi
from math import sqrt
from scipy.constants import G
from astropy.constants import M_sun 
import units as u

#meters
distances_planets_to_sun = {"Mercury" : 57.91e9,
                              "Venus" : 108.21e9, 
                              "Earth" : 149.6e9,
                              "Mars" : 227.94e9,
                              "Jupiter" : 778.41e9,
                              "Saturn" : 1.43e12,
                              "Uranus" :  2.87e12,
                              "Neptune" : 4.5e12,
                               }
solarsystem_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Kepler third law
#C = (T**2) / (a**3)  -> s2/m3
# T = 0#s
# a = 0#m



R_earth_to_sun = 149.6e9 #m

R = R_earth_to_sun



def periodo_orbital(R): #s
    k = (4 * (pi **2))/ (G * M_sun.value)
    T = sqrt(k * (R**3))
    return T


period_earth = periodo_orbital(R)


validate = u.s_to_year(period_earth)


def orbital_period_planet(planet):
    R = distances_planets_to_sun[planet]
    periodo_orbital_of_the_planet = periodo_orbital(R)
    return u.s_to_year(periodo_orbital_of_the_planet)
    
    
    
for planet in solarsystem_planets:
    t = orbital_period_planet(planet)#in years
    print("Orbital period of " + planet + ":", t)
    
