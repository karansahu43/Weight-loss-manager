# Function Calories per day calculation
# Description:
#	calculates how many calories needed per day for goal
# Calls:
#	none
# Parameters:
#	TDEE
#       goalSpeed
# Returns:
#	calPerDay

def calPerDaycalculculator (TDEE, goalSpeed):

    # Declare local variables
    calPerDay = 0

    #calculate cal per day

    if (goalSpeed == 1):
        calPerDay = (TDEE - 250)
    elif (goalSpeed == 2):
        calPerDay = (TDEE - 500)
    elif (goalSpeed == 3):
        calPerDay = (TDEE + 250)
    elif (goalSpeed == 4):
        calPerDay = (TDEE + 500)
    elif (goalSpeed == 5):
        calPerDay = TDEE
    else:
        print("somthing went wrong")
    #End If

    #Round Numbers
    calPerDay = round(calPerDay)

    # Return values
    return calPerDay

# End Function---------------------------------------------------------------------------------------------------------------------






