import string
def dictionary_inside(dictionary):
        for key in dictionary:
            if type(key) == dict:
                return key


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
    
    def check_configuration(element, configuration):
        periodic_group =  element.group
        #configuration = electronic_configuration(element)
        energetic_levels = element.energetic_levels
        Z = element.Z

        check_two_digits = False

        if configuration [-3].isnumeric():
            check_two_digits = True

        correct_configuration = ""
        configuration_is_correct = False

        if periodic_group <= 2:
            correct_configuration = f"s({periodic_group})" 
        elif element == He:
            correct_configuration = "s(2)"

        elif element == Ce or element == Lu: 
                correct_configuration = "d(1)"  

        elif periodic_group <= 12 or element == Es or element == Fm or element == Md or element == No or element.type == "Lantanid":

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

    def electronic_configuration(element):
        electrons_number = element.Z
        
        configuration = ""
        
        orbitals = ["s","p","d","f"]
        
        electronic_configuration_by_group = {1:"s(1)", 2:"s(2)"} #3:,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
        
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

        if element.check_configuration(configuration):
            return configuration

def get_element_object(abbrev):
        for symbol in elements_list:
            if abbrev == symbol.X:
                element_object = symbol
                return element_object

def get_element_name(abbrev):
    for symbol in elements_list:
        if abbrev == symbol.X:
            element_name = symbol.name
            return element_name

