# Function timeTaken Calculation
# Description:
#	Calculates the approximate amount of time to reach your goal
# Calls:
#	none
# Parameters:
#	goalWeight
#       goalSpeed
#       weight
# Returns:
#	timeTaken

def timeTakencalculator (goalWeight , goalSpeed, weight):

    # Declare local variables
    timeTaken = 0
    weightDifference = 0
    
    #find Weight difference
    if (weight > goalWeight):
        weightDifference = (weight - goalWeight)
    elif (weight < goalWeight):
        weightDifference = (goalWeight - weight)
    elif (weight == goalWeight):
        weightDifference = 0
    else:
        print("somthing went wrong")
    #End if

    #calculate timeTaken
    if (goalSpeed == 1) or (goalSpeed == 3):
        timeTaken = ((weightDifference * 3500)/ 250)
    elif (goalSpeed == 2) or (goalSpeed == 4):
        timeTaken = ((weightDifference * 3500)/ 500)
    elif (weightDifference == 0):
        timeTaken = 0
    else:
        print("somthing went wrong")
    #End if 
    
    # Return values
    return timeTaken

# End Function-----------------------------------------------------------------------------------------------------------------------