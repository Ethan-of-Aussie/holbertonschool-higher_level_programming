#!/usr/bin/python3
import sys
accumulate = 0
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        accumulate = int(arg) + accumulate
    print("{}".format(accumulate)
