customer_names = ["Wofai", "Zainab", "A4atullah"]

def checkNames(names):
    notalpha = [  name for name in names if name.isalpha() == False]
    if len(notalpha) > 0:
        raise TypeError(f"These are the invalid names: {notalpha}")
    else:
        print("All names are valid")
        
        
checkNames(customer_names)