#Element objects          
Hydrogen = Element("Hydrogen", "H", 1, 1, 1, 1, "Non-Metal",[+1,-1])
H = Hydrogen
Helyum = Element("Helyum", "He", 2, 4, 1, 18, "Noble gas",[0] )
He = Helyum
Lithium = Element("Lithium", "Li", 3, 6.9, 2, 1, "Alkaline metal",[+1] )
Li = Lithium
Beryllium = Element("Beryllium", "Be", 4, 9.0, 2, 2, "Alkaline earth metal",[+2] )
Be = Beryllium
Boron = Element("Boron", "B", 5, 10.8, 2, 13, "Metalloid",[+3,-3] )
B = Boron
Carbon = Element("Carbon", "C", 6, 12, 2, 14, "Non-Metal",[+2,+4] )
C = Carbon
Nitrogen = Element("Nitrogen", "N", 7, 14, 2, 15, "Non-Metal",[+1,+2,+3,+4,+5,-3] )
N = Nitrogen
Oxygen = Element("Oxygen", "O", 8, 16, 2, 16, "Non-Metal",[-2, -1, +2] )
O = Oxygen
Fluor = Element("Fluor", "F", 9, 19, 2, 17, "Halogen",[-1] )
F = Fluor
Neon = Element("Neon", "Ne", 10, 20.2, 2, 18, "Noble gas",[0] )
Ne = Neon
Sodium = Element("Sodium", "Na", 11, 23, 3, 1, "Alkaline metal",[+1] )
Na = Sodium
Magnesium = Element("Magnesium", "Mg", 12, 24.3, 3, 2, "Alkaline earth metal",[+2] )
Mg = Magnesium 
Aluminum = Element("Aluminum", "Al", 13, 27, 3, 13, "Post-transition metal",[+3] )
Al = Aluminum
Silicon = Element("Silicon", "Si", 14, 28.1, 3, 14, "Metalloid",[+4,-4] )
Si = Silicon
Phosphorus = Element("Phosphorus", "P", 15, 31, 3, 15, "Non-Metal",[+3,+5,-3] )
P = Phosphorus
Sulfur = Element("Sulfur", "S", 16, 32.1, 3, 16, "Non-Metal",[+2,+4,+6,-2] )
S = Sulfur
Chlorine = Element("Chlorine", "Cl", 17, 35.5, 3, 17, "Non-Metal",[+1,+3,+5,+7,-1] )
Cl = Chlorine
Argon = Element("Argon", "Ar", 18, 39.9, 3, 18, "Noble gas",[0] )
Ar = Argon
Potassium = Element("Potassium", "K", 19, 39.1, 4, 1, "Alkaline metal",[+1] )
K = Potassium
Calcium = Element("Calcium", "Ca", 20, 40.1, 4, 2, "Alkaline earth metal",[+2] )
Ca = Calcium
Scandium = Element("Scandium", "Sc", 21, 45, 4, 3, "Transition metal" ) 
Sc = Scandium
Titanium = Element("Titanium", "Ti", 22, 47.9, 4, 4, "Transition metal" )
Ti = Titanium
Vanadium = Element("Vanadium", "V", 23, 50.9, 4, 5, "Transition metal" ) 
V = Vanadium
Chromium = Element("Chromium", "Ch", 24, 52, 4, 6, "Transition metal",[+2,+3,+6] ) 
Cr = Chromium
Manganese  = Element("Manganese", "Mn", 25, 54.9, 4, 7, "Transition metal",[+2, +3, +4, +6 , +7] )
Mn = Manganese
Iron = Element("Iron", "Fe", 26, 55.8, 4, 8, "Transition metal",[+2,+3] )
Fe = Iron
Cobalt = Element("Cobalt", "Co", 27, 58.9, 4, 9, "Transition metal" )
Co = Cobalt
Nickel = Element("Nickel", "Ni", 28, 58.7, 4, 10, "Transition metal",[+2,+3] )
Ni = Nickel
Copper= Element("Copper", "Cu", 29, 63.5, 4, 11, "Transition metal",[+1,+2] )
Cu = Copper
Zinc= Element("Zinc", "Zn", 30, 65.4, 5, 12, "Transition metal",[+2] )
Zn = Zinc
Gallium = Element("Gallium", "Ga", 31, 69.7, 4, 13, "Post-transition metal" )
Ga = Gallium
Germanium = Element("Germanium", "Ge", 32, 72.6, 4, 14, "Metalloid" )
Ge = Germanium
Arsenic = Element("Arsenic", "As", 33, 74.9, 4, 15, "Metalloid",[+3, +5, -3] )
As = Arsenic
Selenium = Element("Selenium", "Se", 34, 79, 4, 16, "Non-Metal",[+2,+4,+6,-2] )
Se = Selenium
Bromine = Element("Bromine", "Br", 35, 79.9, 4, 17, "Halogen",[+1,+3,+5,+7,-1] )
Br = Bromine
Kypton  = Element("Kypton", "Kr", 36, 83.8, 4, 18, "Noble gas",[0] )
Kr = Kypton 
Rubidium = Element("Rubidium", "Rb", 37, 85.5, 5, 1, "Alkaline metal",[+1] )
Rb = Rubidium
Strontium = Element("Strontium", "Sr", 38, 87.6, 5, 2, "Alkaline earth metal",[+2] )
Sr = Strontium
Yttrium = Element("Yttrium", "Y", 39, 88.9, 5, 3, "Transition metal" ) 
Y = Yttrium
Zirconium = Element("Zirconium", "Zr", 40, 91.2, 5, 4, "Transition metal" )
Zr = Zirconium
Niobium = Element("Niobium", "Nb", 41, 92.9, 5, 5, "Transition metal" ) 
Nb = Niobium
Molybdenum = Element("Molybdenum", "Mo", 42, 95.9, 5, 6, "Transition metal" ) 
Mo = Molybdenum
Technetium = Element("Technetium", "Tc", 43, 97.9, 5, 7, "Transition metal" )
Tc = Technetium
Ruthenium = Element("Ruthenium", "Ru", 44, 101.1, 5, 8, "Transition metal" )
Ru = Ruthenium
Rhodium = Element("Rhodium", "Rh", 45, 102.9, 5, 9, "Transition metal" )
Rh = Rhodium
Paladium = Element("Paladium", "Pd", 46, 106.4, 5, 10, "Transition metal",[+2,+4] ) 
Pd = Paladium
Silver = Element("Silver", "Ag", 47, 107.9, 5, 11, "Transition metal",[+1] )
Ag = Silver
Cadmium = Element("Cadmium", "Cd", 48, 112.4, 5, 12, "Transition metal",[+2] )
Cd = Cadmium
Indium = Element("Indium", "In", 49, 114.8, 5, 13, "Post-transition metal" )
In = Indium
Tin = Element("Tin", "Sn", 50, 118.7, 5, 14, "Post-transition metal",[+2,+4] )
Sn = Tin
Antimony = Element("Antimony", "Sb", 51, 121.8, 5, 15, "Metalloid",[+3,+5,-3] )
Sb = Antimony
Tellurium = Element("Tellurium", "Te", 52, 127.6, 5, 16, "Metalloid",[+2,+4,+6,-2] )
Te = Tellurium
Iodine = Element("Iodine", "I", 53, 126.9, 5, 17, "Halogen",[+1,+3,+5,+7,-1] )
I = Iodine
Xenon = Element("Xenon", "Xe", 54, 131.3, 5, 18, "Noble gas",[0] )
Xe = Xenon
Cesium = Element("Cesium", "Cs", 55, 132.9, 6, 1, "Transition metal",[+1] )
Cs = Cesium
Barium = Element("Barium", "Ba", 56, 137.3, 6, 2, "Transition metal",[+2] )
Ba = Barium
Lanthanum = Element("Lanthanum", "La", 57, 138.9, 6, 3, "Lantanid" )
La = Lanthanum
Cerium = Element("Cerium", "Ce", 58, 140.1, 6, 4, "Lantanid" )
Ce = Cerium
Praseodymium = Element("Praseodymium", "Pr", 59, 140.9, 6, 5, "Lantanid" )
Pr = Praseodymium
Neodymium = Element("Neodymium", "Nd", 60, 144.2, 6, 6, "Lantanid" )
Nd = Neodymium
Promethium = Element("Promethium", "Pm", 61, 145, 6, 7, "Lantanid" )
Pm = Promethium
Samarium = Element("Samarium", "Sm", 62, 150.4, 6, 8, "Lantanid" )
Sm = Samarium
Europium = Element("Europium", "Eu", 63, 152, 6, 9, "Lantanid" )
Eu = Europium
Gadolinium = Element("Gadolinium", "Gd", 64, 157.2, 6, 10, "Lantanid" )
Gd = Gadolinium
Terbium = Element("Terbium", "Tb", 65, 158.9, 6, 11, "Lantanid" )
Tb = Terbium
Dysprosium = Element("Dysprosium", "Dy", 66, 162.5, 6, 12, "Lantanid" )
Dy = Dysprosium
Holmium = Element("Holmium", "Ho", 67, 164.9, 6, 13, "Lantanid" )
Ho = Holmium
Erbium = Element("Erbium", "Er", 68, 167.3, 6, 14, "Lantanid" )
Er = Erbium
Thulium = Element("Thulium", "Tm", 69, 168.9, 6, 15, "Lantanid" )
Tm = Thulium
Ytterbium = Element("Ytterbium", "Yb", 70, 173, 6, 16, "Lantanid" )
Yb = Ytterbium
Lutetium = Element("Lutetium", "Lu", 71, 175, 6, 17, "Lantanid" )
Lu = Lutetium
Hafnium = Element("Hafnium", "Hf", 72, 178.5, 6, 4, "Transition metal" )
Hf = Hafnium
Tantalum = Element("Tantalum", "Ta", 73, 180.9, 6, 5, "Transition metal" )
Ta = Tantalum
Tungsten = Element("Tungsten", "W", 74, 183.58, 6, 6, "Transition metal" )
W = Tungsten
Rhenium = Element("Rhenium", "Re", 75, 186.2, 6, 7, "Transition metal" ) 
Re = Rhenium
Osmium = Element("Osmium", "Os", 76, 190.2, 6, 8, "Transition metal" ) 
Os = Osmium
Iridium = Element("Iridium", "Ir", 77, 192.2, 6, 9, "Transition metal" )
Ir = Iridium
Platinum = Element("Platinum", "Pt", 78, 195.1, 6, 10, "Transition metal",[+2,+4] ) 
Pt = Platinum
Gold = Element("Gold", "Au", 79, 197, 6, 11, "Transition metal",[+1,+3] )
Au = Gold
Mercury = Element("Mercury", "Hg", 80, 200.6, 6, 12, "Transition metal",[+1,+2] )
Hg = Mercury
Thallium = Element("Thallium", "Tl", 81, 204.4, 6, 13, "Post-transition metal" ) 
Tl = Thallium
Lead = Element("Lead", "Pb", 82, 207.2, 6, 14, "Post-transition metal",[+2,+4] ) 
Pb = Lead
Bismuth = Element("Bismuth", "Bi", 83, 209, 6, 15, "Post-transition metal",[+3,+5] )  
Bi = Bismuth
Polonium = Element("Polonium", "Po", 84, 209, 6, 16, "Metalloid" )  
Po = Polonium
Astatine = Element("Astatine", "At", 85, 210, 6, 17, "Halogen" ) 
At = Astatine
Radon = Element("Radon", "Rn", 86, 222, 6, 18, "Noble gas",[0] )
Rn = Radon
Francium = Element("Francium", "Fr", 87, 223, 7, 1, "Alkaline metal" ) 
Fr = Francium
Radium = Element("Radium", "Ra", 88, 226, 7, 2, "Alkaline earth metal" ) 
Ra = Radium
Actinium = Element("Actinium", "Ac", 89, 227, 7, 3, "Actinide" )
Ac = Actinium
Thorium = Element("Thorium", "Th", 90, 232, 7, 4, "Actinide" )
Th = Thorium
Protactinium = Element("Protactinium", "Pa", 91, 231, 7, 5, "Actinide" )
Pa = Protactinium
Uranium = Element("Uranium", "U", 92, 238, 7, 6, "Actinide" )
U = Uranium
Neptuninum = Element("Neptuninum", "Np", 93, 237, 7, 7, "Actinide" )
Np = Neptuninum
Plutonium = Element("Plutonium", "Pu", 94, 244, 7, 8 , "Actinide" )
Pu = Plutonium
Americium = Element("Americium", "Am", 95, 243, 7, 9, "Actinide" )
Am = Americium
Curium = Element("Curium", "Cm", 96, 247, 7, 10, "Actinide" ) 
Cm = Curium
Berkelium = Element("Berkelium", "Bk", 97, 247, 7, 11, "Actinide" )
Bk = Berkelium
Californium = Element("Californium", "Cf", 98, 251, 7, 12, "Actinide" )
Cf = Californium
Einsteinium = Element("Einsteinium", "Es", 99, 252, 7, 13, "Actinide" ) 
Es = Einsteinium
Fermium = Element("Fermium", "Fm", 100, 257, 7, 14, "Actinide" )
Fm = Fermium
Mendelevium = Element("Mendelevium", "Md", 101, 258, 7, 15, "Actinide" )
Md = Mendelevium
Nobelium = Element("Nobelium", "No", 102, 259, 7, 16, "Actinide" )
No = Nobelium
Lawrencium = Element("Lawrencium", "Lr", 103, 262, 7, 17, "Actinide" )
Lr = Lawrencium
Rutherfordium = Element("Rutherfordium", "Rf", 104, 267, 7, 4, "Transition metal" )
Rf = Rutherfordium
Dubnium = Element("Dubnium", "Db", 105, 268, 7, 5, "Transition metal" )
Db = Dubnium
Seaborgium = Element("Seaborgium", "Sg", 106, 271, 7, 6, "Transition metal" )
Sg = Seaborgium
Bohrium = Element("Bohrium", "Bh", 107, 272, 7, 7, "Transition metal" )
Bh = Bohrium
Hassium = Element("Hassium", "Hs", 108, 270, 7, 8, "Transition metal" )
Hs = Hassium
Meitnerium = Element("Meitnerium", "Mt", 109, 276, 7, 9, "Transition metal" ) 
Mt = Meitnerium
Darmstadtium = Element("Darmstadtium", "Ds", 110, 281, 7, 10, "Transition metal" )
Ds = Darmstadtium
Roentgenium = Element("Roentgenium", "Rg", 111, 280, 7, 11, "Transition metal" )
Rg = Roentgenium
Copernicium = Element("Copernicium", "Cn", 112, 285, 7, 12, "Transition metal" )
Cn = Copernicium
Nihonium = Element("Nihonium", "Nh", 113, 284, 7, 13, "Post-transition metal" )
Nh = Nihonium
Flerovium = Element("Flerovium", "Fl", 114, 289, 7, 14, "Post-transition metal" )
Fl = Flerovium
Moscovium = Element("Moscovium", "Mc", 115, 288, 7, 15, "Post-transition metal" )
Mc = Moscovium
Livermorium = Element("Livermorium", "Lv", 116, 293, 7, 16, "Post-transition metal" )
Lv = Livermorium
Tennessine = Element("Tennessine", "Ts", 117, 294, 7, 17, "Halogen" )
Ts = Tennessine
Oganesson = Element("Oganesson", "Og", 118, 294, 7, 18, "Noble gas" )
Og = Oganesson

