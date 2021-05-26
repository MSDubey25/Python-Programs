print("Accessing elements from a Dictionary")
dict1={1:1,2:2,3:3}
print(dict1)
print(dict1[1])
print(dict1.get(6))

print("adding a value")
dict1[4]="Namaste"
print(dict1)


print("creating dictionary of squares")

squares={1:1,2:4,3:9,4:16,5:25}
print(squares)
print("removing a particular item :25")
print(squares.pop(5))
print(squares)

print("removing arbitary  item")
print(squares.popitem())
print(squares)

del squares

print("creating a new dictionary using comprehension")
squares={x:x*x for x in range (7)}
print(squares)
print("There is a membership test but they are only for keys not values")

print("iterating through a dictionary using- for")
for i in squares:
    print(squares[i])

print("built in functions")
print("len() and sorted")
print(len(squares))
print("sorted() will sort the keys in order")
print(sorted(squares))
