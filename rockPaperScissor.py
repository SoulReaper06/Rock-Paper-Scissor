import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listChoice = [rock,paper,scissors]

userInput = input("What's your play ? Rock , Paper or Scissors : ").lower()
print(f"You Choose : {userInput}")
print(globals()[userInput])
cpuChoice = random.choice(listChoice)
cpuChoiceStr = ""

if( cpuChoice == rock):
    cpuChoiceStr = "rock"
elif(cpuChoice == paper):
    cpuChoiceStr = "paper"
else:
    cpuChoiceStr = "scissors"         

print(f"Computer's Choice :{cpuChoiceStr}{cpuChoice}")
if(userInput == "paper" and cpuChoiceStr == "rock"):
    print("You Win !!!")
elif(userInput == "paper" and cpuChoiceStr == "scissors"):
    print("Computer Wins !!!")
elif(userInput == "rock" and cpuChoiceStr == "scissors"):
    print("You Win !!!")
elif(userInput == "rock" and cpuChoiceStr == "paper"):
    print("Computer Wins !!!")
elif(userInput == "scissors" and cpuChoiceStr == "paper"):
    print("You Win !!!")
elif(userInput == "scissors" and cpuChoiceStr == "rock"):
    print("Computer Wins !!!")
else:
    print("DRAW ! TRY AGAIN")                              

