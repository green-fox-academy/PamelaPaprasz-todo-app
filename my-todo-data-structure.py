import sys

#print('1;Wake up!'.split(';'))

def arg_reader():
    if len(sys.argv) == 1:
        print_help()

def print_help():
    help_text = open('help.txt', 'r')
    help_text = help_text.read()
    print(help_text)

arg_reader()
