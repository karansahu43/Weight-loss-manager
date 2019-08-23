# Program: The Weight Manager
# Description: 
# 	Input infomation and outputs information needed to reach weight goals
#       with some extra information
# Author: Karan Sahu
# Date: 11/25/2017
# Revised: 
# 	<revision date> 

# list libraries used
import os

# Declare global constants

def main():
    #take care of workout routine

    # Declare variables-------------------------------------------------------------------------------------------------
    name = ''
    nameCondition = False
    height = 0
    weight = 0
    age = 0
    gender = 0
    genderCondition = False
    activityLevel = 0
    activityLevelCondition = False
    goalWeight = 0
    goalSpeed = 0
    goalSpeedCondition = False
    macroNutrients = 0
    macroNutrientsCondition = False
    carbohydrate = 0
    protein = 0
    fat = 0
    outfile = ''
    GotIt = ''                                         

    
    #get costomer information
    print("please enter all asked information to create a personal profile")

    #name--------------------------------------------------------------------------------------------------------------
    while (nameCondition == False):
        try: 
            name = input("Please enter your name: ")
            outfile = open(name + "'s Personal Profile", 'w')
            outfile.write("please finish entering all information and remember to enter anything at the end to create file")
            outfile.close()
        except:
            print("Please enter a name without special characters")
            print()
            nameCondition = False
        else:
            print('Hello', name)
            nameCondition = True
            
    print()
    

    #height---------------------------------------------------------------------------------------------------------------
    while not (height > 0):
        #make sure program doesent crash with wrong inputs
        try:
            height = int(input("Please enter your height in cm: "))
        except:
            print ("please enter a proper height")
            print()
        else:
            if not (height > 0):
                print ("please enter a proper height")
                print()
            #End If
        #End Try
    #End while
    print()
        
    #weight----------------------------------------------------------------------------------------------------------------
    while not (weight > 0):
        try:
            weight = int(input("Please enter your weight in pounds: "))
        except:
            print ("please enter a proper weight")
            print()
        else:
            if not (weight > 0):
                print ("please enter a proper weight")
                print()
            #End if
        #End Try
    #End while
    print()

    #age-----------------------------------------------------------------------------------------------------------------------
    while not (age > 0):
        try:
            age = int(input("Please enter your age in years: "))
        except:
            print ("please enter a proper age")
            print()
        else:
            if not (age > 0):
                print ("please enter a proper age")
                print()
            #End if
        #End Try
    #End while
    print()
    print()

    #gender-----------------------------------------------------------------------------------------------------------------------
    #Diplay input options for gender
    print("If male enter 1")
    print("If female enter 2")
    print()

    while (genderCondition == False):
        try:  
            gender = int(input("Please enter your gender: "))
        except:
            print("please enter either 1 or 2 to specify gender")
            print()
            genderCondition = False
        else:
            if (gender == 1):
                genderCondition = True
            elif (gender == 2):
                genderCondition = True
            else:
                genderCondition = False
                print("please enter either 1 or 2 to specify gender")
                print()
            #End if
        #End Try
    #End while
    print()
    print()
                 
    #activity level--------------------------------------------------------------------------------------------------------------------
    #Display input options for activity level
    print("1: Sedentary (Little or no exercise desk job)")
    print("2: Lightly active (light exercise/sports 1-3 days per week)")
    print("3: Moderatly active (moderate exercise, sports 3-5 days per week)")
    print("4: Very active (Heavy exercise, sports 6-7 days per week)")
    print("5: Extremally active (Very heavy exercise, physical job, training 2x per day)")
    print()

    while (activityLevelCondition == False):
        try:
            activityLevel = int(input("on a scale of 1-5 how active are you: "))
        except:
            print("please enter a number from 1-5")
            print()
            activityLevelCondition = False
        else:
            if (activityLevel == 1) or (activityLevel == 2) or (activityLevel == 3) or (activityLevel == 4) or (activityLevel == 5):
                activityLevelCondition = True
            else:
                activityLevelCondition = False
                print("please enter a number from 1-5")
                print()
            #End if
        #End Try
    #End while
    print()

    #goal weight---------------------------------------------------------------------------------------------------------------
    while not (goalWeight > 0):
        try:
            goalWeight = int(input("please enter the weight you want to acheive in pounds: "))
        except:
            print("please enter a proper weight")
            print()
        else:
            if not (goalWeight > 0):
                print("please enter a proper weight")
                print()
            #End if
        #End Try
    #End while
    print()
    print()

    #goal speed----------------------------------------------------------------------------------------------------------
    if (goalWeight > weight):

        print("Option 3: I would like to gain half a pound per week")
        print("Option 4: I would like to gain a pound per week")
        print()

        while (goalSpeedCondition == False):
            try:
                goalSpeed = int(input("if Option 3, enter 3, if Option 4, enter 4: "))
            except:
                goalSpeedCondition = False
                print("please enter either Option 3 or 4 for your progress speed.")
                print()
            else:
                if (goalSpeed == 3) or (goalSpeed == 4):
                    goalSpeedCondition = True
                #End if
            #End try
        #End while

    elif (goalWeight < weight):

        print("Option 1: I would like to loose half a pound per week")
        print("Option 2: I would like to loose a pound per week")
        print()
        
        while (goalSpeedCondition == False):
            try:
                goalSpeed = int(input("if Option 1, enter 1, if Option 2, enter 2: "))
            except:
                goalSpeedCondition = False
                print("please enter either Option 1 or 2 for your progress speed.")
                print()
            else:
                if (goalSpeed == 1) or (goalSpeed == 2):
                    goalSpeedCondition = True
                #End if
            #End Try
        #End while     

    else:
        print("I am trying to maintain my weight")
        goalSpeed = 5
    #End if
    print()
    print()

    #macronutrients------------------------------------------------------------------------------------------------------------------
    print("Option 1: Not concerned with macronutrients right now")
    print("Option 2: I would like to do the recomended macronutrient diet plan")
    print("Option 3: I would like to do a High carb low fat diet")
    print("Option 4: I would like to do a low carb ketogenic diet")
    print("Option 5: I would like to create my own macronutrient profile")
    print()

    while (macroNutrientsCondition == False):
        try:
            macroNutrients = int(input("please enter the option you like, Ex if Option 3 enter 3: "))
        except:
            macroNutrientsCondition = False
            print("please enter a number from 1-5")
            print()
        else:
            if (macroNutrients == 1) or (macroNutrients == 2) or (macroNutrients == 3) or (macroNutrients == 4) or (macroNutrients == 5):
                macroNutrientsCondition = True
            #End if
        #End try
    #End while
    print()

    if (macroNutrients == 1):
        pass                                                                    ## <<<<---- NEED TO CHANGE EVENTUALLY

    elif (macroNutrients == 2):
        carbohydrate = 60
        fat = 25
        protein = 15

    elif (macroNutrients == 3):
        carbohydrate = 80
        fat = 10
        protein = 10

    elif (macroNutrients == 4):
        carbohydrate = 10
        fat = 60
        protein = 30

    elif(macroNutrients == 5):
        while not(carbohydrate + protein + fat == 100):

            try:
                carbohydrate = int(input("please enter percent of calories you want from carbohydrates: "))
                fat = int(input("please enter percent of calories you want from fat: "))
                protein = int(input("please enter percent of calories you want from protein: "))
            except:
                carbohydrate = 100
                fat = 100
                protein = 100
                print("please enter proper percentage values(make sure it add up to 100)")
                print()
            else:
                if not(carbohydrate + protein + fat == 100):
                    print("please enter proper percentage values(make sure it add up to 100)")
                    print()
                #End if
            #End Try
        #End while
    #End if

    

    ###Assigning values from functions__________________________________________________
    (BMR, TDEE) = TDEEcalculator(height, weight, gender, age, activityLevel)
