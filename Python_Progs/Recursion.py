def fact(n):
    if n<=1:
        return 1
    return n* fact(n-1)
n=int(input("Enter the number for finding its factorial : "))
print("Factorial of ",n," is : ",fact(n))









