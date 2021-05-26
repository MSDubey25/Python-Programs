def printMessage(message):

    def printInner():
        print(message)

    return printInner

another=printMessage("Hello World!!!")
another()

def multi(n):
    def multiInner(x):
        return x*n
    return multiInner

time3=multi(3)
time5=multi(5)
print(time3(6))
print(time5(2))
print(time5(time3(2)))


