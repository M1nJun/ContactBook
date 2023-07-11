import json

def add_contact():
    with open("contact.json") as infile:
        contacts = json.load(infile)

    FN = input("Enter first name: ")
    LN = input("Enter last name: ")
    PN = input("Enter phone number: ")

    new_contact = {"FirstName": FN, "LastName": LN, "PhoneNum": PN}
    contacts["data"].append(new_contact)

    #without the indent, it appeared on the json file as just a straight line of data.
    with open("contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)


def remove_contact():
    with open("contact.json") as infile:
        contacts = json.load(infile)

    for index, contact in enumerate(contacts["data"]):
        FN = contact["FirstName"]
        LN = contact["LastName"]
        print(f'{index}:{FN}-{LN}')

    index_to_delete = input("Enter the index of the person you want to delete: ")

    contacts["data"].pop(index_to_delete)

    with open("contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)


def edit_contact():
    with open("contacts.json", "w") as infile:
        contacts = json.load(infile)
    
    


def show_contact():
