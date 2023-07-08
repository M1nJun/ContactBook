import json

contact = {
    "FirstName": "Minjun",
    "LastName": "Lee",
    "PhoneNum": "9206669262"
}

x = contact["FirstName"]
y = contact["LastName"]
z = contact["PhoneNum"]
print(x,y,z)

FN = input("Enter first name: ")
LN = input("Enter last name: ")
PN = input("Enter phone number: ")

contact.update({"FirstName": FN, "LastName": LN, "PhoneNum": PN})

x = contact["FirstName"]
y = contact["LastName"]
z = contact["PhoneNum"]

#print(x,y,z)

#json_object = json.dumps(contact,indent=4)
#print(json_object)

#open() is used to open files, takes two parameters
#file name(or path) and the mode
#with ensure that the file is properly closed after use
with open("contact.json", "w") as outfile:
    json.dump(contact, outfile)

#need to figure out how to connect to sql on vs code
#need to figure out how to save column name as key and fill in with value
#need to figure out how to have multiple dictionarys like instances of classes

