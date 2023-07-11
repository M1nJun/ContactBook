import json

def add_contact():
    with open("contact.json") as infile:
        contacts = json.load(infile)

    PN = input("Enter phone number: ")
    FN = input("Enter first name: ")
    LN = input("Enter last name: ")

    new_contact = {PN:{"FirstName": FN, "LastName": LN}}
    contacts["data"].update(new_contact)

    #without the indent, it appeared on the json file as just a straight line of data.
    with open("contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)

def remove_contact():
    with open("contact.json") as infile:
        contacts = json.load(infile)

    index_to_delete = input("Enter the index of the person you want to delete: ")

    contacts["data"].pop(index_to_delete)

    with open("contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)

remove_contact()

# def edit_contact():
#     with open("contacts.json", "w") as infile:
#         contacts = json.load(infile)
    




def show_contact():
    with open("contact.json") as infile:
        contacts = json.load(infile)

    # for key in contacts["data"]:
    #     FN = contacts["data"][key]["FirstName"]
    #     LN = contacts["data"][key]["LastName"]
    #     print(f'{FN}-{LN}')

    for key,val in contacts["data"].items():
        PN = key
        FN = val["FirstName"]
        LN = val["LastName"]
        print(f'Phone number is: {PN}\nName is: {FN}-{LN}')

#change the data structure into key:phonenum and value: first, last name
#make a separate folder for the json files.
#change the code so that it works with the changed data structure.
#finish making edit, show contact
#should make a users.json
#if the user does not have a username.json file, make one
#change the function so that it takes in parameters from main.py
