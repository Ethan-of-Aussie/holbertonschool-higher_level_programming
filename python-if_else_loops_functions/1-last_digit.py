#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = number % 10
if number < 0:
    lastnum = -(abs(number) % 10)

lastd = "Last digit of "

if lastnum > 5:
    print(f"{lastd}{number} is {lastnum} and is greater than 5")

elif lastnum == 0:
    print(f"{lastd}{number} is {lastnum} and is 0")

else:
    print(f"{lastd}{number} is {lastnum} and is less than 6 and not 0")
