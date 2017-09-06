
#TREEHOUSE PROJECTS

#age calculator
# Step 1
# Ask the user for their name and the year they were born.
currentYear = 2017

def getName():
    name = input('Please enter your name: ')
    getYear(name)

def getYear(name):
    yearName = name
    birthYear = input('Please enter your birth year: ')
    try:
        birthYear = int(birthYear)
        calcs(yearName,birthYear)
    except ValueError:
        print('Hey, '+str(name)+', Please enter a number for your birthyear. (ie. 1983)')
        getYear(yearName)


# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
def calcs(name,year):
    yearCalc = year
    nameCalc = name
    current_age = currentYear - yearCalc

    turn25 = yearCalc + 25
    turn50 = yearCalc + 50
    turn75 = yearCalc + 75
    turn100 = yearCalc + 100

    #print('DEBUG: birthYear: ' + str(yearCalc) + ' name: ' + str(nameCalc) + ' currentYear: ' + str(currentYear))
    #print('DEBUG: 25@'+str(turn25)+' | 50@'+str(turn50)+' | 75@'+str(turn75)+' | 100@'+str(turn100))

# Step 3
# If they're already past angy of these ages, skip them.

    if turn25 > currentYear:
         print('You will turn 25 in the year '+str(turn25))
    if turn50 > currentYear:
        print('You will turn 50 in the year '+str(turn50))
    if turn75 > currentYear:
        print('You will turn 75 in the year '+str(turn75))
    if turn100 > currentYear:
        print('You will turn 100 in the year '+str(turn100))
    if turn100 < currentYear:
        print('Your over 100... and using a computer... thats commendable.')



getName()
