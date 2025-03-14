#Task 2
"""
Transform the name of the values of a list to follow 
the naming convention we have in the 
"""

person_details = ["first name", "last_name", "date of birth"]

new_person = []

for n in range(len(person_details)):
    new_person.append(person_details[n].replace(" ", "_"))     

print(new_person)