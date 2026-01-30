#Ex1.
# print("Section one of pgm")
# print("Section two of pgm")
# try:
#     print('x')
# except:
#     print("Section six of pgm")
# print("Section seven of pgm")
# print("Section eight of pgm")

#Ex2.
# print("Starting of the pgm.........")
# print("pgm execution in progress....")
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print("Exception occured ...handled..")
# print("pgm completed......")

#Ex3.Multiple except blocks...........
# try:
#     num1,num2,num3=1,2,1
#     result = (num1+num2) / num3
#     print("Result is:", result)
# except ZeroDivisionError:
#     print(" Exception 'ZeroDivisionError'...occured....")
# except SyntaxError:
#     print("Exception handled....")
# else:
#     print("No Exceptions occured...")
# finally:
#     print("Continue the execution")

#Ex4. User defined exceptions...........
def enternumber(num):
    if num >1:
        raise ValueError ("Allowed only valid numbers")
    # if num / 0 :
    #     raise ZeroDivisionError ("Allowed only valid numbers")
    if num %2 == 0:
        print ("Number is Even...")
    if num % 2 == 1:
        print ("Number is Odd....")
print("Check for the number even / odd.........")
num = 4
try:
    num = enternumber(num)
except ZeroDivisionError:
    print("ZeroDivisionError occured....Exception handled....")
except SyntaxError:
    print("SyntaxError occured....Exception handled....")
except ValueError:
    print("ValueError occured....Exception handled....")
else:
    print("No Exceptions occured....")
finally:
    print("End of the pgm.......")














