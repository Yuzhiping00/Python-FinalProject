
#filename:finalProject.py
#I,Zhiping Yu,certify that all code submitted is my own work; that I have not copied it from any other source.
#I also certify that I have not allowed my work to be copied by others.

import random

def rollDie( faces ):
    # module to roll a single die with a variable number of faces
    # ASSUME faces is a valid positive integer, greater than 1
    
    if faces.isdecimal():
        if (int(faces)>= 2) and (int(faces)<= 20):
            return True         
    else:
        return False
    
    
def validateInt( min, max, prompt ):
    # ASSUME min and max are valid positive integers, and that min < max
    
    if not prompt.isdecimal():
        print("I'm sorry, that isn't a valid positive integer, please try again.")
        return False
    if int(prompt) < min or int(prompt)> max:
        print("I'm sorry, that isn't in the range 3 to 6 , please try again.")
        return False
    else:
        return True


def validateStr( prompt, listOfChoices ):
    # assume prompt is a String and listOfChoices is a list of Strings.
    return ""

def calculateSum(aList):
    aSum = 0
    for i in range(0,len(aList)):
        aSum += aList[i]
    return aSum

def average( inList ):
    # ASSUME inList is a list of numbers and the length of inList is > 0
   ''' sum = 0
    length = len(inList)
    for i in range(0,length):
        sum = sum + inList[i]
    average = round(sum / length)
    return average'''
   sum1 = calculateSum(inList)
   average = round(sum1/len(inList))
   return average

def calculatePercentage( sides, dice, diceRolls ):
    # ASSUME sides*dice != 0, sides, dice are numbers
    # ASSUME diceRolls is a list of numbers
    rolledSum = 0
    maxScore = sides * dice
    for i in range(0,len(diceRolls)):
        rolledSum = rolledSum + diceRolls[i]
        
    percentage = rolledSum / maxScore 
    return percentage

def isPrime( number ):
    # ASSUME number is an integer
    for i in range(2,number):
        if number % i == 0:
            return False
    else:
        return True
        

def pattern1( sides, dice ):
    # ASSUME sides > 0 and dice is a list of integers
    if sides >=4:
        
        if dice.count(dice[0])== len(dice):
            print("Pattern 1 matched in your roll ," ,dice,"...all dice are same")
            return True
        
        else:
            print("Pattern 1 does not match in your roll since ," ,dice,"...some dice are different")
            return False
    else:
        print("Pattern 1 does not apply since # of sides is less than 4.")
        return False


def pattern2( sides, count, dice):
    # ASSUME sides, count are integers
    # ASSUME dice is a list of integers
    sum = 0
    maxScore = sides * count
    if maxScore >= 20:
        for i in range(0,len(dice)):
            sum = sum + dice[i]
        if isPrime(sum):
            print("Pattern 2 matched,",sum,"is a prime number!")
            return True
        else:
            print("Patter 2 does not match since",sum,"is not a prime number!")
            return False
    else:
        print("Pattern 2 does not apply since Maximum score is", maxScore,"which is less than 20!")
        return False


def pattern3( dice ):
    # ASSUME dice is a list of integers
    length = len(dice)
    number = 0
    if length >= 5:
        average2 = round(average(myList))
        for i in range(0,length):
            if dice[i] >= average2:
                number = number + 1
        if number >= length / 2:
            print("Pattern 3 mathched! More than half of," ,dice,"are greater than or equal to the average of ",average2)
            return True
        else:
            print("Pattern 3 does not match since less than half of,",dice,"are greater than or equal to the average of ",average2)
            return False
    else:
        print("Pattern 3 does not apply since there are less than 5 dice.")
        return False
        

def pattern4( sides, dice ):
    # ASSUME dice is a list of integers
    length = len(dice)
   
    if length > 4 and sides > length:
        
        flag = len(set(dice)) == length
        if flag == True:
            print("Pattern 4 matched,all of the dice are different values.")
            return True
        else:
            print("Pattern 4 does not match,some dice have the same values.")
            return False
    else:
        print("Pattern 4 does not apply, either sides <= 4 or # of sides <= dice.")
        return False
        
def bonusFactor( sides, count, dice ):
    # ASSUME dice is a list of numbers
    # ASSUME sides, count are integers
    bonFac = 0
    if pattern1( sides, dice ):
        bonFac += 10
    if pattern2( sides, count, dice):
        bonFac += 15
    if pattern3(dice):
        bonFac += 5
    if pattern4(sides, dice):
        bonFac += 8
    #else:
       # print("Since none of the other patterns were matched,pattern 5 is matched")
        #bonFac += 1
        
    return bonFac

def score( maxSides, totalDice, diceRolled,bonusF ):
    # ASSUME maxSides and totalDice are integers > 0
    # ASSUME diceRolled is a list of integers
    percentage = calculatePercentage(maxSides, totalDice, diceRolled)
    number = percentage * bonusF
    grade = int(number + 822513 % 500) 
    return grade

def showInfo(myList,numDice,sides):
    sum1=calculateSum(myList)    
    average1 = average(myList)
    print("These die sum to",sum1,"and have an average rounded value of",round(average1))

    percentage1 = calculatePercentage(sides,numDice,myList)
    print("percentage1 is", percentage1)
    validPrime = isPrime(sum1)    
    factor = bonusFactor(sides,numDice, myList)
    if factor <= 0:
        print("Since none of the other patterns were matched,pattern 5 is matched")
        factor = 1
    else:
        print("Since you matched at least one pattern, pattern 5 is not matched!")
    print("Your bonus factor is", factor)
    points = score(sides,numDice,myList, factor)
    print("These dice are worth",points,"points.")
           
    print("")
    print("")
    print("")
    return points

    
