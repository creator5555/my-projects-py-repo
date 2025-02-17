# Define a function that applies fibonacchi using recursion

def fibonacchi1():
    list1 = []
    result2 = 0
    result1 = 0
    print("enter any number : ")
    num1 = int(input("here = "))
    for i in range(num1):

        if i < 2:
            result1 = result1 + i
            list1.append(result1)
    for j in range (num1):
        result2 = list1[j] + list1[j + 1]
        
        list1.append(result2)

    return list1

    
print(fibonacchi1())


# Write a Python program to remove an item from a given set

def remove1():
    list2 = []

    print("enter the number of numbers you want to assign in the list")
    num2 = int(input())

    for i in range(num2):
        num3 = int(input())
        list2.append(num3)

    print(list2)
    my_set = set(list2)

    list1 = list(my_set)
    print("enter the number you want to delete")
    num1 = int(input())
    list1.remove(num1)
    set2 = set(list1)

    print(set2)

# Write a Python program to removes multiple items from a given set

def remomve2():
    list2 = []

    print("enter the number of numbers you want to assign in the list")
    num2 = int(input())

    for i in range(num2):
        num3 = int(input())
        list2.append(num3)

    print(list2)
    my_set = set(list2)

    list1 = list(my_set)

    print("enter how many numbers you want to delete")
    num4 = int(input())
    print("enter the number you want to delete")
    for j in range(num4):
        
        num1 = int(input())
        list1.remove(num1)
        set2 = set(list1)

    print(set2)

# Write a Python program to find the index of an item in a tuple.

def tuple_index():
    print("how many items do you want to add ? ")
    num1 = int(input())
    list1 = []

    for i in range(num1):
        print("write the items")
        str1 = input()
        list1.append(str1)

    set1 = set(list1)
    print(set1)

    list1 = list(set1)
    print(list1)

    print("what item do you want to know its index ? ")
    str2 = input()
    ind1 = list1.index(str2 , 0 , len(list1))
    print(str2 ,"index is :", ind1)

# Ask user to input a sentence then convert this sentence into list of words. (hint: search for split function)

def sentence1():

    print("enter a sentenece")
    str1 = input()
    list1 = str1.split(" ")
    print(list1)

# Take a string from the user and if it's Palindrome print "Palindrome" otherwise print "Not a Palindrome"

def palindrome():
    print("enter any word")
    str1 = input()
    str6 = str1

    str2 = []
    str3 = []
    str4 = []
    str5 = []
    for i in range(0 , len(str1)):
        str2 = str1[i]
        str3.append(str1[i])

    # print(str3)

    for j in range(len(str3)):
        str4 = str3.pop()
        str5.append(str4)

    # print(str5)

    str6 = "".join(str5)
    print(str6)

    if str6 == str1:
        print("the word is palindrome")

    else:
        print("the word is not pallindrome")

# find the factorial of a number 

def factorial():
    list1 = []
    num2 = 0
    num3 = 1
    print("enter the number you want to factorial")
    num1 = int(input())

    for i in range( 1 , num1):
        
        num2 = num1 - i
        # print(num2)
        list1.append(num2)
    list1.append(num1)

    print(list1)

    for j in range(len(list1)):
        num3 = num3 * list1[j]

    print(num3)

# Create a List of Squares of Numbers from 1 to 10

def Squares_nums():

    import math

    list1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
    list2 = []
    for i in range(len(list1)):
        num1 = pow(list1[i] , 2)
        list2.append(num1)

    print(list2)

# Create a function that Calculates the Sum of Even Numbers in a List

def sum_even():
    list1 = []
    num3 = 0
    print("enter the amount of numbers in the list")
    num1 = int(input())

    for i in range(num1):
        print("enter the numberes you want to add to the list")
        num2 = int(input())
        list1.append(num2)
    print(list1)

    #list now contain numbers

    for j in range(len(list1)):
        if list1[j] % 2 != 0:
            num3 = num3 + list1[j]

    print(num3)

# Create a function that takes a list as input and return reversed list

def reversed1():
    list1 = []
    list2 = []

    num3 = 0
    print("enter the amount of numbers in the list")
    num1 = int(input())

    for i in range(num1):
        print("enter the numberes you want to add to the list")
        num2 = int(input())
        list1.append(num2)
    print(list1)

    #list now contain numbers

    for j in range(len(list1)):
        num4 = list1.pop()
        list2.append(num4)

    print(list2)

# create a function that calculates the median of a list of numbers (a median is the middle element in sorted list of numbers)

def median():
    list1 = []
    list2 = []

    num3 = int()
    num4 = int()

    print("enter the amount of numbers in the list")
    num1 = int(input())

    for i in range(num1):
        print("enter the numberes you want to add to the list")
        num2 = int(input())
        list1.append(num2)


    #list now contain numbers


    for i in range(num1):
        num_min = min(list1)
        list2.append(num_min)
        list1.remove(num_min)
        

    print(list2)

    #now list is sorted
    num3 = max(list2)
    num4 = min(list2)

    result = (num3 + num4) / 2
    print(result)

# create a function that calculates the mode of a list of number (mode is the most frequent element in a list)

def count1():
    from collections import Counter

    def find_mode(lst):
        if not lst:
            return None  # Handle empty list case

        freq_count = Counter(lst)  
        max_count = max(freq_count.values())

        mode = [num for num, count in freq_count.items() if count == max_count]

        return mode[0] if len(mode) == 1 else mode  


    print("enter how many numbers you want to enter")
    n = int(input())

    for i in range(n):
        print("enter numbers")
        lst.append(int(input()))


    print(find_mode(lst)) 

    #///////////////////////////////////////////////////////////////////////////

# Task: take the mark from the user and convert it to grade according to the following guidelines
def user_tasks():

    str1 = str()
    print("enter your grades")
    num1 = int(input())

    if 85 <= num1 <= 100:
        str1 = "A"

    if 75 <= num1 <= 85:
        str1 = "B"

    if 65 <= num1 <= 75:
        str1 = "c"

    if 50 <= num1 <= 65:
        str1 = "D"

    if num1 <= 50:
        str1 = "F"

    print("your grades is : " , num1)
    print("you have got : " , str1 )

