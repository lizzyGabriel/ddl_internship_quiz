#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    symbol = '#'
    for i in range(1, n+1):
        print(('#' * i).rjust(n))
if __name__ == '__main__':
    n = int(input('enter an integer:'))
    staircase(n)
