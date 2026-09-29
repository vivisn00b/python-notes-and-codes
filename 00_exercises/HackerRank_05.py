# You are given a spreadsheet that contains a list of athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

# Note that is indexed from to , where is the number of attributes.
# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
# Input Format
# The first line contains and separated by a space.
# The next lines each contain elements.
# The last line contains .

# Each element
# Output Format
# Print the lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
# Sample Input 0

# ```
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# ```

# Sample Output 0

# ```
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# ```

# https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
    sorted_arr=sorted(arr, key=lambda x:x[k])
    
    for row in sorted_arr:
        print(*row)
