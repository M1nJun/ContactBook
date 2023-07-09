import json

# def add_contact():
#     with open("contact.json") as infile:
#         contacts = json.load(infile)

#     FN = input("Enter first name: ")
#     LN = input("Enter last name: ")
#     PN = input("Enter phone number: ")

#     new_contact = {"FirstName": FN, "LastName": LN, "PhoneNum": PN}
#     contacts["data"].append(new_contact)

#     #without the indent, it appeared on the json file as just a straight line of data.
#     with open("contact.json", "w") as outfile:
#         json.dump(contacts, outfile, indent=4)


with open("contact.json") as infile:
    contacts = json.load(infile)

#should show everyone on contact, and ask which person to delete.
#search for the person's index on the list and delete it.
contacts["data"].pop(3)

with open("contact.json", "w") as outfile:
    json.dump(contacts, outfile, indent=4)