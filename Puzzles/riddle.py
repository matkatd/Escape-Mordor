# from Rooms.Cell_Two import Cell_Two
import random

def valid_guess(Guess) :
    bContinue = True 
    while bContinue == True :
        try: 
            if (Guess.isdigit()) or (len(Guess)) == 0 :
                raise Exception()
            else:
                bContinue = False
        except Exception:
            Guess = input("Please enter a single word as your guess (no numbers or special characters):\n")
            bContinue = True
    return Guess

def answer_riddle(solution):
    print('You have three guesses or we eats it whole!')
    guess_count = 0
    bContinue = True
    bWin = False
    while (guess_count < 3) or (bContinue == True) :
        answer = input('\nWhat could the answer to this riddle be?\n(Enter a single word answer)\n').lower()
        valid_guess(answer)
        guess_count += 1
        if guess_count != 3 :
            if answer == solution :
                print('Bah, it cheats us! No meal for Gollum!\n')
                guess_count = 4
                bContinue = False
                bWin = True
            else :
                guesses_remaining = 3-guess_count
                print(f'\nNope, try again\n(You have {guesses_remaining} guesses remaining)')
        else :
            print("Yay! Gollum was hungry, you'll do!")
            continue  
    return bWin

def read_riddle():
    print('The prisoner wakes violently gurgling out the name, "Gollum! Gollum!"')
    print("After you've asked him about a way out, he agrees to give you a key \nhe nicked from the guards awhile back if you beat him in a game of riddles")
    print("If you lose, he says he'll eat you. You agree hesitantly.")
    riddles_index = random.randint(0, 4)

    riddles = [
        "Riddle: \nWhat has roots as nobody sees,\nIs taller than trees,\nUp, up it goes,\nAnd yet never grows?",
        "Riddle: \nVoiceless it cries\nWingless flutters\nToothless bites\nMouthless mutters.", 
        "Riddle: \nIt cannot be seen, cannot be felt\nCannot be heard, cannot be smelt\nIt lies behind stars and under hills\nAnd empty holes it fills\nIt comes out first and follows after\nEnds life, kills laughter.",
        "Riddle: \nAlive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.",
        "Riddle: \nThis thing all things devours\nBirds, beasts, trees, flowers\nGnaws iron, bites steel\nGrinds hard stones to meal\nSlays king, ruins town,\nAnd beats mountain down."
    ]
    riddles_answers = ["mountain", "wind", "dark", "fish", "time"]
    print(riddles[riddles_index])
    valid = False
    return answer_riddle(riddles_answers[riddles_index])

