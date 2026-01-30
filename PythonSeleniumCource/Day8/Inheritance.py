#EX1. Single inheritance
# class A:
#     def m1(self):
#         print("Method m1 from calss A")
# class B(A):
#     def m2(self):
#         print("Method m2 from calss B")
# obj = B()
# obj.m1()
# obj.m2()

# Ex2.............................
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x + self.y)
#     def m2(self):
#         print(self.x - self.y)
#
# class B(A):
#     def m3(self):
#         print(self.x * self.y)
#     def m4(self):
#         print(self.x / self.y)
#
# obj2 = B()
# obj2.m1()
# obj2.m2()
# obj2.m3()
# obj2.m4()

#Ex3. Multilevel Inheritance............
# class A1:
#     x,y = 1,2
#     def a1(self):
#         print(self.x + self.y)
# class B1(A1):
#     a,b = 2,3
#     def b1(self):
#         print(self.a - self.b)
# class C1(B1):
#     i,j = 3,4
#     def c1(self):
#         print(self.a * self.b)
# class D1(C1):
#     p,q = 4,5
#     def d1(self):
#         print(self.p / self.q)
# obj1 = D1()
# obj1.a1()
# obj1.b1()
# obj1.c1()
# obj1.d1()

# obj2 = B1()
# obj2.a1()
# obj2.b1()
# obj2.c1()   #Error ----> AttributeError: 'B1' object has no attribute 'c1'. Did you mean: 'a1'?

# obj3 = C1()
# obj3.a1()
# obj3.b1()
# obj3.c1()
# obj3.d1()   #Error ----> AttributeError: 'C1' object has no attribute 'd1'. Did you mean: 'a1'?

# obj4 = D1()
# obj4.a1()
# obj4.b1()
# obj4.c1()
# obj4.d1()

#Example4 : Multiple inheritance----> more than one parent and single child..
# class A1:
#     x,y = 1,2
#     def add1(self):
#         print(self.x + self.y)
# class A2:
#     a,b = 10,20
#     def sub1(self):
#         print(self.a - self.b)
# class Aa1(A1, A2):
#     m,n = 100,200
#     def mul1(self):
#         print(self.m * self.n)
#
# objAa1 = Aa1()
# objAa1.add1()
# objAa1.sub1()
# objAa1.mul1()

#Ex5.  Heirarchy inheritance ----> One parent many childs.......
class A3:
    p,q = 10,20
    def mul1(self):
        print(self.p * self.q)
class Aa3(A3):
    m,n = 1000,2000
    def add1(self):
        print(self.m + self.n)
class Aa4(A3):
    j,k = 22,44
    def div1(self):
        print(self.j / self.k)
objAa3 = Aa3()
objAa3.add1()
objAa3.mul1()
objAa3.div()    # Error ---> AttributeError: 'Aa3' object has no attribute 'div'

objAa4 = Aa4()
objAa4.div1()
objAa3.mul1()
objAa4.add()    #Error ---> AttributeError: 'Aa3' object has no attribute 'div'









