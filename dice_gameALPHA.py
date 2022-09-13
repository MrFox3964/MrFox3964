import random
import time
def dice():
    player= random.randint(1,6)
    print("You rolled"+str(player))
    ai= random.randint(1,6)
    print("The computer rolled"+str(ai))
if player > ai :
    print("You win") #hastages are for notes
else: 
    print("You SUCK! HA!")