def make_decorated(func):
    def inner_func():
        print("I got decorated")
        func()
    return inner_func
@make_decorated
def simple_func():
    print("I am a simple function")

decor=make_decorated(simple_func)
decor()
print()
simple_func()

print("Another example")

def myDiv(func):
    def inner(x,y):
        print("I am Dividing ",x," and ",y)
        if(y==0):
            print("oops! cannot divide by zero")
            return
        return func(x,y)
    return inner

@myDiv
def do_divide(a,b):
    return a/b

print(do_divide(20,2))
print(do_divide(20,0))
