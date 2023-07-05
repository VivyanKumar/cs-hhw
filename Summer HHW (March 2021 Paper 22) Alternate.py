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

#Task 1
def Testing():
    StudentName = input("Please enter your name: ")
    while True:
        TableChoice = IntCheck("Enter your choice of table :", "Please enter a whole number.")
        if TableChoice in range(2,13):
            break
        else:
            print("Please enter a whole number among 2 and 12.")
    Score = 0
    for q in range(1,6):
        print(f"Question {q}\n")
        RandomNumber = r.randint(1,12)
        StudentAnswer = IntCheck(f"{TableChoice} x {RandomNumber} = ", "Please enter a whole number.")
        ActualAnswer = TableChoice * RandomNumber
        if StudentAnswer == ActualAnswer:
            Score += 1
        else:
            continue
    print(f"{StudentName} your score is {Score}/5\n")
    if Score == 5:
        print("Well done full marks")
    else:
        print("Have another practice")

#Task 2
def Learning():
    StudentName = input("Please enter your name : ")
    while True:
        TableChoice = IntCheck("Enter your choice of table :", "Please enter a whole number.")
        if TableChoice in range(2,13):
            break
        else:
            print("Please enter a whole number among 2 and 12.")
    for q in range(1, 6):
        Strikes = 3
        RandomNumber = r.randint(1,12)
        ActualAnswer = TableChoice * RandomNumber
        while Strikes != 0:
            print(f"Question {q}\n")
            StudentAnswer = IntCheck(f"{TableChoice} x {RandomNumber} = ", "Please enter a whole number.")
            if StudentAnswer < ActualAnswer:
                print(f"{StudentName} your answer is too small")
                Strikes -= 1
            elif StudentAnswer > ActualAnswer:
                print(f"{StudentName} your answer is too large")
                Strikes -= 1
            else:
                break
        if Strikes == 0:
            print(f"The correct answer is {ActualAnswer}")
        
#Task 3
def Varying():
    StudentName = input("Please enter your name: ")
    while True:
        QuestionNumbers = IntCheck("Please enter how many questions you would like : ", "Please enter a whole number.")
        if QuestionNumbers == 0:
            print("You cannot have 0 questions!")
        else:
            break
    Mixed = BoolCheck("Do you want mixed questions? (Y/N) : ", "Please enter yes or no.")
    if Mixed == False:
        while True:
            TableChoice = IntCheck("Enter your choice of table :", "Please enter a whole number.")
            if TableChoice in range(2,13):
                break
            else:
                print("Please enter a whole number among 2 and 12.")
    else: TableChoice = None #To prevent no value assigned error we assign None value to TableChoice
    Score = 0
    for q in range(1,QuestionNumbers):
        print(f"Question {q}\n")
        RandomNumber = r.randint(1,12)
        RandomTable = r.randint(1,12)
        if Mixed == True:
            StudentAnswer = IntCheck(f"{TableChoice} x {RandomNumber} = ", "Please enter a whole number.")
            ActualAnswer = TableChoice * RandomNumber
        else:
            StudentAnswer = IntCheck(f"{RandomTable} x {RandomNumber} = ", "Please enter a whole number.")
            ActualAnswer = RandomTable * RandomNumber
        if StudentAnswer == ActualAnswer:
            Score += 1
        else:
            continue
    print(f"{StudentName} your score is {Score}/5\n")
    if Score == 5:
        print("Well done full marks")
    else:
        print("Have another practice")
FunctionsList = [Testing(), Learning(), Varying()]
print("-----------------Select your function-------------------");print("(1) Test yourself");print("(2) Learn");print("(3) Vary");print("(4) Exit")
while True:
    Choice = IntCheck("Enter your choice : ", "Please enter a whole number.")
    if Choice in range(1,4):
        FunctionsList[Choice-1]
        break
    elif Choice == 4:
        quit()
    else:
        print("Please enter a number among 1 and 4.")
        continue