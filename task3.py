# Task 3: Return names that begin with a capital letter and end with letter a

names = ["Mayowa", "chizoba", "Chigozie"]
new_names = []

"""
    A code that will extract names that begin with 
    a capital letter and end with letter a

        
    """



for n in names:
    if n[0].isupper():
        new_names.append(n[:-1] + "a") 
print(new_names)