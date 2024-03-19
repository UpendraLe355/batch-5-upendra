
# Eg:3
# def profile(name, age, place):
#     txt ="my name is {}.iam{}years old. iam from{}."
#     print(txt.format(name, age, place))
# profile("upi", 22, "pkd")

# Eg:4
# function with return statement

#! return
#1.) A variable declared inside the function can be accessed outside the function
# using return
# 2.) return does not prrint anything
#3.) we cannot write any code below return statement

# def f1():
#     z = 8
#     f1()
# print(z)  ===> error

# def f1(a, b):
#     c = a*b
#     return c
# obj = f1(6, 8)
# obj1 = f1(4,6)


# def gracemark(object):
#     print(object+4)
# gracemark(obj)   ===> 52
# gracemark(obj1)  ===> 28

# problem:1
# 123
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n, "palindrome")
#     else:
#         print("Not palinddrome")
# a = int(input("Enter the value: "))
# palindrome(a)
''' 
#? Based on the declaration of parameter and args
#? functions are divided into 5 catagories

# Positional args
# keyword args
# default args
# variable length args
# keyword variable length args
'''
# --> positional args
# Eg:1
# def profile(name, phone, mark):
#     txt = "my name is {}. my phone number is {}. I got{} marks."
#     print(txt.format(name, phone, mark))
# profile(7013621690, "upi",93)  # miss macih details

# --> Keyword args
# Eg:1
# To overcome the disadvantage of positioin args, we use keyword args
# It is the process of insdtalising the perameter with the args while calling the function
# def profile(name, phone, mark):
#     txt = "my name is {}. my phone number is {}. I got{} marks."
#     print(txt.format(name, phone, mark))
# profile(phone=7013621690, name="upi",mark=93)

# ==> my name is upi. my phone number is 7013621690. I got93 marks.

# --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt = "my name is {}. my phone number is {}. I got{} marks."
#     print(txt.format(name, phone, mark))
# profile(7013621690, name="upi",mark=93) ===> error
# profile("upi",mark=93,phone=7013621690)


# Default args
# The method of assigning the argument to the parameter while declaring the funcftion
# Eg:1

# def profile(name, phone, place="pkd"):
#     txt = "my name is {}. my phone number is {}. I am from {}."
#     if place=="pkd":
#         print("your eligible")
#     else:
#         print("not eligible")
#     print(txt.format(name, phone, place))

# profile("upi", 7013621690, "pkd")
    
# ===> my name is upi. my phone number is 7013621690. I am from pkd.

# Exception

# profile(name, place="pkd", phone):
#     txt = "my name is {}. my phone number is {}. I am from {}."
# if place=="pkd":
#     print("your eligible")
# else:
#     print("not eligible")
# file("upi", 7013621690)


# ---> variable length params
# to pass more then 1 arg to a parameter means we use variable length arg
# to convert normal parameter to variable length parm, add * to ther prefix of param

# Eg:1

# name = "kabali", 'akhanda', 'devara'
# def profile(*name):
#     for i in name:
#         print("my name is", i)
# profile("kabali", 'akhanda', 'devara')


# eg:2

# name = "kabali", 'akhanda', 'devara'
# def profile(age,*name):
#     for i in name:
#         print("my name is", i, "my age is",age)
# profile("kabali", 'akhanda', 'devara', 93)

# ---> keyword variable length args
# Eg:1

# def price(price_list):
#     print(price_list)

#price(shirt=10000, iphone=130000)

# d1 = {"a":100, "b":300, "c":500}
# d1 = dict(a=100, b=300,c =500)
# print(d1)


'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ===>
# 1.
# n = int(input("enter the number: "))
# d1 = {}
# for i in range(1, n+1):
#     d1[i] = i**2
# print(d1)

# 2.
# def dict1(n):
#     d1 = {}
#     for i in range(1,n+1):
#         d1[i] = i**2
#     print(d1)
# dict1(5)

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number
'''

# ---> object oriented programming
# The paradigms of objects oriented progarmming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# class is a blue print of an object
# l1 = [1,2,3,4,5,,6]

# Eg:1
# class c1:
#     name1 = "upi"
#     print(name1)

# Eg:2
# class person:
#     name = "upi"

# c = person()
# the procwss of creation of an object is csllled as instantiation
# print(c.name)

# Eg:3
# create of a method
# when the function is created with  a class is called as method

# method with out parameter
# class person:
#     def display(person):  # It is a method
#         print("Hello welcome to class")

# p = person()
# p.display()

# Eg:4
#  method with parameter

# class person:
#     def display(person, name, age):
#         print(name, age)
# p = person()
# p.display("upi", 22)

# Eg:5
# class person:
#     name3 = "upi"  # adttribute or static value

#     def display(person):
#         print(person.name3)

# p = person()
# p.display()


# class person1:
#     fname = "upi"
#     lname = "v"

#     def first_name(self):
#         print(self.fname)

#     def full_name(self):
#         print(self.fname+" "+self.lname)

# p = person1()
# p.first_name()
# p.full_name()

# Eg:6
# constructors --> __init__()
# This is a special method which has the ability to execute iotself without
# calling it manullay through the process of instantiation

# class profile:
#     def __init__(self):   # constructor method
#         print("xckjbsa")

# p = profile()# excution of constructor throught this process


























