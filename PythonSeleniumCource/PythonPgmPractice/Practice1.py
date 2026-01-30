#Datatypes
# a=10
# b=20
# # del a
# # del b
# print(a)
# print(b)
from itertools import product

from selenium.webdriver import ActionChains

from PythonSeleniumCource.PackA11.PackMod1 import subtract

#“Tuple Packing”
# A=10,20,30
# print(type(A))  #<class 'tuple'>

#‘Tuple Unpacking’.
# A=1,2,3,4
# a,b,c,d=A
# print(type(A))

#parallel assignment
# a=10
# b=20
# c=30
# a,b,c=c,b,a
# print("value of a is..", a)
# print("value of b is..", b)
# print("value of c is..", c)

# a=10
# b=a
# a=20
# print(b)
# print(a)

# i=10
# print(i)
# i=10.5
# print(i)
# i='test'
# print(i)

# #multiple assignments
# miles=1000
# name='shiva'
# print(miles)
# print(name)
# print(name,'',miles)

# a=b=c=1
# print(a,b) #111
# print(c,b) #1 1
# print(a,b,c)    #1 1 1

# x=y=z=1,2,'a'
# print(x,y,z)    #(1, 2, 'a') (1, 2, 'a') (1, 2, 'a')
# print(x)    #(1, 2, 'a')
# print(y)    #(1, 2, 'a')
# print(z)    #(1, 2, 'a')

# a=100
# b=200
# c=300
#
# add = a+b+c
# mul=a*b*c
# div=a//b//c
# mod=a%b
# sub= a-b-c
#
# print(add,mul,div,mod,sub)
# List=[1,2,3,4,5,6,11,22,30,1,2,44]
# # print(max(List(-2)))
# print(min(List))
#
# print(max(List))

#Max of 3 numbers
# a=10
# b=20
# c=3
#
# if a>=b and a>=c :
#     print(a)
# elif b>=a and b>=c:
#     print(b)
# else:
#     print(c)

#sum of numbers in a list
# A=[1,2,3,4]
# sum = sum(A)
# product=product(A)
#
# print("sum is ", sum)
# print("product is ", product)

#sum of numbers in a given number
# num = input("Enter number: ")
# total = sum(int(d) for d in num)
# print("Sum =", total)

#Factorial of a num
# num = int(input("Enter number: "))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print("factorial of number is..",fact)
# #sum of numbers of fact
# num = int(input("Enter number: "))
# fact=0
# for i in range(1,num+1):
#     fact+=i
# print("sum of factorial of number is..",fact)

#Multiplication table
# n = int(input("Enter number: "))
#
# for i in range(1, 11):
# print(n, "x", i, "=", n * i)

#Fibonaccci
n = int(input("How many terms? "))
a, b = 0, 1
for _ in range(n):
print(a, end=" ")
a, b = b, a + b




























