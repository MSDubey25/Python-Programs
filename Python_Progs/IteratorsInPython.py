mylist=[1,4,2,3,5]
print(mylist)
print("get an iterator using iter()")
out_iter=iter(mylist)
print("Iterating through it using next()")
print(next(out_iter),' is the next element')
print(next(out_iter),' is the next element')
print("next() is same as calling ob.__next__()")
print(out_iter.__next__(),' is the next element')
print(out_iter.__next__(),' is the next element')

print(out_iter.__next__(),' is the next element')
#print(out_iter.__next__(),' is the next element')


class powOfTwo:
    ''' class to implement an iterator of power of two'''
    
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if(self.n<=self.max):
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration

print(powOfTwo.__doc__)
a=powOfTwo(4)
i=iter(a)
print(next(i))
print(next(i))
print(i.__next__())

print("iteration completed")
for i in mylist:
    print(i)
else:
    print("printing completed")

for i in range(2,45,2):
    print(i)
else:
    print("print completed")
