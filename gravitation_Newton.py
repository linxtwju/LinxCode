from scipy.constants import G
from kepler import solarsystem_planets
from kepler import distances_planets_to_sun

#kg
mass_solarsystem_planets = {"Mercury" : 3.303e23,
                              "Venus" : 4.869e24, 
                              "Earth" : 5.976e24,
                              "Mars" : 6.421e23,
                              "Jupiter" : 1.9e27,
                              "Saturn" : 5.688e26,
                              "Uranus" :  8.686e25,
                              "Neptune" : 1.024e26,
                               }
solar_mass = 1.989e30
lunar_mass = 7.349e22 #kg
earth_mass = 5.98e24 #kg

distance_earth_moon = 3.82e8 #m


m1 = lunar_mass
m2 = earth_mass

r = distance_earth_moon

#F = G * ((m1 * m2) / (r**2))

def attraction_force (m1,m2, r):
    F = G * ((m1 * m2) / (r**2))
    return F

print ("The attraction force between moon and Earth is: ", attraction_force(m1,m2,r))


for planet in solarsystem_planets:
    m1 = solar_mass
    m2 = mass_solarsystem_planets[planet]
    r = distances_planets_to_sun[planet]
    F = attraction_force(m1, m2, r)
    print(f"The force between the Sun and {planet} is:", F, f"N. The distance between them is: {r}")
    
