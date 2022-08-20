


config = ["1s1", "1s2", "2s1", "2s2", "2p1", "2p2", "2p3", "2p4", "2p5", "2p6", "3s1", "3s2",
                "3p1", "3p2", "3p3", "3p4", "3p5", "3p6", "4s1", "4s2", "3d1", "3d2", "3d3", "3d4",
                "3d5", "3d6", "3d7", "3d8", "3d9", "3d10", "4p1", "4p2", "4p3", "4p4", "4p5", "4p6",
                "5s1", "5s2", "4d1", "4d2", "4d3", "4d4", "4d5", "4d6", "4d7", "4d8", "4d9", "4d10",
                "5p1", "5p2", "5p3", "5p4", "5p5", "5p6", "6s1", "6s2", "4f1", "4f2", "4f3", "4f4",
                "4f5", "4f6", "4f7", "4f8", "4f9", "4f10", "4f11", "4f12", "4f13", "4f14", "5d1", "5d2",
                "5d3", "5d4", "5d5", "5d6","5d7", "5d8", "5d9", "5d10", "6p1", "6p2", "6p^3", "6p4", "6p5",
                "6p6", "7s1", "7s2","5f1", "5f2", "5f3", "5f4", "5f5", "5f6", "5f7", "5f8", "5f9", "5f10",
                "5f11", "5f12", "5f13", "5f14", "6d1", "6d2", "6d3", "6d4", "6d5", "6d6", "6d7", "6d8",
                "6d9", "6d10", "7p1", "7p2", "7p3", "7p4", "7p5","7p6"]



elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K",
              "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb",
              "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs",
              "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
              "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
              "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs",
              "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]  

elementsname = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
                "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorous", "Sulfur", "Chloride", "Argon", "Potassium",
                "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickle",
                "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium",
                "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver",
                "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum",
                "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
                "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten",
                "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium",
                "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
                "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium",
                "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium"]                       


atn = 0
looping = True


while looping:
    ch = input("atomic number or element name: ")
    if ch =="atomic number":
        atn = int(input("Enter atomic number: "))
        while atn==0 or atn<0:
         print("Invalid atomic number")
        break

    elif ch == "element name":
        name = input("Enter element name: ")   


        try:
            atomicNumber = elements.index(name)
        except ValueError:
            atomicNumber = elementsname.index(name)

        atomicNumber = atomicNumber + 1
        break

    else:
        print("invalid")


print("The name of the element :", elementsname[atn])
print("electron configuration : \n" + ' '.join(map(str, config[0:atn])))