##    print("BMR: ", BMR)
##    print("TDEE: ", TDEE)

    (BMI, NewBMI) = BMIcalculator(height , weight, goalWeight)
##    print("BMI: ", BMI)
##    print("New BMI: ", NewBMI)

    calPerDay = calPerDaycalculculator (TDEE, goalSpeed)
##    print("Calories per day: ", calPerDay)

    timeTaken = timeTakencalculator (goalWeight , goalSpeed, weight)
##    print("Time it will take in days: ", timeTaken)

    (carbohydrateGrams, fatGrams, proteinGrams) = macroNutrientscalculator (macroNutrients, carbohydrate, fat, protein, calPerDay)
##    print("carbohydrate in grams: ", carbohydrateGrams)
##    print("fat in grams: ", fatGrams)
##    print("protein in grams: ", proteinGrams)

    #Instructions

    print("Please Open your personal file (", name + "'s" ," Personal Profile) to see your results.")
    GotIt = input("Enter anything to create file: ")


    #Make personal Profile file--------------------------------------------------------------------------------------------------------
    outfile = open(name + "'s Personal Profile", 'w')

    outfile.write("The Weight Manager" + '\n')
    
    outfile.write(name + "'s Personal Profile" + '\n')
    outfile.write('\n')
    
    outfile.write("Age:                 " + str(age) + " years")
    outfile.write('\n')

    outfile.write("Height:              " + str(height) + " cm")
    outfile.write('\n')

    if (gender == 1):

        outfile.write("Gender:              Male")
    elif (gender == 2):
        outfile.write("Gender:              Female")
    outfile.write('\n')
    
    #End if
    if (activityLevel == 1):
        outfile.write("Your Activity level: Sedentary (Little or no exercise desk job)")
    elif (activityLevel == 2):
        outfile.write("Your Activity level: Lightly active (light exercise/sports 1-3 days per week)")
    elif (activityLevel == 3):
        outfile.write("Your Activity level: Moderatly active (moderate exercise, sports 3-5 days per week)")
    elif (activityLevel == 4):
        outfile.write("Your Activity level: Very active (Heavy exercise, sports 6-7 days per week)")
    elif (activityLevel == 5):
        outfile.write("Your Activity level: Extremally active (Very heavy exercise, physical job, training 2x per day)")
    #End if
    outfile.write('\n')

    outfile.write("Current Weight:      " + str(weight) + " lbs")
    outfile.write('\n')
    outfile.write("Goal Weight:         " + str(goalWeight) + " lbs" + '\n')
    
    if (goalSpeed == 1):
        outfile.write("Weight progression:  I would like to loose half a pound per week")
    elif (goalSpeed == 2):
        outfile.write("Weight progression:  I would like to loose a pound per week")
    elif (goalSpeed == 3):
        outfile.write("Weight progression:  I would like to gain half a pound per week")
    elif (goalSpeed == 4):
        outfile.write("Weight progression:  I would like to gain a pound per week")
    elif (goalSpeed == 5):
        outfile.write("Weight progression:  I am trying to maintain my weight")
    #End if
    outfile.write('\n')

    outfile.write('\n')
                      
    outfile.write("Current BMI: " + str(BMI) + "                          |Underweight: BMI is less than 18.5.")
    outfile.write('\n')
    outfile.write("Goal BMI:    " + str(NewBMI) + "                          |Normal weight: BMI is 18.5 to 24.9.")
    outfile.write('\n')
    outfile.write('                                           |Overweight: BMI is 25 to 29.9.')
    outfile.write('\n')
    outfile.write('                                           |Obese: BMI is 30 or more.')
    outfile.write('\n')
    
                      
    outfile.write('\n')

    outfile.write("Basal Metabolic Rate(BMR) is the number of calories you burn doing nothing")
    outfile.write('\n')
    outfile.write("BMR:  " + str(BMR))
    outfile.write('\n')

    outfile.write('\n')

    outfile.write("Total Daily Energy Expenditure(TDEE) is the total numbers of calories you burn including activity")
    outfile.write('\n')
    outfile.write("TDEE: " + str(TDEE))
    outfile.write('\n')
    
    outfile.write('\n')
    outfile.write("Recomended number of calories per day to reach goal: " + str(calPerDay))
    outfile.write('\n')
    
    outfile.write("Approximate number of days till goal is reached:     " + str(timeTaken))
    outfile.write('\n')
    outfile.write('\n')

    if (macroNutrients == 1):
        pass
    elif (macroNutrients == 2):
        outfile.write("MacroNutrient break down: Recocomended plan (60% carb, 25% fat, 15% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    elif (macroNutrients == 3):
        outfile.write("MacroNutrient break down: High carb, low fat (80% carb, 10% fat, 10% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    elif (macroNutrients == 4):
        outfile.write("MacroNutrient break down: Low carb, Ketogenic diet(10% carb, 60% fat, 30% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    elif (macroNutrients == 5):
        outfile.write("MacroNutrient break down: Your Macronutrient plan(" + str(carbohydrate) + "% carb, " + str(fat) + "% fat, " + str(protein) +"% protein)")
        outfile.write('\n')
        outfile.write('\n')
        outfile.write("Carbohydrate intake in grams per day: " + str(carbohydrateGrams))
        outfile.write('\n')
        outfile.write("Fat intake in grams per day:          " + str(fatGrams))
        outfile.write('\n')
        outfile.write("Protein intake in grams per day:      " + str(proteinGrams))
    #End if

    outfile.close()

    os.startfile(name + "'s Personal Profile")
    

    #createResult()

# End main Function------------------------------------------------------------------------------------------------------------------------

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



    

main()
