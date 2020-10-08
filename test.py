import math
cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))