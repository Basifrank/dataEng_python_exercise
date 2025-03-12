names = ["Mayowa", "chizoba", "Chigozie"]
new_names = []

for n in names:
    if n[0].isupper():
        new_names.append(n[:-1] + "a") 
print(new_names)