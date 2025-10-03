# Task 1: Calculate Factorial Using a Function

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter the Number:"))
res = fact(n)
print(f"The Factorial of {n} is {res}")
