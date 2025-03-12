
def firstName(FN):
    return FN


def lastName(LN):
    return LN


def fullName(FN, LN):
    FN = firstName(FN)
    LN = lastName(LN)
    return f"My full name is {FN} {LN}"
 
 
print(fullName("Chigozie", "Obasi"))