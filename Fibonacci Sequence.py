"""Write a program to generate the Fibonacci sequence up to 100"""

#create function
def fib(lim):
    fibonacci = [0,1]

    while fibonacci[-1] + fibonacci[-2]  <= lim:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci

#call function
fibonacci = fib(100)
print(fibonacci)