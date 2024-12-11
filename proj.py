# we want to be able to add people including age, occupation,id number, and name
# referencing persons information will return results

employee = []


for i in range(3):
    print(i + 1, "Input")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    id = input("I.D.: ")


    person = {"name": name, "age": age, "email": email, "i.d.": id}
    employee.append(person)

print(employee)

