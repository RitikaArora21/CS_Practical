"""2. Write a Python function to produce the outputs such as:
(a)   1
      21
      321
      4321
b)    1
      121
     12321
     1234321
     12321
     121
     1            """
#(a)
n=int(input("Enter the no. of rows:"))
for i in range(0,n):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()

#(b)
n = int(input("Enter the no. of rows: "))
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(end=" ")
    for j in range (1, i+ 1):
        print(j, end=" ")
    for j in range (i-1, 0, -1):
        print(j, end=" ")
    print()
for i in range (1,n):
    for j in range(1, i+1):
        print(end=" ")
    for j in range (1, n-i):
        print(j, end=" ")
    for j in range (n-i, 0, -1):
        print(j, end=" ")
    print()   
