def pull_torches():
    valid_input = [1, 2, 3]
    answer_array = [1, 1, 3, 1, 2, 3]
    user_array = []
    for i in range(6):
        valid = False
        while valid == False:
            print("1. Pull left torch\n2. Pull middle torch\n3. Pull right torch")
            print("Which torch will you pull: ")
            try:
                user_input = input()
                if int(user_input) in valid_input:
                    user_array.append(int(user_input))
                    valid = True
                else:
                    print("Please enter an integer in the desired range (1-3):")
            except:
                print("Please enter an integer in the desired range (1-3):")
    if user_array == answer_array:
        return True
    else:
        return False

