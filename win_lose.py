import sys
from datetime import datetime as dt

def win(message, starttime):
    print(message)
    print(f"Total gametime elapsed: {dt.now() - starttime}")
    sys.exit()
    
def lose(message, starttime): #add playagsain/inventory reset
    bContinue = True
    print(message)
    print(starttime)
    play_again = input("Would you like to play again?\n(Enter Y to continue or press enter to exit:)").upper()
    while bContinue :
        if len(play_again) > 0 : 
            if play_again == 'Y' :
                print("Good choice")
            else :
                play_again = input("Either type Y to play again or hit enter to exit.")
        else :
            sys.exit()
