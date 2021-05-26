print("Demonstration of the use of Property")
class Celcius:
    def __init__(self,temp=0):
        print("Assigning temperature values")
        self._temperature=temp
        self.val=0

    def convert2Far(self):
        return (self._temperature*1.8)+32
    
    
    def get_Temp(self):
        print("Getting temperature value")
        return self._temperature

    
    def set_Temp(self,temp):
        if temp<-273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting temp value")
        self._temperature=temp
#    temperature=property(get_Temp,set_Temp)
    temperature=property()
    temperature=temperature.getter(get_Temp)
    temperature=temperature.setter(set_Temp)
print("property() is a built-in function, creates and returns a property object\nproperty(fget(),fset(),fdel(),doc())")

c=Celcius(5)
print(c.temperature)
c.temperature=100
print(c.temperature)
print(c.__dict__)


























