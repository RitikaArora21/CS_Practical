'''16. Consider a tuple t1=(1,2,5,7,9,2,4,6,8,10). Write a program to perform following 
operations:
a. Print half the values of tuple in one line and the other half in the next line.
b. Print another tuple whose values are even numbers in the given tuple.
c. Concatenate a tuple t2=(11,13,15) witht1.
d. Return maximum and minimum value from this tuple.'''
t1 = (1,2,5,7,9,2,4,6,8,10)

#(a) Print half the values of tuple in one line and other half in the next line.
a = t1[:5]
b = t1[5:]
print(a)
print(b)

#(b) Print another tuple whose values are even numbers in the given tuple.
n = list(t1)
m = list()

for x in n :
    if x in n:
        if (x%2 == 0) :
            m.append(x)
    s = tuple(m)
print("Tuple =",s) 

#(c) Concatenate a tuple t2 (11,13,15) with t1
t2 = (11,13,15)
a = list(t1)
b = list(t2)
c = a+b
print(c)

#(d) Return  maximun and minimum value from this tuple
print("Max number = ",max(t1) )
print("Min number = ",min(t1))
