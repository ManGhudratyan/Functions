# Write a Python program to reverse a string.

def reverseStr(mstr):
    tmp = "";
    for i in mstr:
        tmp = i + tmp;
    return tmp

print(reverseStr('1234abcd'));