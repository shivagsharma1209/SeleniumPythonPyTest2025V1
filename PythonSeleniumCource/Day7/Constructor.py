#E1.
# class MyclassA:
#     name,age = "Pavan", 45
#     def __init__(self,name,age):
#         self.name = 'Shiva'
#         self.age = 35
#         print(self.name)
#         print(self.age)
# Obj = MyclassA(age=15,name="aaaa")

#Ex2 Constructor .............
# class Large:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
#
# Res3=Large(10,11)
# print(Res3.mul())
# print(Res3.div())
# print(Res3.add())
# print(Res3.sub())

#Ex3. Emp
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, self.salary)
emp1 = Employee("Rama", 12000)
emp2 = Employee("Shiva", 11000)
emp1.display()
emp2.display()
