'''7. Write a Python function that takes a number as an input from the user and 
computes its factorial.'''
m=int(input("Enter number:"))
fac=1

if (m == 0):
    print("Factorial = 1" )

else:
    for x in range(1,m+1):
        fac = fac*x
        x = x+1
print("Factorial=",fac)
