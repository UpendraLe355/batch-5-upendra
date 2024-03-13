# Eg:3

#? take value of length and breadth of a
#? from user and check if it is square or not

# length = int(input())
# breadth = int(input())
# if length==breadth:
#     print("its a square")
# else:
#     print("its not square")
    
# Eg:4

# python program to check whether the
# given integer is a multiple of both 5 and 7

# n = int(input("enter the number:"))
# if n%5==0 and n%7==0:
#     print("yes")
# else:
#     print("no")

# Eg:5

# write a program to accept the cost price of a bike and display
# the road tax to be paid
# according to the following criteria:

#        cost price (in Rs)                  Tax
#        > 100000                            15 % + discount 6%
#        > 50000 and <= 100000               10%
#        <= 50000                            5%

# price = int(input("enter the price:"))
# total = 0
# if price>=100000:
#     discount = price*(6/100)
#     value = price-discount
#     tax=value*(15/100)
#     total=value+amount
# else:
#     tax = price*(5/100)
#     total = price+tax
# print(" The on road cost of bike is: ",total)

# if elif
# Eg:1
# a = 7
# b = 9
# c = 3

# if a>b and a>c:
#     print(" a is greater")
# elif b>a and b>c:
#     print(" b is greater")
# else:
# print(" c is greater") # ==> b is greater

# A school has following rulse grading systm:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# mark = int(input("enter mark:"))
# if mark>=80 and mark<=100:
#     print("a")
# elif mark>=60 and mark<=80:
#     print("b")
# elif mark>=50 and mark<=60:
#     print("c")
# elif mark>=45 and mark<=50:
#     print("d")
# elif mark>=25 and mark<=45:
#     print("e")
# else:
#    print("fail")
    
#Eg:6
# Accept the age of 4 people and display the oldest one.

#! ---> Short hand if else
#Eg:1

# a = 9
# b = 60
# if a>b:
#     print("A")
# else:
#     print("B")

#? ---> using short hand if else
#  * Rulse
# 1. Statement inside the if condition have to be present at first
# 2. elif cannot be used in short hand if else
# 3. Always it have to end with else

# print("A") if a>b else print("B")

#! code to check the given char is vowel or consonent
# char = input("enter the char:")
# if char=="a" or char=="e" or char=="o" or char=="u" 
#     print("is a vowel")
# else:
#     print("its consonent")

#  or
# char = input("enter the char:")
# str1 = "aeiouAEIOU"
# if char in str1:
#     print("vowel")
# else:
#     print("consonent")

# ---> using shorthand else

# char = input("enter the char:")
# str1 = "aeiouAEIOU"
# print("vowels") if char in str1 else print("consonent")

# ---> elif ladder using short hand if else
# Eg:1
# ? find greatest among 3 variables using shorthand if else

# a = 8
# b = 5
# c = 9

# print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c else print("c is greater")

# looping can be implimented using
# for loop
# while loop

# ---> for loop
# for loop is used for iteartion, if wee know the number of times the loop have to run
# it is used to iterate the iterables Eg: (str, list, tuple,etc...)

# todo --> syntax for loop

#! for syntax in c
# for(i=0;i<10;i++){
# print("hello");
# }

#! for syntax in python
# for userdefined_variable in range(start, end, step): default step value is 1
#     statement
#     statement
#     statement

# ? Eg:
# To print the value from 1 to 10 using for loop

# for i in range(0, 10): # (n, n-1)
#     print(i) 
# ===>  1
#       2
#       3
#       4
#       5
#       6
#       7
#       8
#       9

#? EG:2
# for upi in range(23,50,5):
#     print(upi)

# for upi in range(23,50,9):
#     print(upi)

# for i in range(2,37,6):
#     print(i) 

# Eg:3

# for i in range(40,5,-3):
#     print(i)

# Eg:4
# ! print the output of 7th multiplication table from 21 to 43

# for i in range(1,10+1):
#     print(i*7)
# ===>
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63

# for i in range(1, 10+1):
#     print('19', 'x', i,'=',i*19) #--> method 1

# ---> method 2

#    ans="19x{}={}"
#    print(ans.format(i, i*19))

# ---> method 3
#    print(f"19 X {i} = {i*19}")

# Eg:4
# -->Break --> used to terminate the loop
# for i in range(1,10):
#     if i ==9:
#         break
#     print(i)
    
# Eg:5

# for i in range(1,10):
#     print(i)
#     if i ==6:
#        break

# Eg:6

# for i in range(1,10):
#     if i ==6:
#         print(i)
#         break

# ! Continue
# Eg:1
# for i in range(1,10):
#     if i ==6:
#         continue
#     print(i)

# ! practise problems
# ? print the even mumber between 20 to 40

# for i in range(20,41,2):
#     if i %2==0:
#       print(i)

# ---> while loop
# while  is used when we do not know the number of times the loop have to run
# to iterate the non iterable element while loop is used

# initialisation
# while condition:
#       statement
#       incre or decre

# Eg:1
# to iterate number from 1 to 10
# i=0
# while i<11:
#     print(i)
#      i=i+1 # or +=1


# For loop practise
# write a program to display sum of odd numbers and even numbers
# that fail b/w 12 and 37 (including both numbers)

# Eg:2
# 10,1

# i = 10
# while i>0:
#     print(i)
#     i-=1

# ! ---> 1
'''
# Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
'''







