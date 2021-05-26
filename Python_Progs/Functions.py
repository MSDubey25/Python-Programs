def hello() :
    """ this is a multiline text for func documnetation"""
    print("Hello lets start with the menu driven operations")
hello()
print(hello.__doc__)

def addition(x,y):
    print("Adding the Numbers {},{}".format(x,y))
    return(x+y)
def subtraction(x,y):
    print("subtracting the Numbers {},{}".format(x,y))
    return(x-y)
def division(x,y):        
    print("dividing the Numbers {},{}".format(x,y))
    out=-1
    try:
        if y==0:
            raise ZeroDivisionError
        else:
            print("Division is possible")
            out=x/y
    except ZeroDivisionError:
        print("cannot divide by zero")
    finally:
        print("Executed")
    return(out)
def multiplication(x,y):
    print("multiplying the Numbers {},{}".format(x,y))
    return(x*y)

def menu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    return int(input("Enter your choice :"))

def calculation():
    ch=menu()
    num1=int(input("Enter the 1st Number :"))
    num2=int(input("Enter the 2nd Number :"))
    if ch==1:
         res=addition(num1,num2)
    elif ch==2:
         res=subtraction(num1,num2)
    elif ch==3:
         res=division(num1,num2)
    elif ch==4:
         res=multiplication(num1,num2)
    if(res!=-1):
        print("result is :",res)

calculation()
print("Done dona done")
