class votingCriteria(Exception):
    """ Creating user defined exceptions """
    def __init__(self):
        super()

try:
    print(votingCriteria.__doc__)
    age=input("Enter your age : ")
    age=int(age)
    if age<18:
        raise votingCriteria
except votingCriteria:
    print("below 18")
except TypeError:
    print("Entered Invalid Type")
except ValueError:
    print("Entered Invalid Value")
else:
    print("above 18")
