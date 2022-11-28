from unicodedata import name
import random

class Person() :
    def __init__(self,fname,lname) :
        self.__first_name = fname
        self.__last_name = lname
    def get_fname(self) :
        return self.__first_name
    def get_lname(self) :
        return self.__last_name
    def set_fname(self) :
        self.__first_name = input("Enter first name: ")
    def set_lname(self) :
        self.__last_name = input("Enter last name: ")

class Games() :
    def __init__(self,guesscnt) :
        self.guess_count = guesscnt

# make contestant class inherit from person
class Contestant(Person) :
    def __init__(self, fname, lname,gamecount = 0):
        super().__init__(fname, lname)
        self.game_count = gamecount
        self.games_played = []
    # this method will show how many guesses you took and how many games played
    def show_results(self) :
        if self.game_count == 0 :
            output = self.get_fname() + ' ' + self.get_lname() + ' has not played a game'
        else :
            TotalGuesses = 0
            for g in range(0,len(self.games_played)) : 
                TotalGuesses += self.games_played[g].guess_count # should add up all the guesses from each game
            output = f'{self.get_fname()} {self.get_lname()} used a total of {TotalGuesses} guesses'
        return output
# made a function to see if the names you enter have any length
def valid_name(name) :
    bContinue = True 
    while bContinue == True :
        try: 
            if len(name) > 0 :
                bContinue = False
            else : # this will throw an error on purpose to force them to the except to fix the name
                1 + 'happy'
        except:
            name = input("Please enter a valid name:\n")
            bContinue = True
    return name

def valid_guess(Guess) :
    bContinue = True 
    while bContinue == True :
        try: 
            if len(Guess) > 1 or (Guess.isdigit()) :
                # this will throw an error on purpose to force them to the except to fix the name
                1 + 'happy'
            else:
                bContinue = False
        except:
            Guess = input("Please enter a single letter guess:\n")
            bContinue = True
    return Guess
# here's the list of songs you randomly get to guess at
lotrNames = ["aragorn", "frodo", "baggins", "elrond", "gandalf","galadriel", "saruman", "sauron"]

# call this function to start a game
fName = input('Enter player first name: ')
fName = valid_name(fName) 
lName = input("Enter players last name: ")
lName = valid_name(lName)
def play_game(fname,lname) :
    guess_count = 0

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
    oContestant = Contestant(fname,lname)
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
                    print(lstUnderScoredName)
                else : # eventually must iterate to this once all instances of a guess have been replaced in the lstUnderScoredName
                    guess_count += 1
                    bContinue2 = False
        UnderScoredName = ''

        for iCount in range (0,len(lstUnderScoredName)) :
            UnderScoredName += lstUnderScoredName[iCount]
        if (UnderScoredName == RandomName) :
            sOutput = f'Correct! You used {guess_count} guesses\nThe name was {RandomName.capitalize()}'
            print(sOutput)
            # increment games played and create game object
            oGame = Games(guess_count)
            oContestant.game_count += 1
            # append game object to list of games played
            oContestant.games_played.append(oGame)
            print(oContestant.show_results())
        elif guess_count > 20 :
            print("You took too many guesses!")
            PlayAgain = input("Would you like to play again (Y:N)\n").upper()
            bContinue1 = True
            while bContinue1 :
                PlayAgain = input("Enter a valid Y or N\n").upper()
                if PlayAgain == 'Y' :
                    play_game(fName,lName)
                    bContinue1 = False
                elif PlayAgain == 'N' :
                    print(oContestant.show_results())
                    bContinue1 = False
                else :
                    PlayAgain = input("Enter a valid Y or N")
        
play_game(fName,lName)
        