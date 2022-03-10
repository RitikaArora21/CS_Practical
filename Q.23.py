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
