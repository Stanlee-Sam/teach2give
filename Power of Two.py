"""Write a program that takes an integer as input and returns true if the input is a power of two.
Examples: 
8=> returns true
6=> returns false
"""

x = int(input("Number: "))

if x <= 0: 
  print (False)

else:
  power = (x & (x - 1)) == 0

print(power)