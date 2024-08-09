import string

class Element(): 
    def __init__(self, name, symbol, atomic_number, mass_number, energetic_levels, group, type, oxidation_number = None)-> None:
        self.name = name;
        self.X = symbol; 
        self.Z= atomic_number; 
        self.A = mass_number;
        self.energetic_levels = energetic_levels;
        self.group = group;
        self.type = type;
        self.o_n = oxidation_number;
           
Hydrogen = Element("Hydrogen", "H", 1, 1, 1, 1, "Others no metals",[+1,-1] )
Helyum = Element("Helyum", "He", 2, 4, 1, 18, "Noble gas",[0] )
Lithium = Element("Lithium", "Li", 3, 6.9, 2, 1, "Alkaline metals",[+1] )
Beryllium = Element("Beryllium", "Be", 4, 9.0, 2, 2, "Alkaline earth metals",[+2] )
Boron = Element("Boron", "B", 5, 10.8, 2, 13, "Others no metals",[+3,-3] )
Carbon = Element("Carbon", "C", 6, 12, 2, 14, "Others no metals",[+2,+4] )
Nitrogen = Element("Nitrogen", "N", 7, 14, 2, 15, "Others no metals",[+1,+2,+3,+4,+5,-3] )
Oxygen = Element("Oxygen", "O", 8, 16, 2, 16, "Others no metals",[-2, -1, +2] )
Fluor = Element("Fluor", "F", 9, 19, 2, 17, "Halogen",[-1] )
Neon = Element("Neon", "Ne", 10, 20.2, 2, 18, "Noble gases",[0] )
Sodium = Element("Sodium", "Na", 11, 23, 3, 1, "Alkaline metals",[+1] )
Magnesium = Element("Magnesium", "Mg", 12, 24.3, 3, 2, "Alkaline earth metals",[+2] )
Aluminum = Element("Aluminum", "Al", 13, 27, 3, 13, "Others metals",[+3] )
Silicon = Element("Silicon", "Si", 14, 28.1, 3, 14, "Others no metals",[+4,-4] )
Phosphorus = Element("Phosphorus", "P", 15, 31, 3, 15, "Others no metals",[+3,+5,-3] )
Sulfur = Element("Sulfur", "S", 16, 32.1, 3, 16, "Others no metals",[+2,+4,+6,-2] )
Chlorine = Element("Chlorine", "Cl", 17, 35.5, 3, 17, "Others no metals",[+1,+3,+5,+7,-1] )
Argon = Element("Argon", "Ar", 18, 39.9, 3, 18, "Noble gases",[0] )
Potassium = Element("Potassium", "K", 19, 39.1, 4, 1, "Alkaline metals",[+1] )
Calcium = Element("Calcium", "Ca", 20, 40.1, 4, 2, "Alkaline earth metals",[+2] )
Scandium = Element("Scandium", "Sc", 21, 45, 4, 3, "Transition metals" ) 
Titanium = Element("Titanium", "Ti", 22, 47.9, 4, 4, "Transition metals" )
Vanadium = Element("Vanadium", "V", 23, 50.9, 4, 5, "Transition metals" ) 
Chromium = Element("Chromium", "Ch", 24, 52, 4, 6, "Transition metals",[+2,+3,+6] ) 
Manganese  = Element("Manganese", "Mn", 25, 54.9, 4, 7, "Transition metals",[+2, +3, +4, +6 , +7] )
Iron = Element("Iron", "Fe", 26, 55.8, 4, 8, "Transition metals",[+2,+3] )
Cobalt = Element("Cobalt", "Co", 27, 58.9, 4, 9, "Transition metals" )
Nickel = Element("Nickel", "Ni", 28, 58.7, 4, 10, "Transition metals",[+2,+3] )
Copper= Element("Copper", "Cu", 29, 63.5, 4, 11, "Transition metals",[+1,+2] )
Zinc= Element("Zinc", "Zn", 30, 65.4, 5, 12, "Transition metals",[+2] )
Gallium = Element("Gallium", "Ga", 31, 69.7, 4, 13, "Others metals" )
Germanium = Element("Germanium", "Ge", 32, 72.6, 4, 14, "Others metals" )
Arsenic = Element("Arsenic", "As", 33, 74.9, 4, 15, "Others no metals",[+3, +5, -3] )
Selenium = Element("Selenium", "Se", 34, 79, 4, 16, "Others no metals",[+2,+4,+6,-2] )
Bromine = Element("Bromine", "Br", 35, 79.9, 4, 17, "Halogens",[+1,+3,+5,+7,-1] )
Kypton  = Element("Kypton", "Kr", 36, 83.8, 4, 18, "Noble gases",[0] )
Rubidium = Element("Rubidium", "Rb", 37, 85.5, 5, 1, "Alkaline metals",[+1] )
Strontium = Element("Strontium", "Sr", 38, 87.6, 5, 2, "Alkaline earth metals",[+2] )
Yttrium = Element("Yttrium", "Y", 39, 88.9, 5, 3, "Transition metals" ) 
Zirconium = Element("Zirconium", "Zr", 40, 91.2, 5, 4, "Transition metals" )
Niobium = Element("Niobium", "Nb", 41, 92.9, 5, 5, "Transition metals" ) 
Molybdenum = Element("Molybdenum", "Mo", 42, 95.9, 5, 6, "Transition metals" ) 
Technetium = Element("Technetium", "Tc", 43, 97.9, 5, 7, "Transition metals" )
Ruthenium = Element("Ruthenium", "Ru", 44, 101.1, 5, 8, "Transition metals" )
Rhodium = Element("Rhodium", "Rh", 45, 102.9, 5, 9, "Transition metals" )
Paladium = Element("Paladium", "Pd", 46, 106.4, 5, 10, "Transition metals",[+2,+4] ) 
Silver = Element("Silver", "Ag", 47, 107.9, 5, 11, "Transition metals",[+1] )
Cadmium = Element("Cadmium", "Cd", 48, 112.4, 5, 12, "Transition metals",[+2] )
Indium = Element("Indium", "In", 49, 114.8, 5, 13, "Others metals" )
Tin = Element("Tin", "Sn", 50, 118.7, 5, 14, "Others metals",[+2,+4] )
Antimony = Element("Antimony", "Sb", 51, 121.8, 5, 15, "Others metals",[+3,+5,-3] )
Tellurium = Element("Tellurium", "Te", 52, 127.6, 5, 16, "Others no metals",[+2,+4,+6,-2] )
Iodine = Element("Iodine", "I", 53, 126.9, 5, 17, "Halogens",[+1,+3,+5,+7,-1] )
Xenon = Element("Xenon", "Xe", 54, 131.3, 5, 18, "Noble gases",[0] )
Cesium = Element("Cesium", "Cs", 55, 132.9, 6, 1, "Transition metal",[+1] )
Barium = Element("Barium", "Ba", 56, 137.3, 6, 2, "Transition metal",[+2] )
Lanthanum = Element("Lanthanum", "La", 57, 138.9, 6, 3, "Lantanids" )
Cerium = Element("Cerium", "Ce", 58, 140.1, 6, 4, "Lantanids" )
Praseodymium = Element("Praseodymium", "Pr", 59, 140.9, 6, 5, "Lantanids" )
Neodymium = Element("Neodymium", "Nd", 60, 144.2, 6, 6, "Lantanids" )
Promethium = Element("Promethium", "Pm", 61, 145, 6, 7, "Lantanids" )
Samarium = Element("Samarium", "Sm", 62, 150.4, 6, 8, "Lantanids" )
Europium = Element("Europium", "Eu", 63, 152, 6, 9, "Lantanids" )
Gadolinium = Element("Gadolinium", "Gd", 64, 157.2, 6, 10, "Lantanids" )
Terbium = Element("Terbium", "Tb", 65, 158.9, 6, 11, "Lantanids" )
Dysprosium = Element("Dysprosium", "Dy", 66, 162.5, 6, 12, "Lantanids" )
Holmium = Element("Holmium", "Ho", 67, 164.9, 6, 13, "Lantanids" )
Erbium = Element("Erbium", "Er", 68, 167.3, 6, 14, "Lantanids" )
Thulium = Element("Thulium", "Tm", 69, 168.9, 6, 15, "Lantanids" )
Ytterbium = Element("Ytterbium", "Yb", 70, 173, 6, 16, "Lantanids" )
Lutetium = Element("Lutetium", "Lu", 71, 175, 6, 17, "Lantanids" )
Hafnium = Element("Hafnium", "Hf", 72, 178.5, 6, 4, "Transition metal" )
Tantalum = Element("Tantalum", "Ta", 73, 180.9, 6, 5, "Transition metal" )
Tungsten = Element("Tungsten", "W", 74, 183.58, 6, 6, "Transition metal" )
Rhenium = Element("Rhenium", "Re", 75, 186.2, 6, 7, "Transition metal" ) 
Osmium = Element("Osmium", "Os", 76, 190.2, 6, 8, "Transition metal" ) 
Iridium = Element("Iridium", "Ir", 77, 192.2, 6, 9, "Transition metal" )
Platinum = Element("Platinum", "Pt", 78, 195.1, 6, 10, "Transition metal",[+2,+4] ) 
Gold = Element("Gold", "Au", 79, 197, 6, 11, "Transition metal",[+1,+3] )
Mercury = Element("Mercury", "Hg", 80, 200.6, 6, 12, "Transition metal",[+1,+2] )
Thallium = Element("Thallium", "Tl", 81, 204.4, 6, 13, "Others metals" ) 
Lead = Element("Lead", "Pb", 82, 207.2, 6, 14, "Others metals",[+2,+4] ) 
Bismuth = Element("Bismuth", "Bi", 83, 209, 6, 15, "Others metals",[+3,+5] )  
Polonium = Element("Polonium", "Po", 84, 209, 6, 16, "Others metals" )  
Astatine = Element("Astatine", "At", 85, 210, 6, 17, "Others no metal" ) 
Radon = Element("Radon", "Rn", 86, 222, 6, 18, "Noble gases",[0] )
Francium = Element("Francium", "Fr", 87, 223, 7, 1, "Alkaline metals" ) 
Radium = Element("Radium", "Ra", 88, 226, 7, 2, "Alkaline earth metals" ) 
Actinium = Element("Actinium", "Ac", 89, 227, 7, 3, "Actinides" )

