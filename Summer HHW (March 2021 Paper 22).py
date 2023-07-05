#imported for use in the random table.
import random as r 

#Check for if the input is an integer
def IntCheck(inpMessage,error):
    inp = input(inpMessage)
    while True:
        if inp.isdigit():
            return int(inp)
        else:
            print(error)
            inp = input(inpMessage)
            
#Check for yes or no:
def BoolCheck(inpMessage, error):
    inp = input(inpMessage)
    while True:
        if inp.lower() == 'y' or inp.lower() == 'yes':
            inp = True
            return inp
        elif inp.lower() == 'n' or inp.lower() == 'no':
            inp = False
            return inp
        else:
            print(error)
            inp = input(inpMessage)

#Student name
StudentName = input("Please enter your name: ")
while True:
    QuestionNumber = IntCheck(input("How many questions do you want in your quiz? : "), "Please enter a whole number.")
    if QuestionNumber == 0:
        print("You cannot take a quiz with 0 questions!")
    else:
        break
Mixed = BoolCheck("Do you want a mixed question set? (Y/N): ", "Please enter yes or no")
if Mixed == False:
    # Range Check
    while True:
        TableChoice = IntCheck("Enter your choice of table: ", "Please enter a valid whole number")
        if TableChoice in range(2,13):
            break
        else:
            print("Please enter values that are among 2 and 12")
else: TableChoice = None #TableChoice is set to None to prevent a value not defined error.

#Main score calculation
Score = 0
for i in range(1,QuestionNumber):

    # Defining starting integers
    Strikes = 3
    RandomNumber = r.randint(1, 12)
    RandomTable = r.randint(2,12)
    print(f"Question {i}\n")

    #While loop for checking if strikes are over
    while Strikes != 0:

        #Checking if the user wants mixed or not. If they do, then TableChoice is not used.
        if Mixed == False:
            Answer = IntCheck(f"{TableChoice} x {RandomNumber} = ", "Please enter a whole number.")
            ActAnswer = TableChoice * RandomNumber
        if Mixed == True:
            Answer = IntCheck(f"{RandomTable} x {RandomNumber} = ", "Please enter a whole number.")
            ActAnswer = RandomTable * RandomNumber

        #Answer checking
        if Answer == ActAnswer:
            Score += 1
            break
        elif Answer > ActAnswer:
            print(f"{StudentName} your answer is too large.")
            Strikes -= 1
        else: 
            print(f"{StudentName} your answer is too small")
            Strikes -= 1

     #Final message if they run out of chances       
    if Strikes == 0:
        print(f"\nThe answer is {ActAnswer}")

#End score
print(f"\n{StudentName} your score is {Score}/5")

#Final Message
if Score == 0: print("It's okay, you will get better with practice!")
elif Score == 1: print("Keep trying, you will get better!")
elif Score == 2: print("You're doing good, more practice will get you better marks.")
elif Score == 3: print("Take some more practice questions and you will be doing good in no time!")
elif Score == 4: print("Almost there, keep practicing!")
else: print("Full marks! Well done!")
