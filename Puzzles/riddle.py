# from Rooms.Cell_Two import Cell_Two
import random


def read_riddle(self):
    riddles_index = random.randint(0, 2)
    riddles = [{
        "What has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows?":
        "mountain"
    }, {
        "riddle2": "answer2"
    }, {
        "riddle3": "answer3"
    }, {
        "Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.":
        "fish"
    }, {
        "riddle5": "answer5"
    }]

    riddles = [
        "What has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows?",
        "riddle2", "riddle3",
        "Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.",
        "riddle5"
    ]
    riddles_answers = ["mountain", "answer2", "answer3", "fish", "answer5"]
    print(riddles[riddles_index])
    valid = False
    while valid == False:
        try:
            player_answer = input()

            if player_answer == riddles_answers[riddles_index]:
                valid = True
                return valid
            else:
                print("Nope, try again")
        except:
            print("")


def answer_riddle(self):
    pass