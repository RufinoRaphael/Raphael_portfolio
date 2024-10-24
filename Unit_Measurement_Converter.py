convert_from = input("Enter Starting Unit of Measurement (inches, feet, yards): ")

convert_to =  input("Enter Unit of Measurement ro Convert to(inches, feet, yards): ")


if convert_from.lower() in ["inches", "in", "Inches", "inch"]:
    number_of_inches = int(input("Enter Starting Measurement in inches: "))
    if convert_to.lower() in  ["feet", "foot", "ft"]:
        print("Result: " + str(number_of_inches) + " inches = " +  str(round(number_of_inches/ 12,2)) + " Feet")
    elif convert_to.lower() in  ["yards", "yard", "yds", "yd"]:
        print("Result: " + str(number_of_inches) + " inches = " +  str(round(number_of_inches/ 36,2)) + " Yards")
    else:
        print("Your input was incorrect")


elif convert_from.lower() in  ["feet", "foot", "ft"]:
    number_of_feet = int(input("Enter Starting Measurement in feet: "))
    if convert_to.lower() in ["inches", "in", "Inches", "inch"]:
        print("Result: " + str(number_of_feet) + " feet = " +  str(round(number_of_feet* 12)) + " Inches")
    elif convert_to.lower() in  ["yards", "yard", "yds", "yd"]:
        print("Result: " + str(number_of_feet) + " feet = " +  str(round(number_of_feet / 3,2)) + " Yards")
    else:
        print("Your input was incorrect")


elif convert_from.lower() in  ["yards", "yard", "yds", "yd"]:
    number_of_yards = int(input("Enter Starting Measurement in yards: "))
    if convert_to.lower() in ["inches", "in", "Inches", "inch"]:
        print("Result: " + str(number_of_yards) + " Yards = " +  str(round(number_of_yards * 36)) + " Inches")    
    elif convert_to.lower() in  ["feet", "foot", "ft"]:
        print("Result: " + str(number_of_yards) + " Yards = " +  str(round(number_of_yards * 3)) + " Feet")
    else:
        print("Your input was incorrect")
else:
    print("Please enter either inches, feet or yards")
