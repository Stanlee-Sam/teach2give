"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""

def rev_integer():
    ipt = input("Enter a number: ")

    if ipt[0] == '-':
        rev_str = '-' + ipt[:0:-1]  
    else:
        rev_str = ipt[::-1]

    rev_num = int(rev_str)

    return rev_num


print(rev_integer())
