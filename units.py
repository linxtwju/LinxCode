#This programme serves to convert different types of units to another ones. 
#The first unit is the quantity equivalent of 1 unit of the second unit of measure. 
#import smtpd

#mass
g = "grams"
kg = "kilograms"
pound = "pounds"                              
mass_IS = g

g_kg = 1e3
g_pound = 453.592



#length (distance)
m = "meters"
km = "kilometers"
mm = "milimeters"   
nm = "nanometers"    
inch = "inch"                                 
length_IS = m

m_km = 1000
mm_inch = 24.5
km_marineMile = 1.852


cm_m = 100  
cm_km =  cm_m * m_km

mm_m  = 1000
nm_m = 1e9


#time 
h = "hours"
min = "minutes"
s = "seconds"
time_IS = s

min_h = 60
s_min = 60
s_h = 3600

h_day = 24
day_year = 365.25

#force
N = "Newtons"
force_IS = N
kp = "kilopond"

#Newton = "kg * m * s ** -2"

dina_N = 100000
N_kilopond = 9.81


#energy 
J = "Joules"
kJ = "kiloJoules"
cal = "calorie"
kcal = "kilocalorie"
Mcal = "megacalorie"
W·s = "Watts·second"
kW·h = "kilowattshour"
Btu = "British thermal unit"
Mbtu = "Mega British thermal unit"
kp·m = "kilopondmetre"
energy_IS = J

J_W·s = 1 #1 Joule is equal to 1 W·s (watt·second)
J_kJ = 1000
J_btu = 1055
J_cal = 4.187
J_kpm = 9.81

W·s_cal = 4.186

kW·h_W·s = 2.78 * 10 ** -7

btu_Mbtu = 1000000

cal_J = 0.2388
cal_Kcal = 1000
cal_Mcal = 1000000

kJ_kW·h = 36000
kJ_kcal = 4.186

#power
W = "Watts"
cv = "horsepower"
Jçs = "Joules per second"                             #Since this line "ç" is used instead of "/" to name some variables

W_cv = 736
W_kW = 1000 
W_Jçs = 1 #1 Watt is equal to 1 J/s (Joule / second)                    


#velocity
kmçh = "kilometres per hour"
mçs = "metres per second"
mçmin = "metres per minute"
kn = "knot" 
velocity_IS = mçs
                                                 
kmçh_mçs = s_h / m_km                                                   
mçmin_mçs = s_min                                                       
kmçh_kn = 1.852                                                       
mçs_kn = 0.5        

#area
cm2 = "square centimetres"
m2 = "square metres"

cm2_m2 = 10000

mm2_m2 = 1e6



#volume
l = "liters"                                                      
m3 = "cubic metres"
dm3 = "decimetres"
galEn = "English gallons"
galAm = "American gallons"
volume_IS = m3

dm3_m3 = 1e3
l_dm3 = 1
l_galEn = 3.785
l_galAm = 4.546

cm3_m3 = 1e6
mm3_m3 = 1e9

#pressure
Pa = "Pascals"
kPa = "Kilopascals"
atm = "atmosferas"
bar = "bar"
Nçm2 = "Newtons per square metres"
kpçcm2 = "Kiloponds per square centimetre "
pressure_IS = Pa

bar_atm = 1
atm_bar = bar_atm

Nçm2_Pa = 1
Pa_Nçm2 = Nçm2_Pa

Pa_kPa = 1000
Pa_bar = 100000
bar_Pa = 10**-5

kpçcm2_Nçm2 = 9.81 * cm2_m2

#temperature 
 
def celsius_to_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit
    
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = 1.8 * kelvin - 459.4
    return fahrenheit



#Functions

#length
nm_to_m = lambda nm: nm / nm_m

#time
s_to_h = lambda s: s / s_h
h_to_day = lambda h: h / h_day
day_to_year = lambda d: d / day_year
s_to_year = lambda s: ((s/s_h) / h_day)/day_year

pounds_to_kg = lambda pounds: pounds * (g_pound / g_kg)
newtons_to_dina = lambda Newtons: Newtons * dina_N
h_to_min = lambda h: h * min_h
km_to_marineMiles = lambda km: km / km_marineMile
inch_to_mm = lambda inch: inch * mm_inch
kWh_to_kJ = lambda kWh: kWh * kJ_kW·h
mbtu_to_kcal = lambda mbtu : mbtu * (btu_Mbtu * J_btu / J_cal / cal_Kcal)
kpm_to_kcal = lambda kpm: kpm * (J_kpm / J_cal / cal_Kcal)
Mcal_to_kWh = lambda Mcal: Mcal * (cal_Mcal * W·s_cal * kW·h_W·s)
kW_to_cv = lambda kW: kW * (W_kW/W_cv)
cv_to_Jçs = lambda cv: cv * (W_cv/W_Jçs)
kmçh_to_mçs = lambda kmçh: kmçh/ kmçh_mçs
kn_to_mçmin = lambda kn: kn * mçs_kn * mçmin_mçs
l_to_m3 = lambda l: l * l_dm3 / dm3_m3
dm3_to_galEn = lambda dm3: dm3 * l_dm3 / l_galEn
bar_to_atm = lambda bar: bar * atm_bar
Nçm2_to_kPa = lambda Nçm2: Nçm2 * Nçm2_Pa / Pa_kPa
kpçcm2_to_bar = lambda kpçcm2: kpçcm2 * kpçcm2_Nçm2 * Nçm2_Pa / Pa_bar




#print (pounds_to_kg(2500), newtons_to_dina(30), h_to_min(0.25), km_to_marineMiles(100), inch_to_mm(3/4), celsius_to_fahrenheit(32)
       #, kelvin_to_fahrenheit(300), kWh_to_kJ (200), mbtu_to_kcal(3), kpm_to_kcal(500), Mcal_to_kWh(2), kW_to_cv(3), cv_to_Jçs(36)
       #, kmçh_to_mçs(120), kn_to_mçmin(30), l_to_m3(6500), dm3_to_galEn(400),  bar_to_atm(5), Nçm2_to_kPa(10), kpçcm2_to_bar(6))



#unit = input("What do you want to convert?" )

