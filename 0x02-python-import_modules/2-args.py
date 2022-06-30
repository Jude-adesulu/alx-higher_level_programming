#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 3:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))
    for arg in argv[1:]:
        print("{:d}: {:s}".format(i, arg))
        i += 1