Thorium = Element("Thorium", "Th", 90, 232, 7, 4, "Actinides" )
Protactinium = Element("Protactinium", "Pa", 91, 231, 7, 5, "Actinides" )
Uranium = Element("Uranium", "U", 92, 238, 7, 6, "Actinides" )
Neptuninum = Element("Neptuninum", "Np", 93, 237, 7, 7, "Actinides" )
Plutonium = Element("Plutonium", "Pu", 94, 244, 7, 8 , "Actinides" )
Americium = Element("Americium", "Am", 95, 243, 7, 9, "Actinides" )
Curium = Element("Curium", "Cm", 96, 247, 7, 10, "Actinides" ) 
Berkelium = Element("Berkelium", "Bk", 97, 247, 7, 11, "Actinides" )
Californium = Element("Californium", "Cf", 98, 251, 7, 12, "Actinides" )
Einsteinium = Element("Einsteinium", "Es", 99, 252, 7, 13, "Actinides" ) 
Fermium = Element("Fermium", "Fm", 100, 257, 7, 14, "Actinides" )
Mendelevium = Element("Mendelevium", "Md", 101, 258, 7, 15, "Actinides" )
Nobelium = Element("Nobelium", "No", 102, 259, 7, 16, "Actinides" )
Lawrencium = Element("Lawrencium", "Lr", 103, 262, 7, 17, "Actinides" )
Rutherfordium = Element("Rutherfordium", "Rf", 104, 267, 7, 4, "Transition metal" )
Dubnium = Element("Dubnium", "Db", 105, 268, 7, 5, "Transition metal" )
Seaborgium = Element("Seaborgium", "Sg", 106, 271, 7, 6, "Transition metal" )
Bohrium = Element("Bohrium", "Bh", 107, 272, 7, 7, "Transition metal" )
Hassium = Element("Hassium", "Hs", 108, 270, 7, 8, "Transition metal" )
Meitnerium = Element("Meitnerium", "Mt", 109, 276, 7, 9, "Transition metal" ) 
Darmstadtium = Element("Darmstadtium", "Ds", 110, 281, 7, 10, "Transition metal" )
Roentgenium = Element("Roentgenium", "Rg", 111, 280, 7, 11, "Transition metal" )
Copernicium = Element("Copernicium", "Cn", 112, 285, 7, 12, "Transition metal" )
Nihonium = Element("Nihonium", "Nh", 113, 284, 7, 13, "Others metals" )
Flerovium = Element("Flerovium", "Fl", 114, 289, 7, 14, "Others metals" )
Moscovium = Element("Moscovium", "Mc", 115, 288, 7, 15, "Others metals" )
Livermorium = Element("Livermorium", "Lv", 116, 293, 7, 16, "Others metals" )
Tennessine = Element("Tennessine", "Ts", 117, 294, 7, 17, "Halogens" )
Oganesson = Element("Oganesson", "Og", 118, 294, 7, 18, "Noble gases" )

