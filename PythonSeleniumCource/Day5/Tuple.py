#Declaration
#Tuple is an ordered collection and it is mutable (can not be changed)
# T1 = (1,2,3,4,5,6,7,8,9)
# print(T1)   #(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(type(T1)) #<class 'tuple'>
# T2 = ('a','b','c','d','e','f','g','h','i')
# print(T2)
# T3 = ("aaa","bbb","ccc","ddd")
# print(T3)
from pickle import TUPLE2

#Ex2. Accessing elements from tuple
# print(T1[2])    #3
# print(T2[4])    #e
# print(T3[3])    #ddd

#Ex3. Read elements from tuple
# T1 = (1,2,3,4,5,8,9)
# T2 = ('a','b','c','d','e','f','i')
# T3 = ("aaa","bbb","ccc","ddd")
# for i in T1:
#     print(i)
# for i in T2:
#     print(i)
# for i in T3:
#     print(i)
# print(T1[1:-3]) #(2, 3, 4)

#Ex4.Update yuple is not possible...indirect way tuple ---->list--update--->list---->tuple
# T4 = ("aaa","bbb","ccc","ddd")
# print(T4)   #('aaa', 'bbb', 'ccc', 'ddd')
# print(type(T4)) #<class 'tuple'>
# #convert tuple to list
# T4 = list(T4)
# print(T4)   #['aaa', 'bbb', 'ccc', 'ddd']
# print(type(T4)) #<class 'list'>
#
# #update list--- add elemt to the lsit
# T4[3]  = "eee"
# print(T4)   #['aaa', 'bbb', 'ccc', 'eee']
# print(type(T4)) #<class 'list'>
# T4 =tuple(T4)
# print(T4)   #('aaa', 'bbb', 'ccc', 'eee')
# print(type(T4)) #<class 'tuple'>
# #Ex5. Add elements to the tuple through list conversion
# T5 = ('a','b','c',"aaa","bbb","ccc","ddd")
# T5 = list(T5)
# print(T5)   #['a', 'b', 'c', 'aaa', 'bbb', 'ccc', 'ddd']
# T5.append("aa11bb")
# print(T5)   #['a', 'b', 'c', 'aaa', 'bbb', 'ccc', 'ddd', 'aa11bb']
# T5[4] ='23nnnc'
# print(T5)   #['a', 'b', 'c', 'aaa', '23nnnc', 'ccc', 'ddd', 'aa11bb']
# del(T5[2])
# print(T5)   #['a', 'b', 'aaa', '23nnnc', 'ccc', 'ddd', 'aa11bb']
# T5 = tuple(T5)
# print(T5)   #('a', 'b', 'aaa', '23nnnc', 'ccc', 'ddd', 'aa11bb')

#Ex6. aad  and Compare tuples
T1 = (1,2,3,4,5,6,7,8,9)
T2 = ('a','b','c','d','e','f','g','h','i')
T3 = T1 + T2
print(T3)
if T1 != T3:
    print('T1 is not same as T3')
else:
    print('T1 is not in T3')





















