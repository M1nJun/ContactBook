import json

contact = json.load(open("contact.json"))

if type(contact) is dict:
    contact = [contact]

FN = input("Enter first name: ")
LN = input("Enter last name: ")
PN = input("Enter phone number: ")

contact.append({
    "FirstName": FN,
    "LastName": LN,
    "PhoneNum": PN
})

with open("contact.json", "w") as outfile:
    json.dump(contact, outfile)
