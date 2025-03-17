persons_names = ["Mayowa", "chizoba", "Chigozie"]
new_names = []

"""
    A function that raise exceptions for wrong entries in a list

    Args:
        A list containing customer names
    Returns:
        Raise an exception if the names are not valid. 
        Valid names are strings that contain only alphabets
    
    """


"""
for n in names:
    if n[0].isupper():
        new_names.append(n[:-1] + "a") 
print(new_names)
"""




for name in persons_names:
    if name[0].isupper() and name[-1] == "a":
        new_names.append(name) 
    if name[0].isupper() and name[-1] != "a":
        name.replace(name[-1], "a")
        new_names.append(name)
print(new_names)