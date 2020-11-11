# Function BMI calculator
# Description:
#	takes inputs and calculates then returns BMI Value
# Calls:
#	none
# Parameters:
#	height
#       weight
# Returns:
#	BMI

def BMIcalculator(height , weight, goalWeight):

    # Declare local variables
    BMI = 0
    NewBMI = 0

    #calculate BMI
    BMI = ((weight / 2.2)/(height / 100)**2)
    NewBMI = ((goalWeight / 2.2)/(height / 100)**2)

    #Round numbers
    BMI = round(BMI, 1)
    NewBMI = round(NewBMI, 1)

    # Return values
    return (BMI, NewBMI)

# End Function----------------------------------------------------------------------------------------------------------------