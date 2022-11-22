from Rooms.Cell_Two import Cell_Two
import utils
import random
def read_riddle():
    print("Gollum: \nIntro")
    riddles = [
        {
            "riddle":"What has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows...",
            "answer":"mountain"
        }, {
            "riddle":"Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters...",
            "answer":"wind",
        }, {
            "riddle":"It cannot be seen, cannot be felt,\nCannot be heard, cannot be smelt.\nIt lies behind stars and under hills,\nAnd empty holes it fills.\nIt comes out first and follows after,\nEnds life, kills laughter...",
            "answer":"dark"
        }, {
            "riddle":"Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking...",
            "answer":"fish"
        }, {
            "riddle":"This thing all things devours;\nBirds, beasts, trees, flowers;\nGnaws iron,bites steel;\nGrinds hard stones to meal;\nSlays king, ruins town,\nAnd beats mountain down...",
            "answer":"time"
        }
        ]
    done = False
    while done == False:
        riddles_index = random.randint(0,len(riddles)-1)
        for line in riddles[riddles_index]["riddle"].split("\n"):
            utils.print_centered_text(line)
        user_answer = input("You have a guess? ")
        if user_answer == riddles[riddles_index]["answer"]:
            print("Correct!")
        else:
            print("Wrong!")

def lose_condition():
    pass

def win_condition():
    pass

read_riddle