import random


def valid_answer(response):
    bContinue = False
    while bContinue == False:
        try:
            response = int(response)
            bContinue = True
        except:
            response = input('Please enter a valid integer as your answer.\n')
    return response


class Fight():

    def __init__(self):
        self.playerHealth = 100
        self.captainHealth = 120
        self.playerMoves = ["stab", "slash", "parry", "sidestep"]
        self.captainMoves1 = ["stab", "parry"]
        self.captainMoves2 = ["slash", "sidestep"]

    def start(self):
        print(
            "You and the captain enter your chosen fighting stances. \nYou feel a rush of adrenaline as you steel your mind and prepare to fight for your life"
        )
        win = False
        while not win:
            print(f"\nPlayer Health: {self.playerHealth}")
            print(f"Captain Health: {self.captainHealth}")
            self.printOptions()
            selectedMoveIndex = input(
                "Select the number of the move you would like to use: ")
            selectedMoveIndex = valid_answer(selectedMoveIndex)
            selectedMove = self.playerMoves[int(selectedMoveIndex) - 1]
            captainMove = self.getCaptainMove()

            self.fight(selectedMove, captainMove)
            if (self.playerHealth <= 0):
                return win
            if (self.captainHealth <= 0):
                print("You beat the captain!")
                win = True
                return win

    def printOptions(self):
        print("\nWhat would you like to do?")
        num = 1
        for i in self.playerMoves:
            print(f"{num}: {i}")
            num += 1

    def getCaptainMove(self):
        setIndex = random.randint(0, 1)
        moveIndex = random.randint(0, 1)
        if (setIndex == 0):
            return self.captainMoves1[moveIndex]
        else:
            return self.captainMoves2[moveIndex]

    def fight(self, playerMove, captainMove):
        print("\n")
        if (playerMove == "stab"):
            if captainMove == "stab":
                print("You both stab each other. \nOuch!")
                self.playerHealth -= 15
                self.captainHealth -= 15
            elif captainMove == "slash":
                print("The captain slashes you, while you only stab at him")
                self.playerHealth -= 20
                self.captainHealth -= 15
            elif captainMove == "parry":
                print(
                    "The captain attempts to parry, but you run him through. \n(a little, anyways...)"
                )
                self.captainHealth -= 15
            elif captainMove == "sidestep":
                print("The captain successfully evades your stab. \nBummer.")

        elif playerMove == "slash":
            if captainMove == "stab":
                print(
                    "You slash the captian, while he pokes you agressively. \nOuch!"
                )
                self.playerHealth -= 15
                self.captainHealth -= 20
            elif captainMove == "slash":
                print("You both slice each other. \nOuch!")
                self.playerHealth -= 20
                self.captainHealth -= 20
            elif captainMove == "parry":
                print("The captain sucessfully parries your slash. \nBummer.")
            elif captainMove == "sidestep":
                print(
                    "The captain attempts to sidestep your slash, but you get him anyways."
                )
                self.captainHealth -= 20

        elif playerMove == "parry":
            if captainMove == "stab":
                print(
                    "You attempt to parry, but the captain still pokes you. \nOuch!"
                )
                self.playerHealth -= 15
            elif captainMove == "slash":
                print("You successfully parry the captains attack. \nHuzzah!")
            elif captainMove == "parry":
                print(
                    "You both parry at the same time. Could this be a new form of dance?"
                )
            elif captainMove == "sidestep":
                print(
                    "You parry while the captain sidesteps at the same time. \nThe surrounding orcs start chuckling at you."
                )

        elif playerMove == "sidestep":
            if captainMove == "stab":
                print("You successfully avoid the captain's attack. \nHuzzah!")
            elif captainMove == "slash":
                print(
                    "You attempt to avoid the captain's attack, but he still gets you. \nOuch!"
                )
                self.playerHealth -= 20
            elif captainMove == "parry":
                print(
                    "You sidestep while the captain tries to parry at the same time. Could this be a new form of dance?"
                )
            elif captainMove == "sidestep":
                print(
                    "You both sidestep at the same time. The surrounding orcs start chuckling at you."
                )


# game = Fight()

# game.start()