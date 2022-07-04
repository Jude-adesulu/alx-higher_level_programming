#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    reverse_list = reversed(my_list)
    for int in reverse_list:
        print("{:d}".format(int))