elements_list = [H,He,
                 Li,Be,B,C,N,O,F,Ne,Na,Mg,Al,Si,P,S,Cl,Ar,
                 K,Sc,Ti,V,Ca,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr,
                 Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe,
                 Cs,Ba,La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu,
                 Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,Po,At,Rn,
                 Fr,Ra,Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr,
                 Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og]

electronegativity_list = [F, Cl, Br, At,
                           O, S, Se, Te, Po,
                             H,
                               N, P, As, Sb, Bi,
                                 C, Si, Ge, Sn, Pb,
                                   B, Al, Ga, In, Tl,
                                     Zn, Cd, Hg,
                                       Cu, Ag, Au, Rg,
                                         Ni, Pd, Pt, Ds,
                                           Co, Rh, Ir, Mt,
                                             Fe, Ru, Os, Hs,
                                               Mn, Tc, Re, Bh,
                                                 Cr, Mo, W, Sg,
                                                   V, Nb, Ta, Db,
                                                    Ti, Zr, Hf, Rf, 
                                                     Sc, Y, La,
                                                      Lu,    Ac,     Lr,
                                                       Be, Mg, Ca, Sr, Ba, Ra,
                                                        Li, Na, K, Rb, Cs, Fr,
                                                        He, Ne, Ar, Kr, Xe, Rn]     

