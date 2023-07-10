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

    #should show everyone on contact, and ask which person to delete.
    #search for the person's index on the list and delete it.
    for x in range(len(contacts["data"])):
        FN = contacts["data"][x]["FirstName"]
        LN = contacts["data"][x]["LastName"]
        print(FN, LN)

    #I didn't make this so that the user chooses the name, but rather the index.
    #bc I was thinking about the future when I would be working with an app
    #where I imagine where the user would have to click on the button where the name appears.
    #and I thought it would be convinient if it were to be an index that were returned to the server.
    index_to_delete = input("Enter the index of the person you want to delete")

    contacts["data"].pop(index_to_delete)

    with open("contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)