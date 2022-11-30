
def valid_answer(response) :
    bContinue = False
    while bContinue == False :
        try:
            response = int(response)
            bContinue = True
        except:
            response = input('Please enter a valid integer as your answer.\n')
    return response

def check_solution(answer,response) : 
    bContinue = False
    answer = int(answer)
    while bContinue == False :
        if response == answer :
            bContinue = True
        else :
            response = input("That's incorrect, try again.\n")
            response = (valid_answer(response))
    return response

def cipher_solver() :
    bComplete = True
    print('Sauron gave 9 rings to men\n7 to the dwarves\n3 to the elves\nand he crafted the 1 master ring.')
    response = input('How many rings were crafted total?\n(Type a number as your answer)\n')
    response = valid_answer(response)
    cipher1 = check_solution(20,response)

    print('There looks to be one more problem...\n')
    print('Sauron has the 9 nazgul, his foes had the 5 wizards, but one dissented from them to serve the Dark Lord.')
    response = input('If each of the wizards that oppose Sauron defeat 2 nazgul, how many nazgul will remain?\n')
    response = valid_answer(response)
    cipher2 = check_solution(1,response)
    print(f'\nThe solutions were {cipher1} and {cipher2}\nI have a feeling those numbers may be important.')
    return bComplete

cipher_solver()