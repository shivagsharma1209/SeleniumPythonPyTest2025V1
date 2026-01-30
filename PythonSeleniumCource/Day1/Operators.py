a=10,'num',"aaaaaaaaaa"
print(a)
del a   # deletes a
# print(a)  NameError: name 'a' is not defined
# print(type(a))   NameError: name 'a' is not defined
print(id(a))    # NameError: name 'a' is not defined

b= 1,2,3,4,5,6
print(b)
print(type(b))
print(id(b))

i,j=10,20
print(i,j)
print(type(i))
print(id(i))

x='xxx','yyyyyy'
print(x)
print(type(x))
print(id(x))