'''
July 13, 2023

Aiming to make a short project to provide some consulting math questions for Sherry to practice with
1. Breakeven point
2. what is n% of m
3. m is n% of what
4. NPV
'''

# imports
import random
import time

# define globals
FRACTIONBASES = [3,6,7,8,9]

# define functions
def breakEvenProblem(*inputs):
    # randomly generate fixed costs  (an integer)
    fixedCosts = random.randint(100, 1000)
    
    # determine factors
    factorsOfFixedCost = []
    for factor in range(1, fixedCosts+1):
        if fixedCosts % factor == 0:
            factorsOfFixedCost.append(factor)

    # randomly select a break even point from the factors of fixed costs
    breakEvenPoint = factorsOfFixedCost[random.randint(0,len(factorsOfFixedCost)-1)]

    # divide fixed costs by break even to get (USP - UC), and randomly determine unit cost and unit selling price
    unitCost = random.randrange(100,5000)/100
    unitSellingPrice = round((fixedCosts / breakEvenPoint) + unitCost,2)

    # break out unit costs
    inputCosts = []
    breakCosts = random.randint(0,7)
    while breakCosts != 0:
        removedCost = (random.randrange(100,int(unitCost*100))/100)
        if (round(unitCost - removedCost,2) < 1):
            break
        inputCosts.append(removedCost)
        unitCost = round(unitCost - removedCost,2)
        breakCosts = random.randint(0,int(breakCosts/2))
    inputCosts.append(unitCost)

    print("Widgets sell for $", unitSellingPrice)
    print("The input costs of widgets are: ", inputCosts)
    print("The fixed costs of producing widgets are $", fixedCosts)
    
    answer = int(input("What is the break even point? >> "))
    if answer == breakEvenPoint:
        return True, 0
    else:
        return False, breakEvenPoint

def percentOfM(*inputs):
    # decide if it's gonna be a funky fraction
    alternative = random.randint(0,5)
    if alternative == 0:
        base = FRACTIONBASES[random.randint(0,len(FRACTIONBASES)-1)]
        correctFraction = random.randint(1, 500)
        m = correctFraction*base
        percent = round(1/base,4)*100
    else:    
        m = random.randint(100, 1000)
        percent = random.randrange(0, 100, 5)
        correctFraction = round(m*(percent/100),2)

    answer = float(input(f"What is {percent}% of {m}? >> "))
    if answer == correctFraction:
        return True, 0
    else:
        return False, correctFraction
    
def percentOfWhat(*inputs):
    # decide if it's gonna be a funky fraction
    alternative = random.randint(0,5)
    if alternative == 0:
        base = FRACTIONBASES[random.randint(0,len(FRACTIONBASES)-1)]
        m = random.randint(1, 100)
        correctWhole = base * m
        percent = round(1/base,2)
    else:
        correctWhole = random.randrange(0, 500,10) 
        percent = random.randrange(0, 100, 5)
        m =  correctWhole*(percent/100)

    answer = int(input(f"{m} is {percent}% of what? >> "))
    if answer == correctWhole:
        return True, 0
    else:
        return False, correctWhole

def netPresentValue(*inputs):
    # randomly select profit
    profit = random.randint(100, 1000)
    DISCOUNTRATE = 5

    '''
    Select GrowthRate - Discountrate from the factors of profit, under 15.
        In the case of primes it will always select 1. This will happen about 12% of the time and shold be rectified.
    
    GrowthRate - DiscountRate is adjusted up by discount rate to find growthRate
    Growth rate is then divided by 100 to make it a decimal for use in calculating NPV
    '''

    grDr = determineGrDr(profit=profit)
    npv = profit / (grDr/100)
    growthRate = grDr + DISCOUNTRATE


    print(f"GrowthRate is {growthRate}%, profit is ${profit}, Discount Rate is ${DISCOUNTRATE}")

    answer = int(input("What is the NPV? >> "))
    if answer == npv:
         return True, 0
    else:
        return False, npv

# helper function for NPV problems
def determineGrDr(profit):
    lastFactor = 0
    for factor in range(1, profit+1):
        if profit % factor == 0:
            if factor > 17:
                break
            else:
                lastFactor = factor
    # lastFactor is now the greatest factor of profit under 15.
    # If it is less than 5, I want a 50/50 chance of it being negative now (or some function where it is more likely for 1 to be negative and less likely for 4 to be negative)
    if lastFactor < 5:
         # choose a random number from 0 to last factor. If that number is 0, flip it. This gives possibilities of seeing negatives, but very small possibilities
        flipSign = random.randint(0,lastFactor)
        if flipSign == 0:
            lastFactor = lastFactor * -1
    
    return lastFactor

def calcRoi(*inputs):
    pass

def exitFunc(*inputs):
    for problemType in problemDesc:
        print(f"For {problemDesc[problemType]} problems you scored {scoringDict[problemType]} out of {problemCountDict[problemType]}")
    leave = input("These results will not be saved after you exit. Type 'Exit' to leave or hit [Enter] to stay. >> ")
    if leave == "Exit":
        exit()
    return False, 0

# main
if __name__ == "__main__":
    # setup dicts
    problemDict = {1:breakEvenProblem,2:percentOfM, 3:percentOfWhat, 4:netPresentValue, 5:exitFunc}
    problemDesc = {1:"Break Even",2:"percent of whole", 3:"whole from percent", 4:"NPV", 5:"Exit"}
    scoringDict = {}
    problemCountDict = {}
    for problemType in problemDesc:
                scoringDict[problemType] = 0
                problemCountDict[problemType] = 0

    print("Welcome to consulting math")

    # run problems until you dont want to anymore
    while True:    
        # input validation
        while True:
            for problemType in problemDesc:
                print(f"{problemType}: {problemDesc[problemType]}")
            selectedProblem = int(input(">> "))

            if selectedProblem <= len(problemDict):
                break
            print("Please select a valid problem")


        if selectedProblem == problemType:
            loopProblem = 1
        else:
            loopProblem = int(input("How many problems of the selected type would you like to run? >> "))

        for counter in range(loopProblem):
            correct, answer = problemDict[selectedProblem]()
            if correct:
                scoringDict[selectedProblem] = scoringDict.get(selectedProblem) + 1
                print("Correct")
            else:
                print(f"Incorrect, the answer is {answer}")
            problemCountDict[selectedProblem] = problemCountDict.get(selectedProblem) + 1