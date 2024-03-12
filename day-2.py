# a=7, 8
# print(a)
# print(type(a))--> # ==> (7,8)
                    # ==> <class 'tuple'>

# a, b, c = 9, 8, 7, 8
# print(a, b, c)  # ==> a, b, c = 9, 8, 7, 8
                  # ValueError: too many values to unpack (expected 3)

# a, b=c=7, 8
# print(a)
# print(c) # ==>  7
           #     (7, 8)
# a=b, c = 4, 2
# print(a, b, c) # ==> (4, 2) 4 2

# --> Swapping of variables
# eg:1
# a = 7
# b = 5
# i=a
# a=b
# b=i
# print(a, b) # ==> 5 7

# eg:2
# a=a+b
# a=a-b
# print(a, b) #==> 7 5

# eg:3
# a, b=b, a # only in python
# print(a,b) #==> 5 7

# eg:4
# a=a*b #a=35
# b=a/b #b=35/7 =5.0
# a=a/b #a=35/5 =7.0
# print(int(a),int(b)) #==> 7 5

# id() --> used to find the memory address of the variable
# a =7
# b =8
# print(id(a))
# print(id(b))#--># ==> 2023701676464
                  # ==> 2023701676496
#---> Keywords
#---> keywords are reserved words which provides speciale mening to compeller or interpector

# import keywords
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(type(keyword.kwlist))

# ---> to check if the string is keyword or not
# print(keyword.is keyword("upi")) ==> false

# if = 8
# print(if) ==> error coz is a keyword

# !---> literals
# Literal is the constant value assigned to a variable
# A variable is considers to be constant when if is defines in caps

# a=78 --> a is variable
# A=78 --> A is constant

# hash() --> it creates a hash value for constant datatype
# provides error for non constant datatypes

# n1=89.8
# print(hash(n1)) # ==> 1844674407370948697

# n1=89+7j
# print(hash(n1)) # ==> 7000110

# f1 = [7, 8, 9]
# print(hash(f1)) # ==> TypeError: unhashable type: 'list'

# a = 9
# b = 9
# print(id(a))
# print(id(b)) # ==> 1950823940592 # it gets same random value
               #     1950823940592

#! ---> Operators
# ? Operators are symbols which is used to perform various operations
# ? between 2 or more operations

# Arithmatic
# Assignment
# Logical
# Relational or comparsion
# Bitwise
# Identity
# membership

# todo  ---> Arithmatic --> +, -, *, /, %, //, **
#eg:1
# a=8
# b=6
# c=9
# print(a+b+c)# ==> 23

# input() --> used to get the runtime input
# eval() --> used to get the runtime value of all datatypes

# n1 = eval(input("Enter the value: "))
# print(type(n1))

# a=4
# b=2
# print(a/b) # is used to get the quotient value
# print(a%b)# ==> 2.0 # is used to get the remainder value
            #     0
# ! // --> floor devision operator

# a=783784
# b=18
# print(a/b)
# print(a//b) # ==> 43543.555555555555
            #     43543 --> the output will be in integer will be
                  #         based on floor value

#! **--> used for power of a number
# print(2**4) # ==> 16

#! Assignment --> +=, -=, /=, *=, //=, **=, &=, |=

# a=8
# a+=2
# print(a) # ==> 10

# a=30
# a-=5
# print(a) #==> 25

# a=50
# a/=5
# print(a) #==> 10.0

#! Comparision --> ==, >, <, !=, <=, >=

# a=8
# b=7
# print(a>b) # True

# a=9
# b=5
# print(a==b) # false

#! Bitwise operator --> &, |, ^, ~, <<, >>

# a=7
# b=6
# print(a&b) # ==> 6

# 2^4 2^3 2^2 2^1 2^0
#   8   4   2   1

#   0   1   1   1  ---> 7
#   0   1   0   0 ----> 4 &
#  ----------------------
#   0   1   0   0 ----> 6

# ~ --->
# a=5
# print(~a) # ==> -6 next -ve value

# <<,>>
# print(5<<3) # ==> 40
# print(5>>1) # ==> 2

#! Logical operator ---> used to compare the expression
# and, or, not
# a=6
# print(a>3 and a<10) ==> True
# print(a>7 or a<30)
# print(not(a>8 and a<10))

#! Identity operator
# is, is not
# ? it is used to compare the memory location that 
# a=8
# b=8
# print(a is b)# ==>True
# print(a==b) # ==> True

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b) # ==> False

#! Membership operator
# in, not in

# l1 = [7,8,9,0,6,5]
# num=55
# print(num in l1) # ==> False
# print(num not in l1) # ==> True

# num =678
# print(8 in num) # ==> error

#! Conditional statement
# if,elif, else

# if condition:
#   statement
#   statement
#   sratement
    
# Eg:1
# a=6
# if a:
#    print("hello")

# Eg:2
# a=6
# if a>3:
#    print("upi")
# else:
#     print("no")# ==> upi

# Eg:3
# if 7>8:
#     print("hello")
# else:    
#     print("no") # ==> no

# Eg:4
# a = 0
# a = None
# a=False
# a=""
# if a:
#     print("yes")
# else:
#     print("no") # ==> no

# sum:1
# a number is even or odd

# n = int(input("enter the number: "))
# if n %2==0:
#    print(n, "is even")
# else:
#    print(n, "is odd")

# sum:2

# name, age, nationality
# 18 above, indian

# name=str(input("enter name"))
# age=int(input("enter age"))
# nationality=str(input("enter nationality"))

# if age  >18 and nationality=="indian":
#    print("eligible for vote")
# else:
#    print("not eligible")













