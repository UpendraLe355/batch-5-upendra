
# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

# assignment
# Q---> 1

# s1 = "upendra"
# fst = s1[0].upper()
# lst = s1[-1].upper()
# print(fst+s1[1:len(s1)-1]+lst)

# print(s1.replace('u','U'))
# print(s1.replace('a','A'))

# Q --> 2

# n = 128
# temp = n
# f1 = 0
# while n!=0:
#     rem = n%10
#     check= temp % rem
#     if check!=0:
#         f1 = 1
#     n= n//10

# if f1==0:
#     print('yes')
# else:
#     print('no')

# Q --> 3

# l1 = [8,9,0,7]
# l2 = [7,6,5,4]
# print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])

# l3=[]
# for i in range(len(l1)):
#     ans = l1[i]+l2[i]
#     l3.append(ans)
# print(l3)

# ---> set

# Charctristics of set
# 1. set can be created using{}
# 2. The lelements inside set are not indexed
# 3. Does not allow duplicate values
# 4. It unordered
# 5. Heterogenous --> accept only unmutable datatypes
# 6. Mutable or chengable

# Eg:1
# s1 = {9,9,89,7.76,8+7j, (8,7,5),"truck",'e'}
# print(s1)

# Eg:2
# s2 = {5,8,98, [9,0]}
# print(s2)  ==> error

# Eg:3
# min(),max(), len()
# Eg:4
# To add element inside the set

# s1 = {8,78,67,'u'}
# add()
# s1.add(55)
# print(s1)

# update()
# s1.update([9,3])
# print(s1)

# to delete element inside set
# s1 = {8,78,67,'u'}

# pop() -->to delete one element randomely
# s1.pop()
# print(s1)

# remove()
# s1.remove(78)
# print(s1)

# discard()
# s1.discard(67)
# print(s1)

# clear()
# l1 = []
# print(type(l1)) --> datatype is dict

# s1 = set() # to create empty set
# print(type(s1))

# s1 = {8,9,0}
# s1.clear()
# print(s1)

# del s1
# print(s1)

# join the sets
# s1 = {9,0,8}
# s2 = {9.90,"card",'t',55}
# union() --> To combine 2 sets
# s3 = s1.union(s2)
# print(s3)

# intersection() --> To get commeon elements inside set
# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.intersection(s2))

# difference()
# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))

# isdisjoit(),issubset(),issuperset()
# s1 = {8,9,0}
# s2 = {6,7,5,8,9,0}

# print(s1.issubset(s2))
# print(s2.issuperset(s1))

# s1 = {1,2,3,4,5}
# s2 = {3,2,7,8,9}
# for i in s1:
#     if i in s2:
#         str1 = " Its joint set"
# print(str1)


#  ----> dictionary 

# Eg:1
# d1 = {1:100, 'a':200,4.5:"hello"}
# print(d1)
# print(len(d1))

# char of dictionary

# 1. have to be surrounded by {}
# 2. It have to be in the from of key, value pair
# 3. It is mutable
# 4. duplicate keys are not allowed, duplicate values are allowed
# 5. It is unindexed
# 6. It is ordered

# d1 = {1:100, 2:200, 3:300, 4:400}
# to access elements in dictionary
# print(d1)
# or
# to access the values,have to use key
# print(d1[1])

# some common functions
# len(), min(), max()

# print(min(d1))
# print(max(d1))

# --> to find min, max based on values
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(min(d1.vaalue()))
# print(max(d1.vaalue()))


# --> dictionary based functions
# To add element (key and value pair) in dict
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[5] = 500
# print(d1)

# --> TO replace a value in dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# d1[2]="moyo moye"
# print(d1)

# delete element from dictionary
# d1 = {1:100, 2:200, 3:300, 4:400}
# popitem() --> to delete last key value pair in dict
# d1.popitem()
# print(d1)

# pop()
# d1.pop(2) # --> 2 is the key in dict
# print(d1)

# join 2 dict
# update()
# d1 = {1:100, 2:200, 3:300, 4:400}
# d2 = {'a':'akka','b':'anna','k':'sdgfjfh'}
# d1.update(d2)
# print(d1)

# get()
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1[3])
# print(d1.get(3))

# to print all the keys in dict
# d1 = {1:100, 2:200, 3:300, 4:400}
# print(d1.keys())
# print(type(d1.keys()))

# to print all the values
# print(d1.values())

# Iterating dictionary
# for i in d1: --> to iterate keys alone
#     print(i)

# for i in d1.values(): -->to iterate values alone
#     print(i)

# to get both key and values
# for key, val in d1.item():
#     print(key,val)


#  Problem:1

# n= int(input("Enter num of time :"))
# integer=[]
# float_value=[]
# string=[]

# for val in range(n):
#     value=eval(input("Enter the values:"))
#     if type(value)==int:
#         integer.append(value)
#      elif type(value)== float:#
#         float_value.append(value)
#     elif type(value) == str:
#         string.append(value)
#     else:
#         print("pls proide data in int, float, sting")
# print(intger)
# print(float_value)
# print(string)
        
# problem:2

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))

# set3 = set()
# for val in set1:
#     if val not in set2:
#         set3.add(val)
# for val in set2:
#     if val not in set1:
#         set3.add(val)
# print(set3)
    
# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

# l1 = [1,2,3,4]
# l2 = ['a','b','c','d']

# d1= {}
# d1[l1[0]] =l2[0]
# print(d1)

# d1= {}
# for val in range(len(l1)):
#      d1[l1[val]] =l2[val]
# print(d1)
   





# mech_name =["name1","name2","name3"]
# mech_age = [23,24,25]
# mech_mark = [78,546,97]













