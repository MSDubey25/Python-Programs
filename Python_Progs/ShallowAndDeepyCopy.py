list1=[1,2,3,4,5]
list2=list1
print("list1 -> ",list1)
print("list2 -> ",list2)
print("id of list1 -> ",id(list1))
print("id of list2 -> ",id(list2))
list1.append([0,8,9])
print("list1 -> ",list1)
print("list2 -> ",list2)

print("craeting a copy using shallow copy")
import copy
old=[[1,2],[3,4],[5,6],[7,8]]
new=copy.copy(old)
print("old list : ",old)
print("new list : ",new)

print("adding elements to old list using shallow copy")
old.append([4,4,4,4])
print("old list : ",old)
print("new list : ",new)

print("adding new nested objects using shallow copy")
old[1][1]='AA'
print("old list : ",old)
print("new list : ",new)

print("id of list1 -> ",id(list1))
print("id of list2 -> ",id(list2))

print("copying a list using deepcopy (creates a new object and recursively add objects)")
old1=[[1,2,3],[3,4,5]]
new1=copy.deepcopy(old1)

print("old list : ",old1)
print("new list : ",new1)
print("id of list1 -> ",id(old1))
print("id of list2 -> ",id(new1))
old1[1][1]=99
old1.append(777)
print("old list : ",old1)
print("new list : ",new1)


