'''15. Write a Python function that prints a dictionary where the keys are numbers 
between 1 and 5 and the values are cubes of the keys.'''
n = int(input("Enter a number:"))
d = dict()
for i in range(1, n+1):
    d[i] = i ** 3
print("The dictionary of cubes upto given number = ", d)
