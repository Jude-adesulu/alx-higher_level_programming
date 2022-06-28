#!/usr/bin/python3
def to_upper(c):
    if ord(c) >= 97 and orc(c) <= 122:
        return (ord(c) - 32)
    else:
        return (ord(c))

def uppercase(string):
    str_new = ""
    for c in string:
        str_new += "%c" % to_upper(c)
    print("{:s}".format(str_new))
        
