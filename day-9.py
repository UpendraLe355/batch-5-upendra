#2.) Find the uncommon words from 2 strings
# s1 = "Hello how are you"
# s2 = "Hello how is"

# s1 = "Hello how are you"
# s2 = "Hello how is"

# s1 = s1.split(" ")
# s2 = s2.split(" ")

# for val in s1:
#     if val not in s2:
#         print(val)
# for val in s2:
#     if val not in s1:
#         print(val)

# ---> Write a code print the 8th fibanochi number
#---> 0,1,1,2,3,5,8

# num = 8
# n1 = 0
# n2 = 1

# for val in range(num):
#     ans = n1+n2
#     n1 = n2
#     n2 = ans
# print(ans)

# ---> constructors

# Eg:2

# ---->unparametarised constructor
# class profile:
#     def init(self):
#         print("hello world")
#        
# obj=profile()
 #obj.init()


# Eg: 3
# parameterised constructor

# class profile:
#     def __init__(self, id, name, age):
#         print(id, name, age)

#  obj = profile(93,"upi", 22)

# EG:4
# class c1:
#       email = "sdtertre44@gmail.com"
      
#       def m1(self):
#           name = "upi"
#           place = "pkd"
#           print(name, place)
#           print(self.email)
 
# object = c1()
# object.m1()

# Eg:5
# class c1:
#     def m1(self):
#         name = "upi"
#         age = 22
#         return name, age

#     def display(self):
#         print(self.m1())
# object = c1()
# object.display()

# Eg:6
# to use the variable inside the constructor in anothe method
# class class1:
# email = "cfsdf@gmail.com"   # static variable
#     def __init__(self):
#         self.name = "upi"     # instance variable
#         self.email = "cfsdf@gmail.com"
#        # return name,email # error 
#     def display(self):        # instance method
#         print(self.name, self.email)

# c1 = class1()
# c1.display()
'''
# -----> inheritance
# the process of utilising the method and attributes of parent class
# through the object of child class it is called as inheritance

# 5 types of inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance
'''

# single inheritance
# It has only one parent class and only one child class

# Eg:1
# class parant:
#     def m1(self):
#         print("Iam parant class")

# class child(parant):
#     def m2(self):
#         print("Iam child class")

# obj = child()
# obj.m1()

# Eg:2
# class c1:
#     def __init__(self):
#         print("Iam constructor from parant class")

# class child1(c1):
#     pass

# obj = child1()
        
# Eg;3
# class parant:
#     name = "upi# "

# class child(parant):
#     name = "kuttal"

#     def display(self):
#         print(self.name)

# d = child()
# d.display()

# Multilevel inheritance

# Eg:1
# class voice:
#     def sound(self):
#         print("All the animals have their own voices")
        
# class dog(voice):
#     def dog_voice(self):
#         print("bark")
        
# class cat(dog):
#     def cat_voice(self):
#         print("Meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")

# all = parrot()
# all.dog_voice() # ==> bark
# all.cat_voice() # ==> Meow
# all.sound()      # ==> All the animals have their own voices
# all.parrot_voice() # ==> speak
'''
# Eg:2
class honda_city:
    def honda_city_engine_speces(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)

    def honda_city_body_speces (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)

class amaze(honda_city):
    def amaze_engine_speces (self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    
    def amaze_body_speces (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)

class civic(amaze):
    def civic_body_speces (self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)

class honda(civic):
    pass

honda = honda()
honda.honda_city_engine_speces(1500, 230, 2979, "petrol", 4)
honda.civic_body_speces("white", 2000, 5.5, 8, "Hatchback")

# ===> 500 230 2979 petrol 4
      white 2000 5.5 8 Hatchback
'''


#---> Multiple Inheritance
# --> it has multiple parent and 1 child

#class while_pertol:
#    def function_w(self):
#        print("used to Airplans")
        
#class Organic_petrol:
#    def function_o(self):
#        print("used for Bike, cars")
        
#class premium_petrol:
#    def function_p(self):
#        print("spots cars, bikes")
        
#class petrol(while_pertol, Organic_petrol, premium_petrol):
#    def defanition(self):
#        print("Petrols types")

#p = petrol()
#p.defanition()
#p.function o()


# --.MRO --> mmethod resolution order
# eg:2
#class addition:
#     def add(self, a, b):
#         print(a+b)

#class subract:
#    def sub(self, a, b):
#        print(a-b)
        
#class multiply:
#    def mul(self, a, b):
#        print(a*b)
#        
#class division (addition, subract, multiply):
#    def div(self, a, b):
#        print(a/b)

#calc = division()
#calc.add(3, 4)
#calc.mul(5, 2)


#------> Heirarical inheritance
#? The one parent classe will asct as parent for all the child classes
#class catagory:
#    def weight(self, weight):
#        print(weight)

#    def display(self, color, taste):
 #       print(color, taste)
        
#class Tomato (catagory):
#    def tomato_specs (self):
#        color="black"
#        taste="neutral taste"
#        self.display(color, taste)
        
#class carrot(catagory):
#    def carrot_specs (self):
#        color="green"
#        taste="sweet"
#        self.display(color, taste)
        
#c= carrot()
#c.carrot_specs()
#c.weight("30gms")

#t = Tomato()
#t.tomato_specs()
#t.weight("20gms")

# ----> Hybrid inheritance
# the combination of 4 inheritance

# Eg:1
#class c1:
#    def m1(self):
#        print("class1")

#class c2(c1):
#    def m2(self):
#        print("class2")
    
#class c3(c2):
#    def m3(self):
#        print("class3")

#class c4(c2):
#    def m4(self):
#        print("class4")

#    def m3(self):
#        print("iam m3 from c4")

#class c5(c3):
#    def m5(self):
#        print("class5")

#class c6(c5,c3):
#    def m6(self):
#        print("class6")

#obj = c6()
#obj.m3()
    
# ------> polymorphism    
# ? poly many, morph --> form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be as plioymorphism

#* Ploymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# polymorphism in operators
# +
# print(8+8)
# print("k"+'j')
# print([1,2,3]+[5,6])

# *
# print(6*7)
# l1 = {1,2,3,4,5,6}
# print(l1)
# def f1(*args):
# l1 = [1,2,3,4]
# print(l1*3)

# ---> Ploymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading --> it is not possible in java
# 2.) Method overriding

# 1. Tasks







