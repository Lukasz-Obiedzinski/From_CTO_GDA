__author__='dev'
'''
name=input("Please enter your name: ")
age=int(input("How old are you, {0} ".format(name)))
if age>=18:
    print("You are old enought to vote")
    print("Put an X in the box")
else:
    print("Please come back in {0} years".format(18-age))
'''
print("Please guess a number between 1 and 10: ")
guess=int(input())

if guess != 5:
    if guess<5:
        print("Please guess higher")
    else:
        print("please guess lower")
    guess=int(input())
    if guess == 5:
        print("Well done")
    else:
        print("Sorry, you have not guessed corectly.")
else:
    print("You got it first time!")
        
