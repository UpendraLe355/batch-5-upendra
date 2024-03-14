
#  ---> while loop
# ---> break using ehile loop

# Eg:1
# 1). iterate from 20 to 30 and break the loop in 27

# i = 20
# while i<32:
#     if i ==27:
#        break
#     print(i)
#     i+=1

# 2). 

# i = 20
# while i<31:
#       print(i)
#        i+=1
#       if i==27:
#           break
     
# 3).

# i = 20
# while i<31:
#       print(i)
#       if i==27:
#           break
#        i+=1

# 4).

# i=20
# while i<31:
#     if i==27:
#         print(i)
#         break
#     i+=1      # ===>27


# ---> continue
# Eg:1

# i = 20
# while i<31:
#     if i==27:
#         continue
#     print(i)
#     i=i+1     # ===> 20 to 26 print

# i = 20
# while i<31:
#     i=i+1
#     if i==27:
#         continue
#     print(i)   # ===> print 20 to 30 and skip 27

# ! Eg:5

# while to iterate from 12 to 22
# find the sum of all numbers

# i = 12
# sum=0
# while i<23:
#     sum=sum+i
#     print(sum)
#     i+=1      # ===> 12,25,39,54,70,87,105,124,144,165,187
    

# i = 12
# sum=0
# while i<23:
#     sum=sum+i
#     i=i+1
# print(sum)      # ===> 187

#! Eg:6

# find the average of value from 20 to25

# i = 20
# sum=0
# count = 0
# while i<26:
#    sum= sum+i
#    count+=1
#    i=i+1
# print(sum/count)   # ===>22.5

# ----> Nested for loop

# Eg:1
# for i in range(1,3+1):
#     for j in range(1,4+1):
#        print(i,j)  # ===>  1 1
#                            1 2
#                            1 3
#                            1 4
#                            2 1
#                            2 2
#                            2 3
#                            2 4
#                            3 1
#                            3 2
#                            3 3
#                            3 4
 
# Eg:2

# * * * *
# * * * *
# * * * *
# * * * *
    
# for row in range(4):
#     for col in range(4):
#         print("*",end=" ")
#    print()
# Eg:3

# rows = int(input("enter the rows:"))
# cols = int(input("enter the cols:"))

# for row in range(rows):
#     for col in range(cols):
#         print("*",end=" ")
#    print()

# for row in range(4):
#      for col in range(4):
#          print(row,end=" ")
#     print()

# ==>   0 0 0 0 
#       1 1 1 1 
#       2 2 2 2 
#       3 3 3 3       

# sum=0
# for row in range(5):
#      for col in range(5):
#          sum=sum+1
#          print(sum,end=" ")
#      print()  
# ==>   1 2 3 4 5 
#       11 12 13 14 15 
#       16 17 18 19 20 
#       21 22 23 24 25

# to print stars in right angle traingle

# for row in range(0,9):
#     for col in range(0,row+1):
#         print("*", end=" ")
#     print()

# for row in range(6,0,-1):
#     for col in range(0,row):
#         print("*", end=" ")
#     print()

# for row in range(5):
#     for col in range(5):
#         if col==0 or col==5-1 or row==0 or row==5-1:
#             print("*", end=" ")
#        else:
#           print(" ",end=" ")
#     print()
#===> * * * * * 
#     *       * 
#     *       * 
#     *       * 
#     * * * * * 
 
# for row in range(0,5):
#     for col in range(0,6):
#         if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4))):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
        
# for row in range(0,6):
#     for col in range(0,6):
#         if ((((row==0 and col==0) or (row==1 and col==1) or (row==1 and col==2) or (row==1 and col==3) or (row==1 and col==4)or (row==1 and col<=5)))):
#         else:
#              print("*",end=" ")
#     print()  ==> not run

#  ---> Datatypes
# primary

# Number --> int,flot,complex
# string
#Boolean
#none

# collection
# List
# tuple
# set
# dictionary

# ---> List []

# 1. if the collection of elements are sorounded by square bracket to be list

# Eg:1

# l1 = [4,7,9,59.44,'upi',3=4hj]

# Charactristics of list
# 1. list have to be sorounded by []
# 2. It is mutable (the elements in the lidt are changble
# 3. Every elements inside list is indexed
# 4. The elements inside list will be ordered format
# 5. It can hold duplicate values
# 6. Its heterogenous

# To acces the elements in list

# lst1 = [1,4,2,5,67.86,'r','u']
# print(lst1)

# ---> Indexing
# the collection datatypes like list, tuple, string, the elements will be allow
# with predefines unique value called index value

# we have 2 types of indexing
# positive indexing --> starts with 0 fromleft hand side
# Negative indexing --> starts with -1from right hand side

# --. positive indexing

# print(lst1[0]) ==> 1
# print(lst1[4]) ==> 67.86

# ---. Negative indexing

# print(lst1[-1]) ==> u
# print(lst1[-4]) ==> 5

# ---> slicing

# lst1 = [1,4,2,5,67.86,'r','u']
# list[start_index:end_index:step]

# print(lst1[0:4])   ===> [1, 4, 2, 5]
# print(lst1[6:8])   ===> ['u']
# print(lst1[3:6])   ===> [5, 67.86, 'r']
# print(lst1[:5])    ===> [1, 4, 2, 5, 67.86]
# print(lst1[3:])    ===> [5, 67.86, 'r', 'u']
# print(lst1[:])     ===> [1, 4, 2, 5, 67.86, 'r', 'u']

# print(lst1[0:7:1]) ===> [1, 4, 2, 5, 67.86, 'r', 'u']
# print(lst1[0:7:2]) ===> [1, 2, 67.86, 'u']

# lst1 = [1,4,2,5,67.86,'r','u']

# print(lst1[-4:-1])   ==> [5, 67.86, 'r']
# print(lst1[-1:-4])   ==> []
# print(lst1[-7:-1])   ==> [1, 4, 2, 5, 67.86, 'r']
# print(lst1[-7:-1:2]) ==> [1, 2, 67.86]

# to insert to add element inside list

# l1 = [9,8,0,6]
# l1.append("car")
# print(l1) ==> [9, 8, 0, 6, 'car']










