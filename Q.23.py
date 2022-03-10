'''23. Implementation of selection sort, insertion sort, and bubble sort techniques'''
#Selection sort
n = int(input("Enter the length of the list : "))
a = []
for i in range(n):
    s = int(input("Enter the value : "))
    a.append(s)

for i in range(n-1):
    for j in range (i+1,n):
        if a[i] > a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t
print("Sorted array by selection sort : ",a)
#Insertion sort
n = int(input("Enter the length of the list : "))
a = []
for i in range(n):
    s = int(input("Enter the value : "))
    a.append(s)

for i in range(1,n):
    t = a[i]
    j = i-1
    while j >= 0 and t < a[j]:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = t
print("Sorted array by insertion sort : ",a)
                            
#Bubble Sort                       

n = int(input("Enter the length of the list : "))
a = []
for i in range(n):
    s = int(input("Enter the value : "))
    a.append(s)

for i in range(n):
    for j in range(0,n-i-1):
        if a[j] > a[j+1] :
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t 
print("Sorted array by bubble sort : ",a)
