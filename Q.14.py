'''14. Write a function that takes a sentence as input from the user and calculates the 
frequency of each letter. Use a variable of dictionary type to maintain the count.'''
text = input("Enter a phrase :")
f = {}
for i in text:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
print("Frequency of each letter :", f)
