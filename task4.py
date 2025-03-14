# Task  4. A function to raise exceptions for wrong entries in a list

customer_names = ["Wofai", "Zainab", "A4atullah"]

def checkNames(names):
    """
    A function that raise exceptions for wrong entries in a list

    Args:
        A list containing customer names
    Returns:
        Raise an exception if the names are not valid. 
        Valid names are strings that contain only alphabets
    
    """
    
    notalpha = [  name for name in names if name.isalpha() == False]
    if len(notalpha) > 0:
        raise TypeError(f"These are the invalid names: {notalpha}")
    else:
        return print("All names are valid")
        
        
checkNames(customer_names)