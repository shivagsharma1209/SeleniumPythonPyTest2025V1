#Example1:  overloadind 1(polymorphism)...Same function name, different behavior.
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello" +name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayhello("Shiva Prasad")
# h.sayhello()

#Ex Method overriding
# class Shape:
#     def draw(self):
#         print("Drawing shape")
#
# class Circle(Shape):
#     def draw(self):
#         print("Drawing circle")
#
# c = Circle()
# c.draw()
# c1=Shape()
# c1.draw()

#Example12: overloading .. Python does not support overloading directly, but can be simulated:

# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# calobj=Calculation()
# calobj.add() # 0
# calobj.add(10,20) # 30
# calobj.add(100,200,300) #600

#Example.............
class Calculator:
    def add(self, a, b, c=None):
        if c:
            return a + b + c
        return a + b

obj = Calculator()
# print(obj.add(2, 3))
print(obj.add(2, 3, 5))

