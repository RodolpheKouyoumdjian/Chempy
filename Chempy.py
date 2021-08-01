from mendeleev import *
from molmass import Formula

#Info about how to use the program
print('Enter the symbol of any element in the periodic table in order to obtain information about it. Not caps sensitive.')
print('To get the molar mass of a compound, type "mm", press ENTER and then write its formula. Caps sensitive.\n')

def get_info():  # Get info about 1 element
    global molmass
    molmass = 0
    try:
        elem = input('Enter atom name or symbol: ')
        print()
        
        if elem == 'mm':
            
            f = Formula(input('Enter the formula correctly: '))
            print()
            print('Molar mass of compound: ' + str(f.mass))
            print()
            get_info()


        elem = elem.lower().capitalize()
        elem = element(elem)

        print('Name: ' + elem.name)
        print('Symbol: ' + elem.symbol)
        print('Atomic number: ' + str(elem.atomic_number))
        print('Mass number: ' + str(elem.mass_number))
        print('Molar mass: ' + str(elem.mass))
        print('Oxidation states: ' + str(elem.oxistates))
        print('Number of valence electrons: ' + str(elem.nvalence()))
        print('Electrons per shell: ' + str(elem.ec.electrons_per_shell()))
        print('Electronegativity: ' + str(elem.en_pauling))
        a = list(elem.ec.conf.items())
        conf = ''

        for i in range(len(a)):
            for j in range(2):
                conf += str(a[i][0][j])
            conf += str(a[i][1])
            conf += ','
        conf = conf[:-1]

        print('Electronic configuration: ' + conf)
        print()
        get_info()

    except:
        print('Not valid try again')
        print()
        get_info()

get_info()
