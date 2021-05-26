#List of keywords : False, class, finally, is, retuen, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, 
#not, with, as, if, elif, or, yield, assert, else, import, pass, break, except, in, raise


#1. True False
print(5<=5)
print(3==4)

#2. None
print(None ==0)
print(None==False)
print(None==[])
print(None == None)

def a_void_func():
    b=1
    a=2
    c=a+b;
x=a_void_func()
print(x)

#3. and, or, not
print("Example and, or, not")
print(True and False)
print(True or False)
print(not False)

#4. as
print("Example of:  as")
import math as myMath
print(myMath.cos(myMath.pi))

#5. assert
print("Example of assert (if true will not print anything if fale than throw error)")
assert 5>3

#6. break
print("Example of break & for")
for i in range(1,10):
    if i==5:
        break
    print(i)

#7.continue
print("Example of continue & for")
for i in range(1,10):
    if i==5:
        continue
    print(i)

#8. class & def
print("Example of class and def")
class Example:
    def func1(self,a):
        print("inside class function")
        print("function1 value {}".format(a))
eg=Example()
eg.func1(10)

#9. del
print("example of del")
q=10
print("value of q : {}".format(q))
print("deleting q with del")
del q


#10. if ...elif...else
print("example of if...elif...else")
a=20
if(a==20):
    print("a = {}".format(a))
elif(a==30):
    print("a = {}".format(a))
else:
    print("something else")

#11. try...raise...catch....finally
print("example of try...raise...catch...finally")
try:
    q=10/0
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division by zero cannot be performed")
finally:
    print("Execution successful")

#12. from...import
print("example of from and import")
from math import cos
print("cos(1) is = {}".format(cos(1)))

#13. global
print("example of global")
gVar=100
def read1():
    print("value of gVar : {}".format(gVar))
def write1():
    global gVar
    gVar=19
    print("changed value of gVar")
def write2():
    gVar=9
    print("local gVar :{}".format(gVar))
read1()
write1()
read1()
write2()
read1()

#14. in
print("example of in")
a=[1,2,3,4]
print("4 in the list :{}".format(4 in a))

#15. is
print("example of is")
print("True is : {}".format(True is True))

#16. lambda
print("example of lambda")
l=lambda x:x*x
for i in range(2,6):
    print(l(i))

#17. nonlocal
print("example of nonlocal")
def outer_func():
    a=5
    print("value of before nonlocal :",a)
    def inner_func():
        nonlocal a
        a=10
        print("inner func : ",a)
    inner_func()
    print("outer func : ",a)

outer_func()

#18. pass
print("example of pass")
def func(args):
    print("nothing happens when you do pass it represents their might be code in future")
    pass


#19. return
print("example of return")
def ret():
    return 10
print("value returned from func :{}",ret())

#20. while
print("example of while")
i=5
while(i>0):
    print(i)
    i=i-1

#21. with and as
print("example of with and as")
with open('example.txt','w+') as myfiles:
    myfiles.write("Hello world !!!")
    print("is file readable : {}".format(myfiles.readable()))
    print("is writable : {}".format(myfiles.writable()))
    myfiles.close()
    
with open('example.txt',"r+") as myfiles:
    print("wrote {} line in file example.txt".format(myfiles.readline()))
    myfiles.close()

#22. yield
print("example of yield")
def generator():
    for i in range(6):
        yield i*i

g=generator()
for i in g:
    print(i)



