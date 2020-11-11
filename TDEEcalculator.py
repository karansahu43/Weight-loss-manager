# Function TDEE calculator
# Description:
#	calculates and returns TDEE and BMR
# Calls:
#	none
# Parameters:
#	height
#       weight
#       gender
#       age
#       activityLevel
# Returns:
#	TDEE
#       BMR

def TDEEcalculator(height, weight, gender, age, activityLevel):

    # Declare local variables
    TDEE = 0
    BMR = 0

    #Check gender
    if (gender == 1):
        BMR = (66 + (13.7 * (weight / 2.2)) + (5 * height) - (6.8 * age))
    elif (gender == 2):
        BMR = (655 + (9.6 * (weight / 2.2)) + (1.8 * height) - (4.7 * age))
    else:
        print("somthing went wrong")
    #End if

    #check activity level
    if (activityLevel == 1):
        TDEE = (BMR * 1.2)
    elif (activityLevel == 2):
        TDEE = (BMR * 1.375)
    elif (activityLevel == 3):
        TDEE = (BMR * 1.55)
    elif (activityLevel == 4):
        TDEE = (BMR * 1.725)
    elif (activityLevel == 5):
        TDEE = (BMR * 1.9)
    else:
        print("somthing went wrong")
    #End if

    #Round Numbers
    BMR = round(BMR)
    TDEE = round(TDEE)

    # Return values
    return (BMR, TDEE)

# End Function---------------------------------------------------------------------------------------------------------------------