a=100
print(type(a))
print("int :",isinstance(a,int))
print("float :",isinstance(a,float))
print("complex :",isinstance(a,complex))

b=10.5
print(type(b))
print("int :",isinstance(b,int))
print("float :",isinstance(b,float))
print("complex :",isinstance(b,complex))


c=10+2j
print(type(c))
print("int :",isinstance(c,int))
print("float :",isinstance(c,float))
print("complex :",isinstance(c,complex))

print(0b10011)
print(0xab)
print(0o23)


print(int(50.70))
print(50.70)

print("importing decimal module")
data1=0.1+0.2
print(data1)
from decimal import Decimal as D
print(D('0.1')+D('0.2'))
print(D('0.1')*D('0.2'))

print("importing Fraction module")
from fractions import Fraction as F
print(F(5))
print(F(5))
print(F(1,5))


print("importing math module")
import math
print(math.pi)
print(math.cos(10))
print(math.log(10))
print(math.log10(10))
print(math.exp(10))
print(math.factorial(5))
print(math.sinh(10))
print(abs(-12.34))

print("importing Random module")
import random
print('Random number --> ',random.randrange(5,15))
print('Random number --> ',random.randrange(5,15))
print('Random number --> ',random.randrange(5,15))
print('Random number --> ',random.randrange(5,15))

day=['sun','mon','tue','wed','thu','fri','sat']
print(day)
print(random.choice(day))
print(day)
random.shuffle(day)
print(day)
print(random.random())




