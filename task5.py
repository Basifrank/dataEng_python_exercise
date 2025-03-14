# Task 5 integers in a list
customer_names = ["Wofai", [1,2], "A4atulla", "Mayor", 15, 10, 20, 30]



def wrong_entries(names):
    """
    A function that returns intergers found in a list 

    Args:
        A list containing integers and string
    Yield:
        Integers found in the list
    
    """
    for name in names:
        if type(name) == int:           
            yield(name)

invalid_names = wrong_entries(customer_names)

print(invalid_names)
print(list(invalid_names))