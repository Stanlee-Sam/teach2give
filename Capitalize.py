"""
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string.
Examples: 
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"

"""

string = input("String: ")
words = string.split()
cap = [word.capitalize() for word in words]
rstring = ' '.join(cap)

print(rstring)
