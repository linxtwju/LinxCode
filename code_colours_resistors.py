class ColourCode():
    def __init__(self, name, first_digit, second_digit, multiplicateur, Tolerance=None, TCR = None):
        self.name = name;
        self.first_digit = first_digit;
        self.second_digit = second_digit;
        self.multiplicateur = multiplicateur; 
        self.Tolerance = Tolerance;
        self.TCR = TCR;
        
# colours = ["black", "brown", "red", "orange, yellow","green", "blue", "violet", "grey", "white","gold", "silver","none"]
# tolerance_basics = {"brown":1, "red": 2, "green":0.5, "grey" : 0.05} #%


# for i in range(len(colours)):
#     if i < 10:
#         tolerance = None 
#         if colours[i] in tolerance_basics:
#             tolerance = tolerance_basics[colours[i]] 
#         colours_code[colours[i]] = ColourCode(colours[i], i, i, 10**i, tolerance )
#     elif i == 10:
#         colours_code[colours[i]] = ColourCode(colours[i], None, None, 10**-1, 5)
#     elif i == 11:
#          colours_code [colours[i]] =ColourCode(colours[i], None, None, 10**-2, 10) 
#     else: 
#          colours_code[colours[i]] = ColourCode(colours[i], None, None, None, 20)

# def resistence(colour1, colour2, colour3, colour4 = None, colour5 = None, colour6 = None):
#     R = (int(str(colour1.first_digit) + str(colour2.second_digit))) * colour3.multiplicateur 
    
#     Tolerance = None
#     if colour4 == None:
#         Tolerance = 20
#     elif colour5 == None:
#         Tolerance = colour4.Tolerance
#     else:
#         R = (int(str(colour1.first_digit) + str(colour2.second_digit)+str(colour3.second_digit))) * colour4.multiplicateur
#         Tolerance = colour5.Tolerance
    
#     TCR = None
#     if colour6 != None:
#         TCR = colour6.TCR
        
#     string_tolerance = ""
    
#     if Tolerance != None:
#         string_tolerance = "±" + str(Tolerance) + "Ω"
#         if TCR != None:
#             string_tolerance += str(TCR) + " ppm/K"
    
    
    
#     Rn = str(R) + "Ω" + string_tolerance
    
#     return Rn


    

# print(resistence("yellow", "red", "blue"))


Black = ColourCode("Black", 0, 0, 10**0, 0, 100)
Brown = ColourCode("Brown", 1, 1, 10**1, 1, 50)
Red = ColourCode("Red", 2, 2, 10**2, 2, 15)
Orange = ColourCode("Orange", 3, 3, 10**3, 3, 25)
Yellow = ColourCode("Yellow", 4, 4, 10**4, 4, 0)
Green = ColourCode("Green", 5, 5, 10**5,0.5, 0)
Blue = ColourCode("Blue", 6, 6, 10**6, 0.25, 10)
Violet = ColourCode("Violet", 7, 7, 10**7, 0.1, 5)
Grey = ColourCode("Grey", 8, 8, 10**8,  0.05)
White = ColourCode("White", 9, 9, 10**9, 0, 0)
Gold = ColourCode("Gold", None, None, 10**-1, 5)
Silver = ColourCode("Silver", None, None, 10**-2, 10)
# ColourCode("None", None, None, None, 20)      
colours_code = [Black,Brown,Red,Orange,Yellow,Green,Blue,Violet,Grey,White,Gold,Silver]



def calculate_resistence(list_of_index_colours):
    colours = []
    for index_colour in list_of_index_colours:
        colours.append(colours_code[index_colour])
        
    ohms = 0 #ohms
    tolerance = 0 #%
    tcr = 0 #ppm / K
    
    string_tcr = ""
    
    if len(colours) <= 4: 
        ohms = int(str(colours[0].first_digit) + str(colours[1].first_digit)) * colours[2].multiplicateur
        if len(colours) == 3:
            tolerance = 20
        elif len(colours) == 4:
            tolerance = colours[3].Tolerance
        else:
            return "Something was wrong."
    elif len(colours) <= 6: 
        ohms = int(str(colours[0].first_digit) + str(colours[1].first_digit) + str(colours[2].first_digit)) * colours[3].multiplicateur
        tolerance = colours[4].Tolerance
        if len(colours) == 6:
            tcr = colours[5].TCR
            string_tcr = str(tcr) + " ppm/K"
    else:
        return "The length is larger than allowed"
    
    
    
    
    Rn = str(ohms) +   " Ω" +  " ±" + str(tolerance) + " % " + string_tcr
    
    return Rn
    
    
    



def main():
    
    resistance_or_colour = int(input("""What do you want to know?
      1.Resistance of a resistor
      2.Colours of a resistor
      ->  """))
    
    if resistance_or_colour == 1:
        
        number_of_colours = int(input("How many colours have the resistance?(Between 3 and 6)"))
            # if 3 <= number_of_colours <= 6:
            #     invalidate = False
        
        
        
        colours_to_calculate = []
        for i in range(number_of_colours):  
            colour = int(input(f""""           
                Introduce the colours of the resistance (ordered left to right):
                0.Black
                1.Brown
                2.Red
                3.Orange
                4.Yellow
                5.Green
                6.Blue
                7.Violet
                8.Grey
                9.White
                10.Gold
                11.Silver
                
                """))
            colours_to_calculate.append(colour)
            
        print(calculate_resistence(colours_to_calculate))
        
main()
            
        
        
        