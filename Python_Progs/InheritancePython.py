print("example of Single inheritance")
class bird:

    def __init__(self):
        print("bird class constructor is executing")

    def whatType(self):
        print("i'm a bird")

    def canSwim(self):
        print("I can swim")

class penguin(bird): #inheriting the bird class

    def __init__(self):
        super.__init__(super())
        print("penguin class constructor is executing")

    def whoiam(self):
        print("i'm penguin")

    def canRun(self):
        print("i can run")

p=penguin()
p.whatType()
p.canSwim()
p.whoiam()
p.canRun()


class myParrot:

    def canFly(self):
        print("i'm parrat and i can fly")

    def canSwim(self):
        print("i'm parrot and i can't swim")

class myPenguin:

    def canFly(self):
        print("penguin can't fly")

    def canSwim(self):
        print("penguin can swim")

def birdTest(b):
    b.canFly()
    b.canSwim()

parrot=myParrot()
pen=myPenguin()
birdTest(parrot)
birdTest(pen)

print("example of multiple inheritance")

class Base1:
     def funcBase1(self):
         print("funcBase1() executed")

class Base2:
     def funcBase2(self):
         print("funcBase2() executed")

class Base3:
     def funcBase3(self):
         print("funcBase3() executed")


class MultiDerived(Base1,Base2,Base3):
     def multiderived1(self):
         print("multiDerived11() executed")

md=MultiDerived()
md.funcBase1()
md.funcBase2()
md.funcBase3()
md.multiderived1()
