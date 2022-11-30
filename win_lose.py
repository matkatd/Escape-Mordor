import sys
from datetime import datetime as dt

def end(message, starttime):
    print(message)
    print(f"Total gametime elapsed: {dt.now() - starttime}")
    sys.exit()
    
def win(message, starttime):
    print(message)
    current_score = dt.now() - starttime
    print(f"Total gametime elapsed: {current_score}")
    with open("myscores.txt", "w+") as use_file:
        old_score = use_file.readline()
        if old_score == "":
            print("Congrats on your first recorded playthrough!")
            use_file.write(str(current_score))
        else:
            if old_score == current_score:
                print(f"You matched your best score of {old_score}")
            elif old_score > current_score:
                print(f"Oooo you missed beating your best score of {old_score}")
            else:
                print(f"Congrats of beating your best score of {old_score}")
                use_file.write(str(current_score))
        return

start = dt.now()
win("You won",start)
sys.exit()