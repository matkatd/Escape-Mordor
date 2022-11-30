def cipher_solver() :
    print('Sauron gave 9 rings to men\n7 to the dwarves\n3 to the elves\nand he crafted the 1 master ring.')
    answer1 = 20
    response = int(input('How many rings were crafted total?\n(Type a number as your answer)'))
    bContinue = True 
    while bContinue == True :
        if response == answer1 :
            bContinue = False
        else :
            response = int(input("That's incorrect, try again."))
    print('There looks to be one more problem')
    print('')