def createList(dice):
    myList = []
    for i in range(0,int(numDice)):
        myList.append(random.randint(2,int(sides)))

    print("You have rolled:",myList)
    print("")               
    return myList
    
#===================================main method========================================================================#


print("")
print("COMP 10001- W2020 Final Project by Zhiping Yu,Student number 000822513")
print("Welcome to my dice game, good luck!")
print("")

flag1= True
sides = ""
while flag1:
    sides = input("Enter # of faces [2,20]: ")
    while not rollDie(sides):
        print("I'm sorry, that isn't a valid positive integer, please try again.")
        sides = input("Enter # of faces [2,20]: ")
    flag1 = False

print("")

numDice =""
flag2 = True
while flag2 :
    numDice = input("Enter # of dice[3,6]: ")
    while not validateInt(3,6,numDice):
        numDice = input("Enter # of dice[3,6]: ")
    flag2 = False

print("")

myList= createList(int(numDice))

grade= showInfo(myList,int(numDice),int(sides))
arrScore=[]
#arrScore.append(grade)

reroll = ""
while True:
    reroll = input("Do you want to reroll any dice?['yes','no'] ")
    if reroll == "Yes" or reroll=="yEs" or reroll=="yeS" or reroll=="YEs" or \
       reroll=="YeS" or reroll=="yES" or reroll=="yes" or reroll=="YES" or \
        reroll=="no" or reroll=="No" or reroll=="nO" or reroll=="NO":
        break
    else:   
        print("I'm sorry,the choices are ['yes,no']. Please pick one of them.")
        


if reroll=="no" or reroll=="No" or reroll=="nO" or reroll=="NO":
    arrScore.append(grade)
    
            
else:
    
    position = 0
    arr=[]
    while position< len(myList):
        print("Reroll die "+str(position+1)+"(was "+ str(myList[position])+") ['y','n'] ",end="")
        answer = input()
        print(answer)
        while True:
            if answer== "y" or answer=="Y" or answer== "n" or answer=="N":
                arr.append(answer)
                break
            else:
                print("Reroll die "+str(position+1)+"(was "+ str(myList[position])+") ['y','n'] ",end="")
                answer = input()
        position += 1
    print(arr)
    decision=""
    while True:
        decision = input("Are you sure? ['yes','no'] ")
        if decision == "Yes" or decision=="yEs" or reroll=="yeS" or decision=="YEs" or \
           decision=="YeS" or decision=="yES" or decision=="yes" or decision=="YES" or \
           decision=="no" or decision=="No" or decision=="nO" or decision=="NO":
            break
        else:
            print("I'm sorry,the choices are ['yes','no']. Please pick one of them.")
            
    if decision == "Yes" or decision=="yEs" or reroll=="yeS" or decision=="YEs" or \
       decision=="YeS" or decision=="yES" or decision=="yes" or decision=="YES":
        for i in range(0,len(arr)):
            if arr[i] != "n" and arr[i] !="N":
                myList[i]= random.randint(2,int(sides))
        
        print("")
        
        print("You have rolled: ", myList)
        grade= showInfo(myList,int(numDice),int(sides))
        arrScore.append(grade)
        print("")
     
    else:
        arrScore.append(grade)
       
        
print("This was your first turn, let's go again!")
myList=createList(numDice)
grade= showInfo(myList,int(numDice),int(sides))
arrScore.append(grade)
print(arrScore)
sumScore = 0
for i in range(0,len(arrScore)):
    sumScore += arrScore[i]
    
average2 = int(sumScore / len(arrScore))
    
repeat=""
while True:
    reply=input("Do you want to reroll any dice? ['yes','no'] ")
    if reply == "Yes" or reply=="yEs" or reply=="yeS" or reply=="YEs" or \
       reply=="YeS" or reply=="yES" or reply=="yes" or reply=="YES" or \
       reply=="no" or reply=="No" or reply=="nO" or reply=="NO":
        break
    else:   
        print("I'm sorry,the choices are ['yes,no']. Please pick one of them.")
    
if reply=="no" or reply=="nO" or reply=="No" or reply=="NO":
    if grade < average2:
        print("Your score of",grade,"on turn",len(arrScore),"was below average",average2,"compared to other turns today.")
    elif grade == average2:
        
        print("Your score of",grade,"on turn",len(arrScore),"was average",average2,"compared to other turns today.")
    else:
        print("Your score of",grade,"on turn",len(arrScore),"was above average",average2,"compared to other turns today.")
else:
    pass

respond =""

while True:
    respond =input("Would you like to play another turn ['y','n'] ")
    if respond == "Y" or respond=="n" or respond =="y" or respond=="N":
        if respond=="y" or respond=="Y":
            myList=createList(numDice)
            grade= showInfo(myList,int(numDice),int(sides))
            arrScore.append(grade)
            print(arrScore)
            sumScore = 0
            for i in range(0,len(arrScore)):
                sumScore += arrScore[i]
                    
            average2 = int(sumScore / len(arrScore))
        
        else:
            print("You played",len(arrScore),"turns today with an average score of",average2,"points.")
            break
                    

    else:
        print("I'm sorry,the choices are ['yes','no']. Please pick one of them.")
        

   
    
