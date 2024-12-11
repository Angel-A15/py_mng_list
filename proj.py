# we want to be able to add people including age, occupation,id number, and name
# referencing persons information will return results
import json


def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    id = input("I.D.: ")
    occupation = input("Occupation: ")
    
    person = {"name": name, "age": age, "email": email, "i.d.": id, "occupation": occupation}
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], person["email"], person["i.d."], person["occupation"])
    

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invali number")

    people.pop(number - 1)
    print("Person deleted")


def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    display_people(results)


print("Hello, welcome to the Contact Management System.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]


while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete', or 'Search and 'Q' to exit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added")

    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Imvalid command.")

with open("contacts.json", "w") as f:
    # people = json.load(f)["contacts"]
    json.dump({"contacts": people}, f)

print(people)