H = Hydrogen
He = Helyum
Li = Lithium
Be = Beryllium
B = Boron
C = Carbon
N = Nitrogen
O = Oxygen
F = Fluor
Ne = Neon
Na = Sodium
Mg = Magnesium 
Al = Aluminum
Si = Silicon
P = Phosphorus
S = Sulfur
Cl = Chlorine
Ar = Argon
K = Potassium
Sc = Scandium
Ti = Titanium
V = Vanadium
Ca = Calcium
Cr = Chromium
Mn = Manganese
Fe = Iron
Co = Cobalt
Ni = Nickel
Cu = Copper
Zn = Zinc
Ga = Gallium
Ge = Germanium
As = Arsenic
Se = Selenium
Br = Bromine
Kr = Kypton 
Rb = Rubidium
Sr = Strontium
Y = Yttrium
Zr = Zirconium
Nb = Niobium
Mo = Molybdenum
Tc = Technetium
Ru = Ruthenium
Rh = Rhodium
Pd = Paladium
Ag = Silver
Cd = Cadmium
In = Indium
Sn = Tin
Sb = Antimony
Te = Tellurium
I = Iodine
Xe = Xenon
Cs = Cesium
Ba = Barium
La = Lanthanum
Ce = Cerium
Pr = Praseodymium
Nd = Neodymium
Pm = Promethium
Sm = Samarium
Eu = Europium
Gd = Gadolinium
Tb = Terbium
Dy = Dysprosium
Ho = Holmium
Er = Erbium
Tm = Thulium
Yb = Ytterbium
Lu = Lutetium
Hf = Hafnium
Ta = Tantalum
W = Tungsten
Re = Rhenium
Os = Osmium
Ir = Iridium
Pt = Platinum
Au = Gold
Hg = Mercury
Tl = Thallium
Pb = Lead
Bi = Bismuth
Po = Polonium
At = Astatine
Rn = Radon
Fr = Francium
Ra = Radium
Ac = Actinium
Th = Thorium
Pa = Protactinium
U = Uranium
Np = Neptuninum
Pu = Plutonium
Am = Americium
Cm = Curium
Bk = Berkelium
Cf = Californium
Es = Einsteinium
Fm = Fermium
Md = Mendelevium
No = Nobelium
Lr = Lawrencium
Rf = Rutherfordium
Db = Dubnium
Sg = Seaborgium
Bh = Bohrium
Hs = Hassium
Mt = Meitnerium
Ds = Darmstadtium
Rg = Roentgenium
Cn = Copernicium
Nh = Nihonium
Fl = Flerovium
Mc = Moscovium
Lv = Livermorium
Ts = Tennessine
Og = Oganesson

