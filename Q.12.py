'''12. Write a function that finds the sum of the 
a) first n odd terms 
b) first n even terms
c) 1, 2, 4, 3, 5, 7, 9, 6, 8, 10, 11, 13.. till n-th term.'''
m = int(input("Enter the number: "))
sum=0
i=1
while(i<=m):
    sum=sum+i
    i=i+2
print("sum of odd numbers=",sum)


#(b) Sum of first n even natural numbers

n = int(input("Enter the number: "))
sum=0
i=2
while(i<=n):
    sum=sum+i
    i=i+2
print("sum of even numbers=",sum)
