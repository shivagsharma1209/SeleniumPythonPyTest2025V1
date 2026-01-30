#1. Psotional parms & Keyword parms
#All positional parms should appear before the keyword parms
#Ex1.
# def fun1(i,j):
#     print(i)
#     print(j)
# fun1(20,30)
# fun1(j=15, i=25)
#Ex2.
# def fun2(i,j=100):
#     print(i,j)
# fun2(200,200)
# fun2(102)

##ex.
# def greetings(name,age):
#     print(name,"", age)
# greetings("Mario",18)
#Ex. Use combination of Global and Local variables
# def funabc(a,b,c):
#     print(a,b,c)
# funabc(10,20,30)
# # funabc(20,a=20,c=30)    #TypeError: funabc() got multiple values for argument 'a'
# funabc(20,20,c=30)

#Ex. Function returns multiple values
def larg(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(larg(10,20))
print(larg(10,2))

res = larg(10,2)
print(res)





