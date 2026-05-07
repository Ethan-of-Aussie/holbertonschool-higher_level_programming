#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = abs(number) % 10
lastd = "Last digit of "
if number % 10 > 5:
    print(f"{lastd}{number} is {lastnum} and is greater than 5")
if number % 10 == 0:
    print(f"{lastd}{number} is {lastnum} and is 0")
if number % 10 < 6 and number % 10 != 0:
    print(f"{lastd}{number} is {lastnum} and is less than 6 and not 0")
