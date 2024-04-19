"""
Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
"FizzBuzz".
"""

for n in range(1,101):

    if n % 3 == 0:
        print("fizz")

    elif n % 5 == 0:
        print("buzz")

    elif n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")

    else:
        print(n)
