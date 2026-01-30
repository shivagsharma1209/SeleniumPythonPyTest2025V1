#Conditional statements - if, if---else, elif
from asyncio import Event

from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

#Ex1. To return voter eligibility
# age = 18
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

#Ex2.
# if False:
#     print("You are True")
# else:
#     print("You are False")

#Ex3.
# if 0:
#     print("True")
# else:
#     print("False")

#Ex4. Find the given number is even /odd
# num =10
# if num % 2 == 1:
#     print("Num is even")
# else:
#     print("Num is odd")

#Ex5. If--else in single line above example can be written as below
# num = 7
# print("Even Number") if num%2==0 else print("Odd Number")

#Ex6. Multiple lines in single stmt
# a = 9
# {print('hi'), print('there')} if a >= 10 else print('there')

#Ex6. Multiple conditions ------elif
# weeknum =3
# if weeknum  == 1:
#     print("Monday")
# elif weeknum  == 2:
#     print("Tuesday")
# else:
#     print("Invalid week number ")

#Ex7. Check the number is postive or negative
# num = int(input("Enter a number: "))
# if num >=0:
#     print("NUmber is positive")
# else:
#     print("Number is negative")

#Ex8. Find largest of 3 numbers
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if num1 >= num2 and num1 >= num3:
    print(f" largest of three numbers is {num1} ")
if num2>=num1 and num2>=num3:
    print(f" largest of three numbers is {num2} ")
else :
    print(f" largest of three numbers is {num3} ")





