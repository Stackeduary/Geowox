##### Instructions:

# add two reversed numbers and output their reversed sum

# assume that no zeros were lost by reversing

# Input
# The input consists of N cases (equal to about 10000). 
# The first line of the input contains only the positive integer N
# The cases follow on the next line
# Each case consists of exactly one line with two integers separated by a space. 
# These are the reversed numbers you are to add.

# Output
# For each case, print exactly one line containing only one integer: the reversed sum of two reversed numbers. 
# Omit any leading zeros in the output.
# If nothing is to be printed, print 0 instead.

# Example
# Sample input Sample output
# 3 34
# 24 1 1998
# 4358 754 1
# 305 794

import psutil
import os
import time

start = time.time()

def reverseDigits(num):    
    number = int(num)
    if number > 0:
        sign = 1
    else:
        sign = -1
    number *= sign
    reverse = 0
    while number > 0:
      remainder = number % 10  # Finding the remainder
      reverse = reverse*10 + remainder
      number = number//10  # Finding the quotient
    return reverse*sign  

    
# read in the file cases.txt containing 10,000 pairs of integers
# skip the lines containing the positive integer N counter variable
# read in the lines containing the pairs of integers separated by a whitespace
# and print the reversed sum of the reversed digits
with open("cases.txt", "r") as f:
    for line in f.read().split("\n")[1::2]:
        line2 = line.split(' ')
        print(reverseDigits(reverseDigits(line2[0]) + reverseDigits(line2[1])))
        
        
end = time.time()

# rudimentary runtime and memory usage statistics
print(f"Runtime of the program is {end - start}")       
print(psutil.Process(os.getpid()).memory_info()) 