prefixes = ["", 
            "mono",
            "di",
            "tri",
            "tetra",
            "penta",
            "hexa",
            "hepta",
            "octa",
            "nona",
            "deca"]

metals = []
no_metals = []
noble_gases = []

for element in elements_list:
    if element.type == "Noble gas":
        noble_gases.append(element)

    elif element.type == "Halogen" or element.type == "Non-Metal" or element.type == "Post-transition metal" or element == B or element == Si or element == As or element == Te:
        no_metals.append(element)
    
    else: 
        metals.append(element)
        

      
#This function return the elements with the number of atoms that contains the formula and the charge
def elements_in_formula(formula, atoms_or_charge=None): 
    
    elements_atoms = {} #Number of atoms of each element
    charge = 0 #Charge of elements in formula 

    #is_molecule = None
    is_aqueous = False

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
            elif formula[i+1] + formula [i+2] == "aq":
                is_aqueous = True

            elif formula[i+1] in string.ascii_uppercase:#x(y)
                #is_molecule = True #If is molecule it has a group* multiplied by something

                molecule = formula[i+1:formula.index(")")]

                if formula[formula.index(")") + 1].isnumeric():
                    number_of_molecules = int(formula[formula.index(")") + 1])

                elements_atoms[elements_in_formula(molecule, "atoms")] = number_of_molecules

                # elements_atoms_mol = elements_in_formula(molecule, "atoms")

                # for element in elements_atoms_mol:
                #     elements_atoms_mol[element] = elements_atoms_mol[element] * number_of_molecules
                
                # elements_atoms.update(elements_atoms_mol)
                
                

            else: 
                return "Wrong formula. Check the code"

            pass
    #if aqueous:
        #return 
                
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
       
    
    if len(dictionary_inside(elements_in_formula)):
        quantity_of_elements += len(dictionary_inside(elements_in_formula))

    if quantity_of_elements >= 5:
        compound_is = "complex"
    else:
        compound_is = compounds_are[quantity_of_elements-1]

    return compound_is

