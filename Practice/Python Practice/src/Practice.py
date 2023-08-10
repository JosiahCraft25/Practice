import random
"""
x = int(input("enter seed now: "))
"""
def RanNumGen ():
    
    #setting function vars
    totalRuns = 0
    unique = 0
    runningNums= []
    badRolls = 0
    

    #Generating 100 numbers
    while (totalRuns <= 100):
        #flag for later on & local var
        unique = 0
        ranTotal = 1
        
        #did not want just 1-10 because it was too many duplicates, therefore I made it multiply itself to get more varied numbers
        ranSeed = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=4)
        
        #Mulitplying the seed to get bigger seed
        for i in ranSeed:
            ranTotal *= i
        #inserting seed into number generator 
        random.seed(ranTotal)
        #generating number
        r = random.randrange(0, 21)
        
       #This checks for duplicates do not want duplicates >:(
        while unique == 0:
            if (r in runningNums):
                ranTotal = 1
                ranSeed = random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=4)
                for i in ranSeed:
                    ranTotal *= i
                random.seed(ranTotal)
                r = random.randrange(0, 21)
                print('bad number!')
                badRolls += 1
                totalRuns += 1
                if (badRolls == 100):
                    unique = 1
                    
            else:
                runningNums.append(r)
                totalRuns += 1
                unique = 1
                print(r)
    
    #Percentage of bad rolls
    percentage = round((badRolls/(len(runningNums) + badRolls) * 100), 7)
    print(f"{percentage}% bad rolls")
    #sorts and prints the numbers
    runningNums.sort()
    print(runningNums)
    
    
