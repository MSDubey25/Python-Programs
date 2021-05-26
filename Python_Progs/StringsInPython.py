#how strings can be declared
mystr='Manikant'
print(mystr)
mystr="Dubey"
print(mystr)
mystr='''Welcome to the Jungle '''
print(mystr)
mystr="""Hello World!!!"""
print(mystr)

mystr='language'
print("mystr = ",mystr)
print('mystr[0] = ',mystr[0])
print('mystr[-1] = ',mystr[-1])
print('mystr[1:5] = ',mystr[1:5])
print('mystr[5:-2] = ',mystr[5:-2])


print("Strings are immutable but can be reassigned")
mystr="pragramming"
print('mystr = ',mystr)

count=0
print("Iterating through a string using for")
for i in 'Manikant Dubey':
    if(i=='a'):
        count+=1
print(count,' times a letter has been found')

print("built-in functions")
print("list(enumerate(mystr)) : ",list(enumerate(mystr)))

print("String formatting using escape sequence")
print('''tell me what's your name?''')
print('tell me "what\'s your name?"')
print("tell me 'what\'s your name?'")
print("tell me \"what's your name?\"")

print("C:\\Users\\Mani\\example.txt")
print("this line is having a newline \n character")
print("this line is having a tab \t character")
print("ABC is written in \x41 \x42 \x43 (HEX) Representation")


print("format() method default(implicit) order")
defaultOrder="{} {} and {}".format('Today','is','Sunday')
print(defaultOrder)
print("positional arguments")
position="{1} {0} and {2}".format('is','Today','Sunday')
print(position)
print("order using keyword argument")
key="{t} {i} and {s}".format(i='is',s='Sunday',t='Today')
print(key)


print("formatting numbers")
print("Required binary representation of {0} is {0:b}".format(20))
print("formatting floats")
print("Exponent Representation : {0:e}".format(1365.345))
print("round-offs")
print("one third is :{0:.3f}".format(1/3))



