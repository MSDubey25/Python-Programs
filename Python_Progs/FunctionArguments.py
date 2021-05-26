print("passing parameters to a function")
def findMax(a,b):
    if a<b:
        return b
    else:
        return a
print("max between 100 and 20 is ",findMax(100,20))

print("default arguments")

def status(name,msg="how are you?"):
    print("Hello {}, {}".format(name,msg))
status("manikant","have a nice day!")
status("manikant")

print("Arbitary arguments")
def sumAll(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print("sum of 1-4 is :",sumAll(1,2,3,4))
print("sum of 1-8 is :",sumAll(1,2,3,4,5,6,7,8))

print("defaukt arguments")
def defaultArgs(a=1,b=2,c=3):
    print("a={}, b={}, c={}".format(a,b,c))

defaultArgs(100)
defaultArgs(1,200)
defaultArgs(300,400,43)
defaultArgs(c=45)
defaultArgs(b=67,a=87)

defaultArgs()

defaultArgs(c=78,a=90,b=80)
