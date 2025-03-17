#Task 2

person_details = ["first name", "last_name", "date of birth"]


def transforn_name(person_details): 
    new_person = []

    for person in person_details:
        person = person.lower()
        person = person.replace(" ", "_")
        new_person.append(person)
    return new_person

print(transforn_name(person_details))