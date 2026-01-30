# Class is a logical entity, does not occuoy any space in the memory.
#Class contains methods with some action, methods will be called by objects for storing results after performing actions
#Class --->Methods(functions within the class)--->Objects to call methods
from email.contentmanager import raw_data_manager


#Ex1. Create a class, method and object
# class Myclass:  #Name of the class
#     def myfunc(self): # Method myfunc
#         print("hello")
#     def display(self):  #Method display
#         print("how are you doing?")
# res1 = Myclass()    #res1 is object to store the result
# res1.myfunc()
# res1.display()

#Ex2.
# class MyClass:
#     def myfun(self,name):
#         print(name)
#     def display(self,age):
#         print(age)
# r1=MyClass()
# r1.myfun("Shiva")
# r1.display(30)
# r2=MyClass()
# r2.myfun('Rama')
# r2.display(40)

#Ex3. Instance & Static Methods
# class MyClass:
#     def m1(self,name):
#         print("this is instance method...")
#         print(name)
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
# mc=MyClass()
# mc.m1('rama')
# mc.m2(100,200) #100 200
# MyClass.m2(1000,2000)

#Ex4.Class with multiple methods....one object can invoke all methods

# class Myclass2:
#     def add(self,a,b):
#         self.a,self.b=10,20
#     print("Addition is:", self.a + self.b)
#     def sub(self):
#         a,b=10,20
#     print("Difference is:", a - b)
#     def mul(self):
#         a,b=10,20
#     print("product is:", a * b)
#     def div(self):
#         a,b=10,20
#     print("Division is:", a / b)
#
# cal=Myclass2()
# cal.add()
# cal.sub()
# cal.div()
# cal.mul()

# class TestClass:
#
#     def add(self, num1,num2):
#         self.add1=num1+num2
#         print("Sum of numbers=",self.add1)
#
#     def subtract(self, num1,num2):
#         self.subtract1=num1-num2
#         print("Sum of numbers=",self.subtract1)
#
#     def multiply(self, num1,num2):
#         self.multiply1=num1*num2
#         print("Sum of numbers=",self.multiply1)
#
#     def divide(self, num1,num2):
#         self.divide1=num1/num2
#         print("Sum of numbers=",self.divide1)
#
#     def display(self):
#         print("Sum of all calculations =",self.add1 + self.subtract1 + self.multiply1 + self.divide1)
#
# caltest=TestClass()
#
# caltest.add(10,20)
# caltest.subtract(10,20)
# caltest.multiply(10,20)
# caltest.divide(10,20)
# caltest.display()


#Ex5. Accessing Class variables.............
# class Myclass:
#     a,b=10,20   #class variables
#     def calc(self):
#         print(self.a + self.b)
#         print(self.a - self.b)
#         print(self.a * self.b)
#         print(self.a / self.b)
#         print(self.a // self.b)
#         print(self.a % self.b)
#         print(self.a ** self.b)
# Res=Myclass()
# Res.calc()
#---------Above example can also written as below.........
# class Myclass1:
#     a,b=10,20
#     def add(self):
#         print(self.a + self.b)
#     def sub(self):
#         print(self.a - self.b)
#     def mul(self):
#         print(self.a * self.b)
#     def div(self):
#         print(self.a / self.b)
#     def exp(self):
#         print(self.a ** self.b)
# Res1=Myclass1()
# Res1.add()
# Res1.sub()
# Res1.mul()
# Res1.div()
# Res1.exp()

#Ex6. Accessing Global variables...................
# i,j=120,220 #Global variables
# class Myclass3:
#     a,b=10,20   #class variables
#     def add(self, x,y):
#         print(self.a + self.b)
#         print(x + y)    #Local variables
#         print(i + j)    # Global variables
# Res2=Myclass3()
# Res2.add(11,22)

#Ex7 Global, class and local variables
# a,b=10,20
# class Myclass4:
#     a,b=30,40
#     def calc(self,a,b):
#         print(self.a + self.b)
#         print(globals()['a'] + globals()['b'])
#         print(a + b)
# Res3=Myclass4()
# Res3.calc(110,220)

#Ex8, Class with multple objects
# class Myclass5:
#     def calc(self):
#         a,b=10,20
#         print (a + b)
#
# Obj1=Myclass5()
# Obj2=Myclass5()
# Obj3=Myclass5()
# Obj4=Myclass5()
# Obj1.calc()
# Obj2.calc()
# Obj3.calc()
# Obj4.calc()

















