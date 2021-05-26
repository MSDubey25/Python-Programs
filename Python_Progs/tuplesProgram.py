# tupples are immutable and can be heterogeneous data types
#Functions of tuples
#1. all() - returns true if all the elements of tuples are true
#2. any() - returns true if one of the element is true
#. enumerate() - it retuens an enumerated object which contains all the keys and values as a pair
#3. len() - returns the length of the tupple
#4. max() - returns largest
#5. min() - returns smallest
#6. sorted() - returns a new sorted list
#7. sum() - returns sum of all elements
#8. tuple() - convert an iterable(list,String,set,dictionary) as a tuple

#creating an empty tuple
tuple1=()
print(tuple1)

tuple2=(1,2,3)
print(tuple2)

tuple3=(101,"ABC",2000.0,"HR")
print(tuple3)

print("creating a nested tuple")
tuple4=(11,[1,2,3],"string",(5,6,7,8))
print(tuple4)

#tuple can e created without () and also called as tuple packing
tuple5=101,"mani",20000.0,"GCM2"
print(tuple5)

#tuple unpacking is also possible
empid,name,sal,brand=tuple5
print(empid)
print(name)
print(sal)
print(brand)
print(type(tuple5))

#accessing elements in tuple
tuple6=('a','b','c','d','e')
print(tuple6)
print(tuple6[3])
print(tuple6[1])

# nested tuple

print(tuple4)
print(tuple4[0])
print(tuple4[1][2])
print(tuple4[2][3])
print(tuple4[3][2])

print("slicing tuple content")
print(tuple6[1:3])
print(tuple6[2-3])
print(tuple6[:])

#tuples can be reassigned
tuple7=(1,2,3)
print(tuple7)
print("reassigning")
tuple7=(4,5,6)
print(tuple7)

print("concatenation of tuples")
tuple8=('m','a','n','i')
tuple9=('k','a','n','t')
print(tuple8)
print(tuple9)
print(tuple8+tuple9)
print(("again",)*4)

print("tuple is immutable so elements cannot be deleted")

print("operation===================")
print(tuple9.count('n'))
print(tuple9.index('a'))

print("Membership")
print('a' in tuple9)
print('c' not in tuple9)

print("iteration through tuple elements")
tuple10=('w','e','l','c','o','m','e')
for letters in tuple10:
    print("letters===> ",letters)


print("built-in functions for tupple")
print("min :",min(tuple10))
print("max :",max(tuple10))
print("sorted :",sorted(tuple10))
print("len :",len(tuple10))

