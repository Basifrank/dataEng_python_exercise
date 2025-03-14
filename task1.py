"""
Create a function that return the first name of anyone
Create another function that return the last name of anyone
Then Create a function that will concatenate the first name and the last name that will be returned from those 2 functions above.

"""



def firstName(FN):
    return FN


def lastName(LN):
    return LN


def fullName(FN, LN):
    FN = firstName(FN)
    LN = lastName(LN)
    return f"My full name is {FN} {LN}"
 
 
print(fullName("Chigozie", "Obasi"))