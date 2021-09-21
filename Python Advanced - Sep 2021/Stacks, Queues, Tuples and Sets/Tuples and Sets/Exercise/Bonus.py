# Store numbers in phone book and check if they are in it. Then print them
def read_contact():
    people = {}
    while True:
        line = input()
        if line.isnumeric():
            break
        person, num = line.split("-")
        people[person] = num
    return people, int(line)


def print_people(contacts, number):
    for _ in range(number):
        name = input()

        if name in contacts:
            print(f"{name} -> {contacts[name]}")
        else:
            print(f"Contact {name} does not exist.")

contacts, number = read_contact()
print_people(contacts, number)