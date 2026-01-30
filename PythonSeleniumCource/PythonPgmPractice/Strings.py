from pygments.lexer import words
from selenium.webdriver.common.devtools.v140.storage import SignedInt64AsBase10
# S="Hello Woorld"
# print(S)
#
# U = S.upper()
# print(U)
# L=S.lower()
# print(L)
#
# num1=int(input("Enter num1.."))
# num2=int(input("Enter num2.."))
# print("sum =",(num1 + num2))
# print("product =", (num1 * num2))
# print("quotient =", (num1 / num2))
# print("remainder =", (num1 % num2))
# print("Difference =", (num1 - num2))
#------------------------------------
# num = int(input("Enter a number: "))
# if num>0:
#     print("number is positive")
# else:
#     print("number is negative")
# ---------------------------------
# num= int(input("Enter a number: "))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")
# Largest of 3 numbers
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter another number: "))

# print("max of given numbers is..", max(a,b,c))

# import sys
# # print(sys.version)
#
# x='aaaaaaaaaaaaa'
# y=x
# print(sys.getrefcount(x))
# del x
# print(sys.getrefcount(x))

# a = "this is a sample string with many characters"
# print(len(set(a)))
# print(a.upper())
# print(a.count("i"))
# print(a.find("a"))
# print(a)
#
# from collections import Counter
#
# def anagrams(a: str, b: str) -> bool:
#     # Normalize: remove spaces and lowercase (customize as needed)
#     na = ''.join(a.split()).lower()
#     nb = ''.join(b.split()).lower()
#     return Counter(na) == Counter(nb)
# print(anagrams("listen", "silent"))

#Palindrome
# S="Welcome"
# if S==S[::-1]:
#     print("Sting is polyndrome", S)
# else:
#     print("Sting is not polyndrome", S)

#Count vowels in string
# str = "this is a sample string with many characters"
# vowels=0
# for i in str:
#     if i in "aeiou":
#         vowels+=1
# print(vowels)

#Number of words in a given string
str="Python Selenium training sessions new batch"
words=str.split()
print("Total words=", len(words))













