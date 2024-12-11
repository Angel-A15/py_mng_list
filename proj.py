# we want to be able to add people including age, occupation,id number, and name
# referencing persons information will return results

names = []
ages = []
emails = []

for i in range(3):
    print(i + 1, "Input")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    names.append(name)
    ages.append(age)
    emails.append(email)


print(names, ages, emails)