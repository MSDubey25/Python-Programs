#Sets
#sets are immuttable. we can add and remove elements in set(no duplicates allowed) and is unordered.

#Methods of set

#1. add()-
#2. clear()-
#3. copy()-
#4. difference()-
#5. difference_update()-
#6. discard()-
#7. intersection()-
#8. intersection_update()-
#9. isdisjoint()-
#10. issubset()-
#11. issuperset()-
#12. pop()-
#13. remove()-
#14. symmetric_difference()-
#15. symmetric_difference_update()-
#16. union()-
#17. update()-
#below are python built-in functions with sets
#18. all()-
#19. any()-
#20. enumerate()-
#21. len()-
#22. min()-
#23. max()-
#24. sorted()-
#25. sum()-

print("creating set of integers")
set1={1,2,3,6,5}
print(set1)

print("creating set of mixed datatypes")
set2={10,"Manikant",(1,2,3)}
print(set2)

print("duplicates are not allowed in sets")
set3={2,3,4,4,5,2,3,1}
print(set3)

print("set cannot have mutable items")
#set4={1,2,[3,4]}

print("we can create set from list")
set4=set([1,2,3,4,5])
print(set4)
print(type(set4))


print("we can make list from set")
list1=list(set4)
print(list1)
print(type(list1))

print("Operations on set")
set5={22,3,44,55,66}
print(set5)
print("set object does not support indexing")
#set5[1]

print("adding element with add()")
set5.add(77)
print(set5)
print("add multiple items using update()")
set5.update([0,8,9])
print(set5)
print("add list and set using update()")
set5.update([99,88],{909,808,798})
print(set5)

print("discard an element which is not present :no error")
set5.discard(999)
print(set5)

print("remove an element which is not present :raise error")
#set5.remove(999)

print("discard and remove existing element 909,808")
set5.discard(909)
set5.remove(808)
print(set5)

print("pop will remove elements according to the predefined order")
print("element : {} popped".format(set5.pop()))
print("element : {} popped".format(set5.pop()))
print(set5)
print("set5 is cleared using clear()")
set5.clear()
print(set5)

print("union os set1 & set2 using union()")
print(set1.union(set2))

print("union of set2 & set3 using |")
print(set2 | set3)

set2={1,2,3,4}
set3={3,4,6,7}
print(set2)
print(set3)
print("intersection of set3 & set2 using intersection()")
print(set3.intersection(set2))

print("intersection of set2 & set3 using '&'")
print(set2 & set3)

print("set difference of set2 and set3 using difference()")
print(set2.difference(set3))

print("set difference of set3 and set2 using -")
print(set3 - set2)

print("symmetric difference using ^ and symmetric_difference()")
print(set2 ^ set3)

print("Membership check")
print(6 in set3)
print(6 not in set2)

print("iterating through set")
for i in set("ManiBhai"):
    print(i)

print("built-in function for set(len(),max(),min(),sorted())")
print(len(set3))
print(max(set3))
print(min(set3))
print(sorted(set3))

print("python frozenset")
print("frozenset is a new class that has characteristics of a set, but its elements cannot be changed once assigned.")
print("while tupples are immutable lists, frozensets are immutable sets.")


myset1=frozenset([1,2,3,4])
myset2=frozenset([3,4,5,6])

print(myset1)
print(myset2)
print(myset1.difference(myset2))
print(myset1.union(myset2))
print(myset1.intersection(myset2))
print(myset1.symmetric_difference(myset2))
