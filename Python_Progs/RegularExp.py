import re
if(re.search("ape","The ape is at the apex")):
    print("There is an ape")

allape=re.findall("ape.","The ape is at the apex appending")
for i in allape:
    print(i)

print("span() to get the location of the substring")
str1="The ape is at the apex"
for i in re.finditer("ape.",str1):
    locTuple=i.span()
    print(locTuple)
    print(str1[locTuple[0]:locTuple[1]])
str1="rat Cat mat fat hat"
for i in re.findall("[cmfrh]at",str1):
    print(i)

print("lower and upper c-m and C-M")    
for i in re.findall("[c-mC-M]at",str1):
    print(i)

print("other than C and r")
for i in re.findall("[^Cr]at",str1):
    print(i)

print("replace all matches")

replace=re.compile("[Cr]at")
owlfood=replace.sub("owl",str1)
print(owlfood)


print("searching \\\\")
randStr="This is my \\\\stuff"
print("find \\\\stuff :",re.search("\\\\stuff",randStr))

print("find \\\\stuff :",re.search(r"\\stuff",randStr))
print("finding any character")
print("char.char.char")
random="F.B.I C.B.I RBI C.I.D"
print("Matches : ",re.findall(".\..\..",random))


randstr='''This is a long
string that goes
for many lines'''
print(randstr)
regex=re.compile('\n')
randstr=regex.sub(' ',randstr)
print(randstr)

print("\d can be used instead of [0-9]\n\\D is same as [^0-9]")
digits="123h6f5"
print(digits)
print("Matches : ",re.findall("\d",digits))
print("Matches : ",re.findall("\D",digits))

digits="123 1234 12345 56432 567890"
print(digits)
print("Matched : ",re.findall("\d{5}",digits))

print("Matched : ",re.findall("\d{5,7}",digits))

print("\\w is same as [a-zA-Z0-9]")
print("\\W is same as [^a-zA-Z0-9]")

phone="412-555-2112"
print(phone)
if(re.search("\w{3}-\w{3}-\w{4}",phone)):
    print("This is a phone number")
name="manikant"
print(name)
if re.search("\w{2,10}",name):
    print("its a valid name")


print("\\s is same as [\\f\\n\\r\\t\\v]")
print("\\S is same as [^\\f\\n\\r\\t\\v]")

name="manikant Dubey"
print(name)
if re.search("\w{2,10}\s\w{2,10}",name):
    print("This is a calid name")

name="a am aape bro code aaaa aaaaaaaa"
print(name)
print("+ for one or more matches and * for ")
print("Matches : ",re.findall("a+",name))
print("Matches : ",re.findall("a*",name))

print("Regex that matches email id")
email="manikant.dubey1995@gmail.com a@.com ksnxk@gmail kj.@com abc@yahoo.com"
print(email)
#print("Matches : ",re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email))

print("Matches : ",re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[a-z]{2,3}",email))

