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

def reverseDigits(input1, input2):
    """
    this function reverses the digits of any two integers, whether positive, negative or zero
    sums the reverse of the digits, then reverses the sum

    Parameters
    ----------
    input1 : integer or string
    input2 : integer or string

    Returns
    -------
    reverseSumInt : integer
    """
    
    input1 = int(input1)
    input2 = int(input2)
    
    # because the directions don't say that integers to be summed are positive only, 
    # consider the possibility that they're negative
    if input1 < 0:
        input1 = abs(input1)
        sign1 = -1
    else:
        sign1 = 1
    if input2 < 0:
        input2 = abs(input2)
        sign2 = -1
    else:
        sign2 = 1
    
    # convert input integers to strings and strip any leading zeros
    strInput1 = str(input1).lstrip('0')
    strInput2 = str(input2).lstrip('0')
    
    # reverse the strings
    reverseInput1 = strInput1[::-1]
    reverseInput2 = strInput2[::-1]
    
    # if either of the initial inputs are 0, 
    # then they'll be coded to "" (empty string) when converted to a string
    # and thus need to be coded as 0 when converted back to an integer
    if reverseInput1 == "":
        reverseInputInt1 = 0
    else:
        reverseInputInt1 = int(reverseInput1)*sign1
    if reverseInput2 == "":
        reverseInputInt2 = 0
    else:
        reverseInputInt2 = int(reverseInput2)*sign2
        
    # sum the reversed integers        
    sum = reverseInputInt1 + reverseInputInt2
    
    # if sum is negative, 
    # use its absolute value and convert back to negative later via signSum
    if sum < 0:
        sum = abs(sum)
        signSum = -1
    else:
        signSum = 1
    
    # convert the sum to string
    strSum = str(sum)
    
    # reverse the string
    reverseSum = strSum[::-1]
    
    # convert the reversed string to integer and take its negative if sum was negative 
    reverseSumInt = int(reverseSum)*signSum
    
    return reverseSumInt   

    
# read in the file cases.txt containing 10,000 pairs of integers
# skip the lines containing the positive integer N counter variable
# read in the lines containing the pairs of integers separated by a whitespace
# and print the reversed sum of the reversed digits
with open("cases.txt", "r") as f:
    for line in f.read().split("\n")[1::2]:
        line2 = line.split(' ')
        print(reverseDigits(line2[0], line2[1]))            
        
        
end = time.time()

# rudimentary runtime and memory usage statistics
print(f"Runtime of the program is {end - start}")       
print(psutil.Process(os.getpid()).memory_info()) 