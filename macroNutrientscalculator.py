
# Function Macroprofile calculator
# Description:
#	calculate how many grams of each macronutrient you need based on your preference
# Calls:
#	none
# Parameters:
#	macroNutrients
#       carbohydrate
#       fat
#       protein
#       calPerDay
# Returns:
#	carbohydrateGrams
#       fatGrams
#       proteinGrams

def macroNutrientscalculator (macroNutrients, carbohydrate, fat, protein, calPerDay):

    # Declare local variables
    carbohydrateGrams = 0
    fatGrams = 0
    proteinGrams = 0

    #calculate macronutrint profile
    if (macroNutrients == 1):
        pass
    else:
        carbohydrateGrams = ((calPerDay * (carbohydrate / 100)) / 4)
        fatGrams = ((calPerDay * (fat / 100)) / 9)
        proteinGrams = ((calPerDay * (protein / 100)) / 4)
    #End if

    #Round Numbers
    carbohydrateGrams = round(carbohydrateGrams)
    fatGrams = round(fatGrams)
    proteinGrams = round(proteinGrams)

    # Return values
    return (carbohydrateGrams, fatGrams, proteinGrams)

# End Function----------------------------------------------------------------------------------------------------------------------