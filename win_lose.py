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
    read_file = open("myscores.txt", "r")
    old_score = read_file.readline()
    read_file.close()
    write_file = open("myscores.txt", "w")
    if old_score == "":
        print("Congrats on your first recorded playthrough!")
        write_file.write(str(current_score))
        sys.exit()
    elif old_score == str(current_score):
        print(f"You matched your best score of {old_score}")
        write_file.write(str(old_score))
    elif str(old_score) < str(current_score):
        print(f"Oooo you missed beating your best score of {old_score}")
        write_file.write(str(old_score))
    else:
        print(f"Congrats of beating your best score of {old_score}")
        write_file.write(str(current_score))
    write_file.close()
        
    sys.exit()
