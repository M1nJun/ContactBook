#class Contact:
#
#    def __init__(self, FN, LN, PN):
#        self.FirstName = FN
#        self.LastName = LN
#        self.PhoneNum = PN
#        #possibly a picture next time
#        #will think of a way to add to emergency contact

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

print(x,y,z)
