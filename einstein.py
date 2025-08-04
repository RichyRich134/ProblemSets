# E (energy in Joules) = mc^2(mass in kilograms, light speed)
# e represents x10

#Speed of Light in meters per second
LIGHT_SPEED = 2.99792458e8

def main():
    mass = float(input("What is the mass (m) of the resting object in kilograms (kg) ?"))
    energy = mass_energy_equivalence(mass)
    print(f"The rest energy of the object, that means the total energy contained in it's mass, is {energy:.2e} Joules (J)")

def mass_energy_equivalence(mass):
    #mass times light speed, (m/s)
    return mass * LIGHT_SPEED ** 2
    
main()







#Input masss, output energy