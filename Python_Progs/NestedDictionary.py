people={1:{'name':'John','age':'24','sex':'M'},
        2:{'name':'Maria','age':'23','sex':'F'}}
print(people)

print("Accessing Elements of Dictionary")

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

print("Adding elements to a dictionary")
people[3]={'name':'mani','age':'25','sex':'M'}
people[4]={}
people[4]['name']='Luna'
people[4]['age']='22'
people[4]['sex']='F'

print(people)
print("deleting elements")
del people[4]['sex'],people[4]['age']
print(people[4])

print("Iterating through nested Dictionary")

for key,value in people.items():
    print("\nperson ID : ",key)
    for key in value:
        print(key+ ": "+value[key])
