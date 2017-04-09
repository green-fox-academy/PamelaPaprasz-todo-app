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
    my_file.close()
    view_todo()

            
    
def add_element():
    add_file = open('my-todo.txt', 'a')
    add_element = '\n0;' + sys.argv[2].rstrip()
    add_line = add_file.writelines(add_element)
    add_file.close()
    view_todo()


def remove_element():
    remove_file = open('my-todo.txt', 'r+')
    remove_list = remove_file.readlines()
    remove_index = int(sys.argv[2])-1 # commadline arguments are strings always 
    item_to_delet = ''
    for i in range(len(remove_list)): #while looping through a list it is not recommended to delete element until the loop finished
        if i == remove_index:
            item_to_delet = remove_list[i]
    remove_list.remove(item_to_delet) #remove method delet the string but not the index of an element
    #print(remove_list)
    remove_file.close()
    remove_file = open('my-todo.txt', 'w')
    for i in remove_list:
        remove_file.write(i)
    remove_file.close()
    view_todo()
    
    
    
def complete_element():
    complete_file = open('my-todo.txt', 'r+')
    complete_lines = complete_file.readlines()
    checker_index = int(sys.argv[2])-1
    for i in range(len(complete_lines)):
        if i == checker_index:
            split_item = complete_lines[i].split(';')
            if split_item[0] =='0':
                split_item[0] = '1'
                split_item = ';'.join(split_item)
                complete_lines[i] = split_item
    complete_file.close()
    complete_file = open('my-todo.txt', 'w')
    for i in complete_lines:
        complete_file.write(i)
    complete_file.close()
    view_todo()

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