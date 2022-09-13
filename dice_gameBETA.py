import random
import time
def dice():
    player = random.randint(1,6)
    print("You rolled "+str(player))
    ai = random.randint(1,6)
    print("The computer rolls...")
    time.sleep(2)
    print("The computer rolled "+str(ai))
if player > ai :
    print("You win") #hastages are for notes
elif player == ai:
    print("Tie game.")
else: 
    print("You SUCK! HA!")
print("Quit? Y/N")
continue = input()
if continue == "Y" or continue == "y":
    exit()
elif continue == "N" or continue == "n"
    pass
else:
    print("I did not understand that. Playing again.")
#main loop
while True: 
    print("Press return to roll your die")
    roll = input()
    dice()
    