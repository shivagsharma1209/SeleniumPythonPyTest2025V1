#Function is set of statements to perform a task
# Builtin functions in Python
#User defined functions

#Ex1. Declare  a function using def
# def fun1():
#     print("Function1")
# fun1()
# #Ex2. Passing parms to the function
# def add(x,y):
#     print(x + y)
# add(10,20)
#
# #Ex3. Access the function by passing parms
# def myfunc(name):
#     print("My name is:", name)
# myfunc('Shiva')

#Ex4. Define and usage of Local and Global variables
# global_var = 100
# def fun1():
#     local_var = 10
#     print(local_var)
#     print(global_var)
# fun1()

#Ex Global variable
# xy=100
# def fun2():
#     xy=200
#     print(xy)   #200 -- Takes local variable inside the function
# fun2()

#Ex.. Local and Global
# ab=200
# def func3():
#     global ab
#     print(ab)   #200
# func3()

#Ex...
x = 100
def fun3():
    global x
    x = 200
    print(x)    #200 .. local will take priority inside the function, so x= 200
fun3()
print(x)    # 200-- as the global value of x got changed inside the function

#Ex.. Declare global variable in side the function
def fun4():
    global x
    x = 300
    print(x)
fun4()
print(x)