elements_list = [H,He,Li,Be,B,C,N,O,F,Ne,Na,Mg,Al,Si,P,S,Cl,Ar,K,Sc,Ti,V,Ca,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr,Rb,Sr,Y,Zr,Nb,Mo,Tc,
                 Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe,Cs,Ba,La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu,Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,
                 Po,At,Rn,Fr,Ra,Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr,Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og]

electronegativity_list = [F, Cl, Br, At, O, S, Se, Te, Po, H, N, P, As, Sb, Bi, C, Si, Ge, Sn, Pb, B, Al, Ga, In, Tl, Zn, Cd, Hg, Cu, Ag, Au,
                      Rg, Ni, Pd, Pt, Ds, Co, Rh, Ir, Mt, Fe, Ru, Os, Hs, Mn, Tc, Re, Bh, Cr, Mo, W, Sg, V, Nb, Ta, Db, Ti, Zr, Hf,  Rf, 
                      Sc, Y, La, Lu, Ac, Lr, Be, Mg, Ca, Sr, Ba, Ra, Li, Na, K, Rb, Cs, Fr, He, Ne, Ar, Kr, Xe, Rn]     

string_numbers = [ number for number in range (100) ]

prefixes = ["","mono", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca"]

metals = []
no_metals = []
noble_gases =[]
for element in elements_list:
    if element.type == "Noble gases":
        noble_gases.append(element)
    elif element.type == "Halogens" or element.type == "Others no metals":
        no_metals.append(element)
    else: 
        metals.append(element)
        
def get_element_object(expression):
        for symbol in elements_list:
            if expression == symbol.X:
                element_object = symbol
                return element_object
    
def electronic_configuration(element):
        electrons_number = element.Z
        
        configuration = ""
        
        orbitals = ["s","p","d","f"]
        
        electronic_configuration_by_group = {1:"s(1)",2:"s(2)"} #3:,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
        
        max_electrons_per_orbital = {"s":2, "p":6, "d": 10, "f":14}
        
        #For the moment, we print superindices between parenthesis()            
        while electrons_number >= 1:
            
            if "1s" not in configuration:
                if electrons_number >=2:
                    configuration = "1s(2)"
                    electrons_number -= 2
                else:
                    configuration = "1s(1)"
                    electrons_number -= 1
                
            elif "2s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "2s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "2s(1)"
                    electrons_number -= 1
            
            elif "2p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "2p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"2p({electrons_number})"
                    electrons_number = 0
                            
            elif "3s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "3s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "3s(1)"
                    electrons_number -= 1
            
            elif "3p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "3p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"3p({electrons_number})"
                    electrons_number = 0
            
            elif "4s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "4s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "4s(1)"
                    electrons_number -= 1
            
            elif "3d" not in configuration:
                if electrons_number >= 10:
                    configuration = configuration + "3d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"3d({electrons_number})"
                    electrons_number = 0
            
            elif "4p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "4p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"4p({electrons_number})"
                    electrons_number = 0
            
            elif "5s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "5s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "5s(1)"
                    electrons_number -= 1
            
            elif "4d" not in configuration:
                if electrons_number >= 10:
                    configuration = configuration + "4d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"4d({electrons_number})"
                    electrons_number = 0
            
            elif "5p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "5p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"5p({electrons_number})"
                    electrons_number = 0
                           
                    
            elif "6s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "6s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "6s(1)"
                    electrons_number -= 1
                
            
            elif "4f" not in configuration and element != La :
                if electrons_number >= 14:
                    configuration = configuration + "4f(14)"
                    electrons_number -= 14
                    
                elif element == Ce:
                    configuration = configuration + "4f(1)"
                    electrons_number -= 1
                    
                elif element == Eu:
                    configuration = configuration + "4f(7)"
                    electrons_number -= 7
                    
                else:
                    configuration = configuration + f"4f({electrons_number})"
                    electrons_number = 0        
                    
            elif "5d" not in configuration:     
                if electrons_number >= 10:
                    configuration = configuration + "5d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"5d({electrons_number})"
                    electrons_number = 0
            
            elif "6p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "6p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"6p({electrons_number})"
                    electrons_number = 0
                    
            elif "7s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "7s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "7s(1)"
                    electrons_number -= 1
                    
                
                    
            elif "5f" not in configuration and element != Ac and element != Th:
                if electrons_number >= 14:
                    configuration = configuration + "5f(14)"
                    electrons_number -= 14
                elif element == Pa:
                    configuration = configuration + "5f(2)"
                    electrons_number -= 2
                elif element == U:
                    configuration = configuration + "5f(3)"
                    electrons_number -= 3
                elif element == Np:
                    configuration = configuration + "5f(4)"
                    electrons_number -= 4
                elif element == Cm:
                    configuration = configuration + "5f(7)"
                    electrons_number -= 7
                else:
                    configuration = configuration + f"5f({electrons_number})"
                    electrons_number = 0
                    
            elif "7p" not in configuration and element == Lr:
                configuration = configuration + "7p(1)"
                electrons_number -= 1
            
            elif "6d" not in configuration:
                if electrons_number >= 10:
                    configuration = configuration + "6d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"6d({electrons_number})"
                    electrons_number = 0
                    
            elif "7p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "7p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"7p({electrons_number})"
                    electrons_number = 0
            
            else:
                return configuration + " Something happened with your electrons"
        return configuration
    
def check_configuration(element):
    periodic_group =  element.group
    configuration = electronic_configuration(element)
    energetic_levels = element.energetic_levels
    Z = element.Z
    
    check_two_digits = False
    
    if configuration [-3] in string_numbers:
        check_two_digits = True
    
    correct_configuration = ""
    configuration_is_correct = False
    
    if periodic_group <= 2:
        correct_configuration = f"s({periodic_group})" 
    elif element == He:
        correct_configuration = "s(2)"
      
    elif element == Ce or element == Lu: 
            correct_configuration = "d(1)"  
     
    elif periodic_group <= 12 or element == Es or element == Fm or element == Md or element == No or element.type == "Lantanids":
        
        if energetic_levels == 6 and Z > 57 and Z < 72:
            
            correct_configuration = f"f({Z-56})"
            
            
        elif energetic_levels == 7 and Z > 93 and Z < 103 and element != Cm:
            
            correct_configuration = f"f({Z-88})"
            
            
        elif energetic_levels == 7 and Z <= 93 and Z > 90 or element == Cm:
            #correct_configuration = f"f({Z-89})"
            correct_configuration = "d(1)"
            
        else: 
            
            correct_configuration = f"d({periodic_group-2})"
            
    elif element == Lr: 
            correct_configuration = "p(1)"
                    
    elif periodic_group <= 18: 
        correct_configuration = f"p({periodic_group - 12})"
    else: 
        return "Something was wrong with the periodic group"
    
    if correct_configuration == configuration[-4:]:
        configuration_is_correct = True
    elif check_two_digits and correct_configuration == configuration[-5:]:
            configuration_is_correct = True
        
    else: 
        return "Something was wrong with the configuration. " + "Currently configuration is: " + configuration + ". Correct configuration is: " + correct_configuration
    
    return configuration_is_correct
    
for element in elements_list: 
    electronic_configuration(element)
  

def assign_name_to_symbol_of_element (abbrev):
    for symbol in elements_list:
        if abbrev == symbol.X:
            element_name = symbol.name
            return element_name
        else:
            new_abbrev = input("Not element coincidence. Please introduce the abbreviation of the element again.")
            assign_name_to_symbol_of_element(new_abbrev)


#This function return the elements with the number of atoms that contains the formula and the charge
def elements_in_formula(formula, atoms_or_charge=None): 
    
    elements_atoms = {} #Number of atoms of each element
    charge = 0 #Charge of elements in formula 

    is_molecule = False

    abbrev_element = ""
    for i in range(len(formula)):
        
        num_of_atoms = 0

        #There is only one if checking the uppercase because is when there is a new element
        if formula[i] in string.ascii_uppercase:
            #This is checking if the next character is lower case e.g. "Fe" or "He" #0 is uppercase, 1 is lowercase, 2 is number
            if i + 1  < len(formula) and formula[i+1] in string.ascii_lowercase: #01, Ul
                abbrev_element = formula[i] + formula[i+1]
                num_of_atoms = 1

                #This is checking if the next character is a number e.g. "Hg2"
                if i + 2 < len(formula) and formula[i+2].isnumeric(): #012 Uln
                    num_of_atoms = int(formula [i+2])
                    
            
            #This is checking if the next character is a number e.g. "N2"    
            elif i + 1 < len(formula) and formula[i+1].isnumeric(): #02 Un
                abbrev_element = formula[i]
                num_of_atoms = int(formula[i+1])
                
            #This is checking if the next character is a new element e.g. "HF"
            elif i + 1  <= len(formula) or formula[i+1] in string.ascii_uppercase:#00 UU or 0 U
                abbrev_element = formula[i]
                num_of_atoms = 1
                                   
    
            else:
                return "Something happened. Check your code "

            elements_atoms[abbrev_element] = num_of_atoms

        #Here we check if there is a parentesis then the formula has charge or is molecule
        elif formula[i] == "(":
    
            if formula[i+1].isnumeric(): #x(n+)
                if formula[i+2] == "+":
                    charge = int(formula[i+1])
                elif formula[i+2] == "-":
                    charge = -(int(formula[i+1]))
                
            elif formula[i+1] == "+": #x(+)
                charge = 1
            elif formula[i+1] == "-": #x(-)
                charge = -1

            elif formula[i+1] in string.ascii_uppercase:#x(y)
                is_molecule = True
            else: 
                return "Wrong formula"

            pass
                
    if atoms_or_charge == "atoms":
        return elements_atoms
    elif atoms_or_charge == "charge":
        return charge
    else:
        return elements_atoms, charge


def classification_of_compounds(formula):
    compounds_are = ["simple", "binary", "tertiary", "quaternary", "complex"]
    elements_of_formula_to_classify = elements_in_formula(formula, "atoms")
    quantity_of_elements = len(elements_of_formula_to_classify) 
    
    if quantity_of_elements >= 5:
        compound_is = "complex"
    else:
        compound_is = compounds_are[quantity_of_elements-1]
    
    return compound_is

def name_formula_simple (formula, is_anion = False, is_cation = False, return_with_charge = False):
    name = ""
    
    prefixes = ["","mono", "di", "tri", "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca"]

    compound = classification_of_compounds(formula)
    atoms_in_elements, charge = elements_in_formula(formula)

    is_anion = charge < 0
    is_cation = charge > 0
    is_not_ion = charge == 0
    
    #names_of_elements = []

    element_name = ""
    prefix = ""

    for element in compound:
        element_name = assign_name_to_symbol_of_element(element)
        number_of_atoms = compound[element]
        prefix = prefixes[number_of_atoms]
        #names_of_elements.append(element_name)

    electrons_balance = charge

    if is_cation: 
        charge_ = "(" + str(abs(electrons_balance)) + "+" + ")"
        

    if is_anion:
        charge_ ="(" + str(abs(electrons_balance)) + "-" + ")"

        suffix = "ide"
        if element_name == "Hydrogen" or element_name == "Nitrogen":
            element_name = element_name.replace("ogen", suffix) 
        elif element_name[-3:] == "ium": 
            element_name = element_name.replace("ium", suffix)
        elif element_name[-2:] == "on":
            element_name = element_name.replace("on", suffix)
        elif element_name == "Oxygen": 
            element_name = "Oxide"
        elif element_name == "Phosporus":
            element_name == element_name.replace("orus", suffix)
        elif element_name == "Sulfur":
            element_name = element_name.replace("ur", suffix)
        elif element_name [-3:] == "ine":
            element_name == element_name.replace("ine", suffix)  
        elif element_name == "Antimony":
            element_name == element_name.replace("y", suffix)
        else:
             element_name = element_name + suffix

    name = prefix + element_name + charge_ 

    return name

def main():
    formula = input("What formula you want to name?\nPlease write the number after the name of the element,  if there are more than one atom(e.g. N2), and if it has charge between parenthesis(e.g. Fe(3+)). If it has both conditions write it together(e.g. Hg2(2+)):\n")

    election = input("What type of name you want to know? \n 1. Name with prefixes. \n 2. Name with oxidation number. \n 3. Name with number of charge. \n 4. All of them. \n")
    if election is not int or election < 1 or election > 4:
        election = input("Please introduce a number between 1 and 4")
    
    if election == 1:
        print(f"The name with prefixes of {formula} is:" )
        print(prefixes_name(formula))
    elif election == 2:
        print(f"The name with oxidation number of {formula} is:" )
        print(oxidation_name(formula))
    elif election == 3:
        print(f"The name with charge number of {formula} is:" )
        print(charge_name(formula))
    elif election == 4: 
        print("Formula              Prefixes                Oxidation number                Charge number")
        print(f"{formula}", prefixes_name(formula), oxidation_name(formula), charge_name(formula))






