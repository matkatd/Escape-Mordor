from unicodedata import name
import random

def valid_guess(Guess) :
    bContinue = True 
    while bContinue == True :
        try: 
            if (len(Guess) > 1) or (Guess.isdigit()) or (len(Guess)) == 0 :
                raise Exception()
            else:
                bContinue = False
        except Exception:
            Guess = input("Please enter a single letter guess:\n")
            bContinue = True
    return Guess
# here's the list of songs you randomly get to guess at
lotrNames = ["aragorn", "frodo", "baggins", "elrond", "gandalf","galadriel", "saruman", "sauron"]

# call this function to start a game
def play_game() :
    bWin = False
    guess_count = 0
    print('You have 12 guesses to win this hangman style game. Good luck prisoner.\n')
    iRanNum = random.randint(0,7) # randomly selects a position to use as the index
    # selects the random song
    RandomName = lotrNames[iRanNum]
    lstNamesLetters = []
    lstUnderScoredName = []
    UnderScoredName = ''
    # this for loop will make UnderScoredName the right length
    for chr in range(0,len(RandomName)) :
        lstNamesLetters.append(RandomName[chr]) # this is a list of the letters in the RandomName to use for finding more easily.
        UnderScoredName += '_' # equal length string of all underscores
        lstUnderScoredName.append('_') # will use to check against lstNamesLetters
    
    tempLetterList = lstNamesLetters # to use to check for repeated letters
    # oContestant = Contestant()
    # initializes the dictionary before the guessing begins
    dictAlphabet = { 'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0,
    'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0 }
    bContinue1 = True
    sOutput = ''
    while bContinue1 : # will continue accepting guesses until you get the song or exceed 20 guesses
        sGuess = input("Enter a single letter of the alphabet as your guess\n").lower()
        sGuess = valid_guess(sGuess)
        if dictAlphabet[sGuess] == 1 : # makes sure they make a unique guess
            sGuess = input("You already guessed that, try again\n").lower()
            sGuess = valid_guess(sGuess)
        else: 
            bContinue2 = True
            while bContinue2 == True :
                length = len(lstNamesLetters)
                if sGuess in dictAlphabet :
                    dictAlphabet[sGuess] += 1
                while sGuess in(tempLetterList) :
                    for cnt in range(0,length) :
                        if lstNamesLetters[cnt] == sGuess :
                            place = lstNamesLetters.index(sGuess)
                            lstUnderScoredName[place] = sGuess # replaces the value stored in this list at the position the letter was last found in the song
                            tempLetterList[place] = '_' 
                    for l in lstUnderScoredName :
                        print(l.upper(), end='')    
                    print('\n')
                else : # eventually must iterate to this once all instances of a guess have been replaced in the lstUnderScoredName
                    guess_count += 1
                    bContinue2 = False
        UnderScoredName = ''

        for iCount in range (0,len(lstUnderScoredName)) :
            UnderScoredName += lstUnderScoredName[iCount]
        if (UnderScoredName == RandomName) :
            sOutput = f'Correct! You used {guess_count} guesses\nThe name was {RandomName.capitalize()}'
            print(sOutput)
            bContinue1 = False
            bWin = True
        elif guess_count > 20 :
            print("You took too many guesses!")
            bContinue1 = False
    return bWin
        
play_game()
        