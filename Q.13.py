'''13. Write a Python function that takes a string as an input from the user and 
determines whether it is palindrome or not.'''
def palindrome(s):
    if(s == s[::-1]):                        #the reverse remains same as input(palindrome)
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

palindrome("pauap")
