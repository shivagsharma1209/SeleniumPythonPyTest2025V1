#List[] --> Collection of ordered elemets. List is immutable(changed)..works on Index based..
#Ex1. declare list
# L1 = [1,2,3,4,5,6]
# L2 = ['a','b','c','d','e','f']
# L3 = ["aa","bb","cc","dd","ee","ff"]
# print(l1)
# print(L2)
# print(L3)

#Ex2. Accessing elemsts from the list...
# print(L1[0])
# print(L2[1])
# print(L3[2])

#E3.Add elemts to the list ---append(0/insert()..........
# L1 = [1,2,3,4,5,6]
# L1.append(7)
# print(L1)   #[1, 2, 3, 4, 5, 6, 7]
# # L1.insert(8)    #TypeError: insert expected 2 arguments, got 1
# L1.remove(1)
# print(L1)   #[2, 3, 4, 5, 6, 7]

#Ex4. Update the list
# L2 = ['a','b','c','d','e','f']
# L2[0] = 'aaaaaaa'
# print(L2)   #['aaaaaaa', 'b', 'c', 'd', 'e', 'f']
# L3 = ["aa","bb","cc","dd","ee","ff"]
# L2[4] = 'vvvvvvvvvv'
# print(L2)   #['aaaaaaa', 'b', 'c', 'd', 'vvvvvvvvvv', 'f']

# #Ex5. Read elemets from the lsit
# for i in L2:
#       print(i)
# print(L3[-3:-1])    #['dd', 'ee']

#Ex6. Check for the element present  the list
# L1 = [1,2,3,4,5,6]
# L2 = ['a','b','c','d','e','f']
# L3 = ["aa","bb","cc","dd","ee","ff"]
#
# if 3 in L1:
#     print(" Item existing") # Item existing
# else:
#     print("Item not existing")
# if 'h' in L2:
#     print("Item existing")
# else:
#     print("Item not existing")  #Item not existing
# if 'aa' in L3:
#     print("Item existing")
# else:
#     print("Item not existing")  #Item existing

#Ex7. Length of the list
# L1 = [1,2,3,4,5,6]
# L2 = ['a','b','c','d','e','f']
# L3 = ["aa","bb","cc","dd","ee","ff"]
# print(len(L1))
# print(len(L2))
# print(len(L3))

#Ex8.cler()/pop()/remove/del...........
# L1 = [1,2,3,4,5,6]
# L2 = ['a','b','c','d','e','f']
# L3 = ["aa","bb","cc","dd","ee","ff"]
# # L1.clear()
# # print(L1)   # clear will return an empty list []
# L2.pop(1)
# print(L2)   #['a', 'c', 'd', 'e', 'f'] --'b' is removed
# # del L3[3]
# # print(L3)   #['aa', 'bb', 'cc', 'ee', 'ff']----'dd' is deleted
# L3.pop(3)
# print(L3)   # Same as del.....['aa', 'bb', 'cc', 'ee', 'ff']----'dd' is deleted

#Ex9. copying the lsit
# L1 = [1,2,3,4,5,6]
# L2 = ['a','b','c','d','e','f']
# L3 = ["aa","bb","cc","dd","ee","ff"]
# L4 = list(set(L1+L2+L3))    #[1, 2, 3, 4, 5, 6, 'e', 'ff', 'aa', 'bb', 'dd', 'b', 'f', 'c', 'ee', 'a', 'cc', 'd']
# print(L4)
#Joining two lists/combining two lists
# L5 = L1 + L2 + L3
# print(L5)   #1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
# L6 = list(L1)
# print(L6)   #[1, 2, 3, 4, 5, 6]
# L7 = L2.copy()
# print(L7)   #['a', 'b', 'c', 'd', 'e', 'f']
# #using extend()
# L1.extend(L2)
# print(L1)   #[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f']-- adding all elemets of L2 into L1
# #Using loop stmt
# for i in L1:
#     L2.append(i)
#     print(L2)
#     print(L1)

L2 = ['a','b','c','d','e','f']
L3 = ["aa","bb","cc","dd","ee","ff"]
L4 = ['a','b','c','d','e','f']
if L2 == L4:
    print("valid")
else:
    print("not valid")

















