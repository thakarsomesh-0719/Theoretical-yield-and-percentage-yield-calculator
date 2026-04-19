# program to calculate theoretical yeild of any chemistry synthesis based on amounts of limiting reagents used.
# Somesh Thakar
# March 2026
def theoretical_yield():
    print("Please balance the reaction coefficients before proceeding")
    print("Identify the limiting reagent in your reaction")
    molar_mass_limiting = float(input("Please enter the molar mass of limiting reagent (g/mol)   "))
    # ---------- taking inputs of the limiting reagent ----------
    mass_or_volume = input("Please enter if mass measurement or volume measurement was used for the limiting reagent   ")
    mass_or_volume = mass_or_volume.lower()
    if mass_or_volume in ("mass", "m"):
    # ---------- conversion of units to grams ---------- 
        while True: 
            mass_limiting_unit = input("Please enter if mass of the limiting reagent was taken in grams(g), milligrams(mg) or kilograms(kg)     ")
            mass_limiting_unit = mass_limiting_unit.lower()
            if mass_limiting_unit in ("grams","g"):
                mass_limiting_g = float(input("Please enter mass of limiting reagent (g)   "))
                break
            elif mass_limiting_unit in ("milligrams", "mg"):
                mass_limiting_mg = float(input("Please enter mass of limiting reagent (mg)   "))
                mass_limiting_g = mass_limiting_mg/1000
                break
            elif mass_limiting_unit in ("kilograms", "kg"):
                mass_limiting_kg = float(input("Please enter mass of limiting reagent (kg)   "))
                mass_limiting_g = mass_limiting_kg * 1000
                break
            else:
                print("I didn't understand that please try again")
        moles_limiting = mass_limiting_g/molar_mass_limiting
    elif mass_or_volume in ("volume", "vol", "v"):
        while True:
        # ---------- Unit conversion to millilitres ---------- 
            density_limiting = float(input("Enter the density of the limiting reagent (g/mL): "))
            volume_limiting_ml_l = input("please enter if volume of limiting reagent is in litres(l) or mililitres(ml)   ")
            volume_limiting_ml_l = volume_limiting_ml_l.lower()
            if volume_limiting_ml_l in ("mililitre","ml") :
                volume_limiting_ml =float(input("Please enter the volume of limiting reagent (ml)   "))
                break
            elif volume_limiting_ml_l in ("litre","l"):
                volume_limiting_l =float(input("Please enter the volume of limiting reagent (l)   "))
                volume_limiting_ml = volume_limiting_l * 1000
                break
            else:
                print("I don't understand that please try again")
        moles_limiting = (volume_limiting_ml * density_limiting) / molar_mass_limiting
    # ---------- calculation of moles of limiting reagent and calculation of theoretical mass of the product ---------- 
    coefficient_product =float(input("Please enter the coefficient of the product   "))
    coefficient_limiting =float(input("Please enter the coefficient of the limiting reagent   "))
    moles_product = (moles_limiting * coefficient_product)/coefficient_limiting
    molar_mass_product =float(input("Please enter the molar mass of the product (g/mol)    "))
    theoretical_mass = moles_product * molar_mass_product
    print(f"Theoretical mass of the product is {theoretical_mass:.3f}g   ")
    return theoretical_mass


def percentage_calculator(theoretical_mass):
    # ---------- Calculation of percentage yield of the product ---------- 
    actual_mass =float(input("Please enter the actual mass of the product obtained (g)   "))
    percentage_yield = (actual_mass / theoretical_mass) * 100
    print(f"The percentage yield of the desired product is {percentage_yield:.3f}% ")
    return percentage_yield


while True:
    theoretical_percentage = input('''Please enter the calculation which you want to perform
    1 for theoretical yield calculation
    2 for percentage yield calculation 
    3 for both the afformentioned calculations
    ''')
    if theoretical_percentage == "1":
        theoretical_yield_val = theoretical_yield()
        break
    elif theoretical_percentage == "2":
        theoretical_mass = float(input("Please enter the theoretical yield of the desired product (g)   "))
        percentage_calculator(theoretical_mass)
        break
    elif theoretical_percentage == "3":
        theoretical_yield = theoretical_yield()
        theoretical_yield_val = float(theoretical_yield)
        percentage_calculator(theoretical_yield_val)
        break
    else:
        print("I didn't understand that, please try again")