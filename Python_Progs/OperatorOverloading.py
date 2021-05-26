a=1
b=2
print("value of a {} and b {} = {}".format(a,b,a.__add__(b)))

print("operator overloiading")
class mypoint:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "({0} {1})".format(self.x,self.y)

    def __add__(self,other):
        print("Overloaded + operator")
        x=self.x+other.x
        y=self.y+other.y
        return mypoint(x,y)

    def __lt__(self,other):
        print("Overloaded < operator")
        x=(self.x**2)+(other.x**2)
        y=(self.y**2)+(other.y**2)
        return x<y
p1=mypoint(1,2)
p2=mypoint(4,5)
print(p1)
print(p2)
print()
print(p1<p2)
print(p1+p2)
print()
print(p1.__lt__(p2))
print(p1.__add__(p2))

