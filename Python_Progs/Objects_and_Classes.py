class ComplexNumber:
    #constructor irrespective of class name
    def __init__(self,real=0,imag=0):
        print("in constructor")
        self.real_part=real
        self.imag_part=imag

    def displayComplex(self):
        print("complex Number is :")
        print("{0}+{1}j".format(self.real_part,self.imag_part))

#create an object of a class
obj1=ComplexNumber(40,50)

#calling display function
obj1.displayComplex()


#Creating another object and creating a new attribute to that particular object
obj2=ComplexNumber(10,20)
obj2.new_attribute=80
obj2.displayComplex()
print("printing all the attribute values")
print(obj2.real_part,obj2.imag_part,obj2.new_attribute)

#Deleting object attributes and the object
del obj1.real_part
print("real part of obj1 is deleted")
print(obj1)
del obj1
print("deleted obj1 object")
print(obj1)
