# Example 1  :  ways of creating string varialbes
# A = 'aaa'
# B = "bbb"
# C = str("aaaaaaaaaaaa")
# D = str("bbbbbbbbbbbb")
#
# # Emplty string
# X = "0000"
# Y = '111'
# Z = str(111)
# print(A)
# print(B)
# print(C)
# print(D)
# print(X)
# print(Y)
# print(Z)
#String is immutable...can be updated
# str1 = str('Hari Om')
# str2 = str("Jay sree ram")
# str3 = str(1111111111111111)
# str1 = str1 + "Hara Hara Maha Dev" + '2223333'
# print(str1 + "    ", str2 + "   ", str3)
# print(len(str1))
# print(id(str1))
#Ex3.
# strA = 'xxxxxx'
# print(strA + "  ", 'yyyyy' + "   ", "zzzz")
# print(strA + strA + strA)
# print(strA *2)
#Ex4. Slicing
# StrB = "Welcome to my class"
# print(StrB[1:4])
# print(StrB[2:])
# print(StrB[:2])
# print(StrB[:])
#
# #Example5 : ord() and chr()
# print(ord ('A'))
# print(ord ('a'))
# print(ord ('B'))
# print(ord ('b'))
# print (chr(65))
from typing_extensions import reveal_type

#Example6:   max()  min() len()
# print(max('i am going to hyd'))
# print(min('i am going to hyd'))
# print(len("Welcome to my class"))

#Example 7: in ,  not in operators  - returns true/false
# StrB = "Welcome to my class"
# print("my" in StrB)
# print("my" not in StrB)

#Example8: String comparison
# A = 'aaaaaaaaa'
# B = 'aaaaaaaa'
# if A == B:
#     print("A is equal to B")
# else:
#     print("A is not equal to B")
#EX................... Same can be written as below
# A = 'aaaaaaaa'
# B = 'aaaaaaaa'
# if len(A) == len(B):
#     print("A is equal to B")
# else:
#     print("A is not equal to B")

#Example9: String comparision
# print("aaaa" == "aaa") #False
# print("free" != "freedom") #True
# print("111" == 111)
# print("111" == '111')
# print("111" != 111)

#Ex10. Testing the string
strc = "welcome to python"
# print(strc.isalnum()) #False
# print("Welcome".isalpha()) #True
# print("2012".isdigit()) #True
# print("first Number".isidentifier())#False
print(strc.lower())
print(strc.upper())
print(strc.title())

#Example11 : Searching for Substrings
# s = "welcome to python"
# print(s.endswith("on")) #True
# print(s.startswith("good")) #False
# print(s.count("t"))
#Ex12 Reverse a string

s = "welcome to python"
rev_str =""
for i in s:
    rev_str += i
print("rev str is:",rev_str)

















