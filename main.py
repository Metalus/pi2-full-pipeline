# Access point for translating braille to text and vice verse.
import printer, alphaToBraille, brailleToAlpha
from sys import argv


def menu():
    print('''
    Usage:
        main.py <parameter>
        main.py <file name> <parameter>
    Parameters:
        --braille | -b      translate braille to text
        --text    | -t      translate text to braille
        --help    | -h      display this screen
        --map     | -m      print translation map
    ''')


def user_braille():
    print("Input Braille: ", end="")
    print(brailleToAlpha.translate(input()))


def user_text():
    print("Input Text: ", end="")
    print(alphaToBraille.translate(input()))


def open_braille(filename):
    #file = open(filename)
    #content = file.read()
    oi = brailleToAlpha.translate(filename)
    print(f"Texto literal: {oi}")


def open_text(filename):
    content = filename
    file = open('out', 'w')
    file.write(alphaToBraille.translate(content))


def argument_handler():
    if len(argv) == 1:
        menu()
    elif len(argv) == 2:
        if argv[1] == "--braille" or argv[1] == "-b":
            user_braille()
        elif argv[1] == "--text" or argv[1] == "-t":
            user_text()
        elif argv[1] == "--map" or argv[1] == "-m":
            printer.all_braille()
        else:
            menu()
    elif len(argv) == 3:
        if argv[2] == "--braille" or argv[2] == "-b":
            #print("Literal text: ", ' ')
            open_braille(argv[1])
        elif argv[2] == "--text" or argv[2] == "-t":
            #print("Braille: ", ' ')
            open_text(argv[1])
        elif argv[2] == "--map" or argv[2] == "-m":
            printer.all_braille()
        else:
            menu()
    else:
        menu()


if __name__ == "__main__":
    argument_handler()
