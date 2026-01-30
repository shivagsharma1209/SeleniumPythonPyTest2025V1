# set is mutable, can not be updated directly, also unindexed
# set1={} # Empty set
# print(set1)

#Ex1. Declaration of set with elements
# S1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# print(S1)       # #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# print(type(S1)) # <class 'set'>
# print(id(S1))   # 2851581479840
# S2 = {'a','b','c','d'}
# print(S2)
# print(type(S2)) # {'c', 'a', 'b', 'd'}-- un ordered display
# S3 = {"x","y","z"}
# print(S3)
# print(type(S3)) #{'x', 'z', 'y'} -- un ordered set

# #Ex2. Accessing elements from the set
# s3 = {'a','b','c','d',1,2,3,4,"x","y","z"}
# print(s3)
# for s3 in s3:
#     print(s3)

# Ex3. Check for the items in the set
# s4 = {'a','b','c','d',1,2,3,4,"x","y","z"}
# print('y'  in s4) # True
# print(2 in s4)  # True
# print(5 in s4)  # False


#Ex4.Adding items to the set---using add() .. and update()
#add() --- will add only one element at a time
# S5 = {'a','b','c','d',1,2,3,4,"x","y","z"}
# S5.add('e')
# print(S5)
#update() --- Will add multiple elements at a time
# S5.update('aa',"bb",11)#TypeError: 'int' object is not iterable
# S5.update(['bb','11',"aa"]) #{1, 2, 3, 4, 'c', 'aa', 'd', 'a', '11', 'x', 'z', 'b', 'bb', 'y'}
# print(S5)

#Ex5. Find items in the set
# S5 = {'a','b','c','d',1,2,3,4,"x","y","z"}
# print(len( S5))

#Ex6. Remove/Clear/discard/del()------To remove items from the set
# S5 = {'a', 'b', 'c', 'd', 1, 2, 3, 4, "x", "y", "z"}
# S5.remove('a')
# print(S5)
# print(len( S5))
# S5.remove('e')  #KeyError: 'e'
# S5.discard('e')
# print(S5)
# S5.clear()  # Removes all items from the set and returns an empty set()
# print(S5)
# S5 = {'a', 'b', 'c', 'd', 1, 2, 3, 4, "x", "y", "z"}
# del S5
# print(S5)   #NameError: name 'S5' is not defined

#Ex7. Joining two sets...union()/update()/intersection()...........
# Set1 = {'aaaa', 'bbbb', 'cccc'}
# print(Set1)
# Set2 = {'111', '222', '333'}
# print(Set2)
# Set3 = Set1.union(Set2)
# print(Set3) # {'cccc', '111', '333', '222', 'bbbb', 'aaaa'}
# Set4 = Set1.symmetric_difference(Set2)
# print(Set4) #{'bbbb', 'aaaa', '222', 'cccc', '333', '111'}
# Set5 = Set1.intersection(Set2)
# print(Set5) #set()
# Set6 = Set1.difference(Set2)
# print(Set6)
# Set1.update(Set2)
# print(Set1)











