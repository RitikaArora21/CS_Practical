'''5. Write a program that reads an integer value and prints “leap year” or “not a leap 
year”.'''
def year(n):
    if (n%400 == 0 ) and (n%100 == 0):
        print(n,"is a leap year")

    elif (n%4 == 0) and (n%100 != 0):
        print(n,"is a leap year")

    else:
        print(n,"is a not leap year")
       

year(2000)
