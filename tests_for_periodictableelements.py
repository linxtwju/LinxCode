#Tests for periodictableelements 
import Periodictableelements as pte
#Checks 
simple_test_elements = ["O2"]
simple_test_cations = ["Na(+)", "Fe(3+)", "H(+)", "Hg2(2+)"]
simple_test_anions = ["F(-)", "S(2-)", "O(2-)", "N(3-)", "H(-)", "O2(2-)", "C2(2-)"]
binary_test = ["KCl", "Li2O", "MgO", "CO2", "NO", "PH3", "HBr", "RaH2", "B2O3", "Al2Se3", "NH3", "H2O"]
oxide_test = ["CO2", "NO", "Fe2O3", "CaO"]
peroxide_test = ["Li2O2", "CaO2", "H2O2"]
hydride_hydracid_test = ["CuH2", "AgH", "NiH3", "HCl", "HF", "H2S", "HCl(aq)", "HF(aq)", "H2S(aq)"] #
binary_salt_test = ["CaBr2", "NaCl", "Fe2S3"]
two_no_metals_combined = ["SBr2", "CCl4", "P2S3"]
hydroxid_test = ["Mg(OH)2", "Pb(OH)4", "KOH"] 
oxoacid_test = ["HClO", "HClO2", "HClO3", "HClO4", "H2SO2", "H2SO3", "H2SO4","H2CO2", "H2CO3"]
tertiary_test = ["H2SO4", "HClO "]
oxosal_test = ["Mg(BrO)2",  "Au(H2PO4)3", "Ca(ClO4)2", "Cu(IO)2", "K2(Cr2O7)"]
formules_P = ["H3PO5", "H3PO2", "H3PO3", "H3PO4"]
fails = ["Fe2(SO4)3", "Na(HCO3)2"]
oxoanions = ["CrO4(2-)", "MnO4(2-)", "HSO3(-)","Cr2O7(2-)" ]

for formula in oxoanions:
    print(pte.name_formula(formula))

for formula in fails:
    print(pte.name_formula(formula))