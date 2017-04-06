import sys


def different_inputs():
    if len(sys.argv) == 1:
        print_help()
    else:
        if sys.argv[1] == '-l':
            list_element()
        if sys.argv[1] == '-a':
            add_element()
        if sys.argv[1] == '-r':
            remove_element()
        if sys.argv[1] == '-c':
            complete_element()
            
            
def print_help():
    help_text = open('help.txt', 'r')
    help_text1 = help_text.read()
    print(help_text1)
    help_text.close()
    

def list_element():
    my_file = open('my-todo.txt', 'r')
    my_line = my_file.read()
    #print(my_line)
    my_file.close()
    view_todo()

        
def add_element():
    add_file = open('my-todo.txt', 'r+')
    add_file.write('\n0;' + sys.argv[2].rstrip())
    add_line = add_file.readlines()
    print(add_line)
    add_file.close()


def remove_element():
    remove_file = open('my-todo.txt', 'r+')
    remove_lines = remove_file.readlines()
    print(remove_lines)
    remove_file.close()


def complete_element():
    complete_file = open('my-todo.txt', 'r+')
    complete_lines = complete_file.readlines()
    print(complete_lines)
    complete_file.close()


def view_todo():
    view_file = open('my-todo.txt', 'r')
    number = 1
    for i in view_file:
        lines = i.rstrip().split(';')
        if lines[0] =='1':
            print(number, '[x]', lines[1])
        else:
            print(number, '[ ]', lines[1])
        number += 1
    view_file.close()



different_inputs()