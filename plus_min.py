#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    const: int = len(arr)
    under_zero: list[int] = [value for value in arr if value < 0]
    zero: list[int] = [value for value in arr if value == 0]
    above_zero: list[int] = [value for value in arr if value > 0]
    
    if len(under_zero) > 0:
        uz: float = len(under_zero) / const
    else:
        uz: float = 0
    
    if len(zero) > 0:
        z: float = len(zero) / const
    else:
        z: float = 0
    
    if len(above_zero) > 0:
        az: float = len(above_zero) / const
    else:
        az:float = len(above_zero) / const
    print(f'{az:.6f} ::: {z:.6f} ::: {uz:.6f}')
    return [uz, z, az]
    # Write your code here

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
