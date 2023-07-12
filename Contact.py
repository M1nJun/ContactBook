import json

def add_contact(PN, FN, LN):
    with open("contacts/contact.json") as infile:
        contacts = json.load(infile)

    new_contact = {PN:{"FirstName": FN, "LastName": LN}}
    contacts["data"].update(new_contact)

    #without the indent, it appeared on the json file as just a straight line of data.
    with open("contacts/contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)

def remove_contact(index_to_delete):
    with open("contacts/contact.json") as infile:
        contacts = json.load(infile)

    contacts["data"].pop(index_to_delete)

    with open("contacts/contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)

def edit_contact(PN, option, edit):
    with open("contacts/contact.json", "r") as infile:
        contacts = json.load(infile)
    
    if option == 1:
        contacts["data"][PN]["FirstName"] = edit
    if option == 2:
        contacts["data"][PN]["LastName"] = edit
    if option == 3:
        contacts["data"][edit] = contacts["data"][PN]
        del contacts["data"][PN]
    
    with open("contacts/contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)


def show_contact():
    with open("contacts/contact.json") as infile:
        contacts = json.load(infile)

    for key,val in contacts["data"].items():
        PN = key
        FN = val["FirstName"]
        LN = val["LastName"]
        print(f'Phone number is: {PN}\nName is: {FN}-{LN}')

#if the user does not have a username.json file, make one
#change the function so that it takes in parameters from main.py