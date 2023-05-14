#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# My code
def missingCharacters(s):
    # Write your code here
    result = ''
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in s: 
            result += char
    return result
# End my code
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()
