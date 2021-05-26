#Methods for arrays(List)
#append(),extend(),insert(),remove(),pop(),clear(),index(),count(),sort(),reverse(),copy()


#Defining and declaring an Array. There is no such data structure in python so we are going to use List(does everything as array)
arr=[1,2,3,4,5,6]
print(arr)

#accessing elements of arrays
print(arr[0])
print(arr[1])
print(arr[-1])#negavtive indexing (as its double circularly linked list -1 means the last element and so on)
print(arr[-2])

brands=["Coke","apple","microsoft","Dell"]

#finding the length of the array
print(brands)
print(len(brands))

#adding elements to an array
brands.append("Intel")

print(brands)
#removing elements from an array
colors=["violet","indigo","blue","green","yellow","orange","red"]
print(colors)
print("deleting using del")
del colors[4]
print(colors)
print("deleting using remove()")
colors.remove("blue")
print(colors)
print("deleting using pop")
print("poping elemenet :{}".format(colors.pop(3)))
print(colors)

#modifying elements of array using indexing
fruits=["Apple","Banana","Mango","Grapes","orange"]
print(fruits)
fruits[1]="pipeapple"
fruits[-1]="Guava"
print(fruits)

#concatinating two arrays using + operator

concat=[1,2,3]
print(concat)
concat+[4,5,6]
print(concat)
concat=concat+[4,5,6]
print(concat)

#repeating elements in array
repeat="a"
print(repeat)
repeat=repeat*5
print(repeat)

#slicing an array
print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])
print(fruits[-4:])
print(fruits[-3:-1])

#working with two dimentional arrays
multid=[[1,2],[3,4],[5,6],[7,8]]
print(multid)
print(multid[0])
print(multid[3])
print(multid[0][0])
print(multid[2][1])



