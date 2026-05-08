#!/usr/bin/env python3
def uppercase(str):
    newstr=""
    for i in str:
        if ord(i) >96 and ord(i)< 123:
            newstr+=chr(ord(i)-32)
        else:
            newstr+=i
    print(newstr)
