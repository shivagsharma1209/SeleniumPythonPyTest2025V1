#Ex1. calling parent class method using child class(super())..........
# class A:
#     def m1(self):
#         print("This is method m1 from class A")
# class B(A):
#     def m1(self):
#         print("This is method m1 from class B")
#         super().m1()
# bobj = B()
# bobj.m1()

#Ex2.
class A:
    a,b = 10,20
class B(A):
    i,j = 100,200
    def m(self,x,y):
        print(x + y)  # 3000 ===> Local variables
        print(self.i + self.j)  #300 ===>=Class variables
        print(self.a + self.b)  # 30====>clas variables
bobj = B()
bobj.m(1000,2000)

#Ex3: overriding variables
class Parent:
    name="Shiva"

class Child(Parent):
    name="Prasad"   # overriding the variable value
    def test(self):
        print(super().name)

cobj=Child()
print(cobj.name) #"Prasad"
cobj.test() #Shiva

#Ex4: Overriding methods
# class RBI_Bank:
#     def rateOfInterest(self):
#         return 0
#
# class HDFC_Bank(RBI_Bank):
#     def rateOfInterest(self):
#         return 10
#
# class AXIS_Bank(RBI_Bank):
#     def rateOfInterest(self):
#         return 12
#
# objhdfc=HDFC_Bank()
# print(objhdfc.rateOfInterest()) # 10
#
# objaxis=AXIS_Bank()
# print(objaxis.rateOfInterest()) #12












