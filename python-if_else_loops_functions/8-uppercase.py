#!/usr/bin/python3
def uppercase(str):
    str_upper = ''
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) < 123):
            str_upper = str_upper + chr(ord(str[i]) - 32)
            continue
        str_upper = str_upper + str[i]

    print('{}'.format(str_upper))
