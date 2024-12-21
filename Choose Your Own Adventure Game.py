import random

print("Hello. Your name is Zan Dhao and you are a freshman at Consetoga High School.")
print("")
enter = input("Click enter to continue")
print("")
print("You walk into French class and your teacher says your class has a pop quiz today.")
print("")
cheatDecision = input("Do you cheat on the test? Type 1 for yes and 2 for no")
loopContinuous = 1
while loopContinuous == 1:
    if cheatDecision == 2:
        y = random.randint(0, 3)
        if y == 0:
            print("You failed the class. You LOSE.")
            loopContinuous = 0
        else:
            print("You pass and are fine")  # NOT WORTH INDENTING IF STATEMENTS INSIDE IF STATEMENTS
            enter = input("Click enter to continue")
            print("You walk into your next class which is english, but realize you forgot to do your homework.")
            print("")
            rushJob = input("Do you rush to do your homework? Type 1 for yes and 2 for no")
            if rushJob == 2:
                print("You failed.")
                loopContinuous = 0
            if rushJob == 1:
                x = random.randint(0,2)
                if x == 0:
                    print(x)
                    loopContinuous = 0
    if cheatDecision == 1:
        y = random.randint(0,4)
        if y == 0:
            print("You don't get caught cheating, you lucky duck.")
        else:
            print("LOL YOU GOT CAUGHT AND LOST")
            loopContinuous = 0