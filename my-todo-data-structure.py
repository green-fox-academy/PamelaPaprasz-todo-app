import sys

#print('1;Wake up!'.split(';'))

def no_argument():
    if len(sys.argv) == 1:
        print_help()
def print_help():
    help_text = open('help.txt', 'r')
    help_text = help_text.read()
    print(help_text)



def list_todo():
    if sys.argv[1] == '-l':
        open_list_todo()
def open_list_todo():
    my_todo = open('my-todo.txt', 'r')
    my_todo = my_todo.read()
    print(my_todo)



def add_todo():
    if sys.argv[1] == '-a':
        open_add_todo()
def open_add_todo():
    add_my_todo = open('my-todo.txt', 'r+')
    add_my_todo.write('\n0;' + sys.argv[2].rstrip())
    add_my_todo1 = add_my_todo.readlines()
    print(add_my_todo1)



def remove_todo():
    if sys.argv[1] == '-r':
        open_remove_todo()
def open_remove_todo():
    remove_my_todo = open('my-todo.txt', 'r+')
    remove_my_todo1 = remove_my_todo.readlines()
    print(remove_my_todo1)



def complete_todo():
    if sys.argv[1] == '-c':
        open_complete_todo()
def open_complete_todo():
    complete_my_todo = open('my-todo.txt', 'r+')
    complete_my_todo1 = complete_my_todo.readlines()
    print(complete_my_todo1)


no_argument()
list_todo()
add_todo()
remove_todo()
