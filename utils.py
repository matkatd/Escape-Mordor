import os
# contains functions that will be reused in multiple classes
def print_line_of_char(char):
    terminal_width = os.get_terminal_size()[0]
    for i in range(terminal_width):
        print(char, end="")
def print_centered_text(text):
    terminal_width = os.get_terminal_size()[0]
    length_text = len(text)
    if length_text >= terminal_width:
        print(text)
    else:
        half_width = (terminal_width - length_text)//2
        for i in range(half_width):
            print(" ",end="")
        print(text)
