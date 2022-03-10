'''17. Write a function called “check_duplicates” that takes a list and returns true if 
there is any element that appears more than once. Also find the frequency of that 
element. The original list should not be modified.'''
def check_duplicates(n):
    length = len(n)
    duplicates = []
    for i in range(length):
        k = i+1
        for j in range(k,length):
            if n[i] == n[j] and n[i] not in duplicates:
                duplicates.append(n[i])
    return duplicates

list = [1,2,1,3,4,5,6,1,2,7,8,9,1,2,4,5,4,5,3]
print(check_duplicates(list))
