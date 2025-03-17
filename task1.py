"""
Create a function that return the first name of anyone
Create another function that return the last name of anyone
Then Create a function that will concatenate the first name and the last name that will be returned from those 2 functions above.

"""



def firstName(myfirsName):
    return myfirsName


def lastName(myLastName):
    return myLastName


def fullName(myfirsName, myLastName):
    FirstName = firstName(myfirsName)
    LastName = lastName(myLastName)
    return f"My full name is {FirstName} {LastName}"
 
 
print(fullName("Chigozie", "Obasi"))