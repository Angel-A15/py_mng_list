# we want to be able to add people including age, occupation,id number, and name
# referencing persons information will return results


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    id = input("I.D.: ")
    occupation = input("Occupation: ")
    
    person = {"name": name, "age": age, "email": email, "i.d.": id, "occupation": occupation}
    return person

print("Hello, welcome to the Contact Management System.")
print()
command = input("You can 'Add', 'Delete', or 'Search: ").lower()
people = []

if command == "add":
    person = add_person()
    people.append(person)
    print("Person added")

elif command == "delete":
    pass
elif command == "search":
    pass
else:
    print("Imvalid command.")

print(people)
