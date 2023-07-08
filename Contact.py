import json

contact = {
    "FirstName": "Minjun",
    "LastName": "Lee",
    "PhoneNum": "9206669262"
}

# x = contact["FirstName"]
# y = contact["LastName"]
# z = contact["PhoneNum"]
# print(x,y,z)

# FN = input("Enter first name: ")
# LN = input("Enter last name: ")
# PN = input("Enter phone number: ")

# contact.update({"FirstName": FN, "LastName": LN, "PhoneNum": PN})

# x = contact["FirstName"]
# y = contact["LastName"]
# z = contact["PhoneNum"]

#print(x,y,z)

#json_object = json.dumps(contact,indent=4)
#print(json_object)

#open() is used to open files, takes two parameters
#file name(or path) and the mode
#with ensure that the file is properly closed after use
with open("contact.json", "w") as outfile:
    json.dump(contact, outfile)

#Question: load from json file as a string?dict?
#Answer: I found out from an error that this was loaded as a 'dict' object and therefore can't use append
#does ' or " matter?
contact = json.load(open("contact.json"))

#convert from dict to list
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
