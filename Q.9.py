'''9. Write a function that takes a number as an input and finds its reverse and 
computes the sum of its digits.'''
n = 4562
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)
def getSum(n):

    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)

    return sum
getSum(56)