def prefixes_name(formula):
    atoms_per_elements = elements_in_formula(formula, "atoms")
    
    if classification_of_compounds(formula) == "binary":
        #prefixes_per_element = {}
        name = ""

        for element in atoms_per_elements:
            #prefixes_per_element[element] = prefixes[atoms_per_elements[element]] + get_element_object(element).name.lower()
            name = name + prefixes[atoms_per_elements[element]] + get_element_object(element).name.lower()

def name_anion(element_name):

    suffix = "ide"

    if element_name == "Hydrogen" or element_name == "Nitrogen":
        element_name = element_name.replace("ogen", suffix) 
    elif element_name[-3:] == "ium": 
        element_name = element_name.replace("ium", suffix)
    elif element_name[-2:] == "on":
        element_name = element_name.replace("on", suffix)
    elif element_name == "Oxygen": 
        element_name = "Oxide"
        #if electrons_balance == 2:
            #element_name == "Peroxide"
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

    return element_name.lower()

#Inorganic nomenclature
def name_formula (formula):
    name = ""

    

    compound_is = classification_of_compounds(formula)
    atoms_per_formula = elements_in_formula("atoms")
    charge = elements_in_formula(formula, "charge")

    
    element_names = []

    for element in atoms_per_formula:
            element_name = get_element_name(element)
            number_of_atoms = atoms_per_formula[element]
            element_names.append(prefixes[number_of_atoms] + element_name.lower())

            element_object = get_element_object(element)
            element_types.append(element_object.type)


    if compound_is == "simple":
        element_name = ""
        prefix = prefixes[number_of_atoms]
        
        electrons_balance = charge

        if charge > 0: 
            charge_ = "(" + str(abs(electrons_balance)) + "+" + ")"
        
        elif charge < 0:
            charge_ ="(" + str(abs(electrons_balance)) + "-" + ")"

            element_name = name_anion(element_name)

        else:
            if atoms_per_formula["O"] == 3:
                name = "Ozone"
                return name

        name = prefix + element_name.lower() + charge_ 

    if compound_is == "binary":
        
        ### Type of binary compound
        combined_with_oxigen = False
        is_oxide = False
        is_peroxide = False

        combined_with_hydrogen = False
        is_metal_hydride = False
        is_hydracid = False
        is_parent_hydride = False

        metal_with_no_metal = False #(Salt)
        is_metal = False
        is_not_metal = False

        combination_of_two_no_metals = False
        ###

        parent_hydrides = {#Parent hydrides(hidrurs progenitors) are named with an specific name, although can be named with systematic nomenclature or traditionally if it is in aquous solution
            "HF": "fluorine",       # Hydrofluoric acid
            "HCl": "chlorine",      # Hydrochloric acid
            "HBr": "bromane",       # Hydrobromic acid
            "HI": "iodane",         # Hydroiodic acid
            "H2S": "sulfane",       # Hydrosulfuric acid
            "H2Se": "selenane",     # Hydroselenic acid
            "H2Te": "tellane",      # Hydrotelluric acid
            "AtH": "astatane",      # Hydroastatic acid
            "BH3": "borane",        # Boron trihydride
            "CH4": "methane",       # Methane
            "NH3": "ammonia",       # Ammonia
            "AlH3": "alumane",      # Aluminium hydride
            "SiH4": "silane",       # Silicon hydride
            "PH3": "phosphane",     # Phosphine (Phosphane)
            "GaH3": "gallane",      # Gallium trihydride
            "GeH4": "germane",      # Germanium hydride
            "AsH3": "arsine",       # Arsenic hydride
            "SnH4": "stannane",     # Tin hydride
            "SbH3": "stibine",      # Antimony hydride (Stibine)
            "InH3": "indigane",     # Indium hydride
            "TlH3": "thalane",      # Thallium hydride
            "PbH4": "plumbane",     # Lead hydride
            "BiH3": "bismuthane",   # Bismuth hydride
            "PoH2": "polonane"      # Polonium hydride
        }

        if formula in parent_hydrides:
            name = parent_hydrides[formula]
            return name.capitalize()


        #We start with prefixes, later we search the nomenclature with number of oxidation and with number of charge
        
        
        element_types = []

        for element in atoms_per_formula:
            
            if element == "O":
                combined_with_oxigen = True

                if "Alkaline metal" in element_types or "Alkaline earth metal" in element_types and atoms_per_formula["O"] == 2:
                    is_peroxide = True #Oxidation number of oxigen in the case of peroxide is -1
                    n_oxidation = -1
                    

                    first_element = element_names[0]
                    if first_element == "Hydrogen" and atoms_per_formula["O"] == 1: # Except of H2O
                        is_peroxide = False
                        name = "Water"
                        return name
                    #Peroxide has not nomenclature with number of oxidation or charge because is known that the number of oxidation of peroxide is -1. Then, these nomenclatures will be the same.
                    
                else: 
                    is_oxide = True #Oxidation number of oxigen is -2
                    n_oxidation = -2
            elif is_oxide and element == "H":
                is_hydroxide = True

            elif is_metal and element == "H":
                combined_with_hydrogen = True
                is_metal_hydride = True
            elif element == "H":
                combined_with_hydrogen = True
            elif combined_with_hydrogen and element.group == 16 or element.group == 17:
                is_hydracid = True
            #elif element == "H" and  13 <= element.group <= 17:
                #combined_with_hydrogen = True
                #parent_hydride = True
            elif is_metal and element_object in no_metals:
                metal_with_no_metal

            elif element_object in metals:
                is_metal = True

            elif is_not_metal and element_object in no_metals:
                combination_of_two_no_metals = True

            elif element_object in no_metals:
                is_not_metal = True

        first_element = element_names[0]
        second_element = element_names[1]
        #Names with prefixes
        prefix_first_element = prefixes[atoms_per_formula[first_element]] + first_element.lower()
        prefix_second_element = prefixes[atoms_per_formula[second_element]] + name_anion(second_element)

        if is_peroxide:
            name = prefix_first_element + " peroxide"

        elif is_hydroxide:
            name = "hydroxide"

        elif is_hydracid:
            name = "hydrogen" + " " + name_anion(second_element)

        else:
            name = prefix_first_element + " " + prefix_second_element



        elements_of_formula_to_classify = elements_in_formula(formula, "atoms")



        #names_of_elements.append(element_name)


        pass
    
    if compound_is == "tertiary" or compound_is == "quaternary":

        is_hydroxide = False
        is_oxoacid = False
        is_oxosal = False
        is_ion_heteropolyatomic = False

        for element in atoms_per_formula:
            name = 


        if dictionary_inside(atoms_per_formula):
            pass

        if len(atoms_per_formula) == 2:
            

            part_molecule = dictionary_inside(atoms_per_formula)

            prefix_mol = prefix[atoms_per_formula[part_molecule]]

            name_mol = name_formula(part_molecule)
            


            pass
        


        
        pass


    return name.capitalize()


def oxidation_name(formula):
    pass

# def charge_name(formula):
#     pass

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
        print("Formula      Prefixes        Oxidation number        Charge number")
        print(f"{formula}", prefixes_name(formula), oxidation_name(formula), charge_name(formula))









