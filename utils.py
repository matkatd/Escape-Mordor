import os
# contains functions that will be reused in multiple classes
def print_char_width(char):
    size = os.get_terminal_size()
    for i in range(size[0]):
        print(char)