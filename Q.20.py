'''20. Write a Python program to perform the following using list:
a. Check if all elements in list are numbers or not
b. If it is a numeric list, then count number of odd values in it
c. If list contains all Strings, then display largest String in the list
d. Display list in reverse form
e. Find a specified element in list
f. Remove the specified element'''
list = []
print("Make a list first!")
user_input = int(input("Enter the length of the list : "))

for i in range(user_input):
    value = input("Enter values in list :")
    list.append(value)

def check_and_odd():
    count = 0
    for item in list:
        if item.isalpha():
            print("All the values in list are not numeric")
            exit()
        if item.isnumeric():
            for i in item:
                if int(i) % 2 != 0:
                   count =  count + 1                  
    print("The list contains all numeric values and the odd values in list is = ",count)   
        
# (c)If list contains all strings,then display largest string in the list
   
def largest_string():
    m = max(list,key = len)
    print("The largest string in the list = ",m)

#(d)Display list in reverse form

def reverse():
    print("The original list = ",list)
    print("The reversed list = ",list[::-1])

#(e)Find a specified element in list

def find_in_list():
    n = input("Enter value to find : ")
    ind = list.index(n)
    print("The value is at index",ind)


#(f)Remove the specified element from the list

def remove():
    n = input("Enter the value to remove : ")
    print("The original list = ",list)
    list.remove(n)
    print("The new list after removing specified value =  ",list)


print("""What should I do for you? Select from the following:
1 = Check if all the values in list are numbers or not and if all values are numeric
          count the number of odd values in the list.
2 = Display the largest string in the list.
3 = Find a specified element in list.
4 = Remove the specified element from the list """)

choice = int(input("What is your choice : "))
if choice == 1:
    check_and_odd()
elif choice == 2 :
    largest_string()
elif choice == 3 :
    find_in_list()
elif choice == 4 :
    remove()
else:
    print("Invalid choice!")
