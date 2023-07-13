# ContactBook

This is my journey of learning python.

My goal is to make a simple contact book app. In the future, I want to make a simple messenger app that uses this contact book app. I will also learn Javascript, CSS, and HTML. When I get used to it, I want to learn React to make a good looking UI for these apps.

I'm keeping record of the stuff I learned here.

You can create a dictionary like this. A dictionary needs a key and a value.

```python
contact = {
    "FirstName": "Minjun",
    "LastName": "Lee",
    "PhoneNum": "9206669262"
}
```

You can print the value in the dictionary by using the key. <dict_name>["<key>"]
Also, you can print multiple stuff with one print function like this.

```python
x = contact["FirstName"]
y = contact["LastName"]
z = contact["PhoneNum"]
print(x,y,z)
```

You can get a input from user with input("<prompt>")
This is how you update your dictionary.

```python
FN = input("Enter first name: ")
LN = input("Enter last name: ")
PN = input("Enter phone number: ")

contact.update({"FirstName": FN, "LastName": LN, "PhoneNum": PN})
```

This is when I was working with json without a json file.
Dump() method used to write Python serialized object as JSON formatted data into a file_name.json
Dumps() method is used to encode any Python object into JSON formatted String.
Indent is for visual appearance, =4 is a popular choice.

```python
import json

json_object = json.dumps(contact,indent=4)
print(json_object)
```

'open()' is used to open files, takes two parameters file name(or path) and the mode.
'with' ensure that the file is properly closed after use

```python
with open("contact.json", "w") as outfile:
    json.dump(contact, outfile)
```

Question: With this code, does the data load from json file as a string? dict?
Answer: I found out from an error that this was loaded as a 'dict' object and therefore I couldn't use append.
Question: Does ' or " matter?

```python
contact = json.load(open("contact.json"))
```

This is how I converted dict object to list. After this, I could use contact.append()

```python
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
```

Starting from here, I updated my json file into a nested dict structure. It looks like this. The key for the very outer dictionary is "data" and the value is a list. Now I can simply append to this list for new contacts.

```javascript
{
    "data": [
        {
            "FirstName": "Minjun",
            "LastName": "Lee",
            "PhoneNum": "9206669262"
        },
        {
            "FirstName": "Kangbok",
            "LastName": "Lee",
            "PhoneNum": "2067937371"
        }
    ]
}
```

This is the append process. The indent is there so that the json file is neat.

```python
new_contact = {"FirstName": FN, "LastName": LN, "PhoneNum": PN}
contacts["data"].append(new_contact)

#without the indent, it appeared on the json file as just a straight line of data.
with open("contact.json", "w") as outfile:
    json.dump(contacts, outfile, indent=4)
```

If you don't speicfy the index on pop(), it will simply remove the last item on the list.

```python
contacts["data"].pop(3)
#or
del contacts["data"][3]
```

This is my remove_contact() function. I tried using print(f''), which is a convinient tool to print.
I thought it would be convinient if it were to be an index that were returned to the server.

```python
def remove_contact():
    with open("contact.json") as infile:
        contacts = json.load(infile)

    for x in range(len(contacts["data"])):
        FN = contacts["data"][x]["FirstName"]
        LN = contacts["data"][x]["LastName"]
        print(f'{x}:{FN}-{LN}')

    index_to_delete = input("Enter the index of the person you want to delete: ")

    contacts["data"].pop(index_to_delete)

    with open("contact.json", "w") as outfile:
        json.dump(contacts, outfile, indent=4)
```

I realized that using range() in for loops is kind of like a java approach.
Because I'm learning python I wanted to try something more of a python approach.

Used enumerate. If you give one variable to the for loop, you get a tuple. If you give two varibale, you get an index for the first, obeject for the second.

```python
 for index, contact in enumerate(contacts["data"]):
        FN = contact["FirstName"]
        LN = contact["LastName"]
        print(f'{index}:{FN}-{LN}')
```

For my information, you never use a function that returns a tuple to just receive a tuple.

```python
def tupleFunc():

    return a, b, c

x = tupleFunc()
x = (a, b, c) #not good
x, y, z = tupleFunc()
x, _, z = tupleFunc()
x, _, _ = tupleFunc()
```

This is my revised contact.json so that it isn't a nested dictionary with a list as a value anymore. I wanted to access the names via phone numbers.

```javascript
{
    "data": {
        "9206669262": {
            "FirstName": "Minjun",
            "LastName": "Lee"
        },
        "2067937371": {
            "FirstName": "Kangbok",
            "LastName": "Lee"
        }
    }
}
```

This is the revised code for the add_contact function. instead of append(), I'm using update(). This works for dictionarys.

```python
    new_contact = {PN:{"FirstName": FN, "LastName": LN}}
    contacts["data"].update(new_contact)
```

This is the show_contact function. I got rid of the enumerate() function from the for loop. When you give two variables and <dictionary>.items() to a for loop, you receive a key and value for each variable. In the commented version, I learned that you can get a key by giving the dictionary directly to the for loop.

```python
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
```

I learned that the functional things must stay in the Functions file and things like asking prompts are best when it stays in the main file.

I still need to figure out the options to be saved as integers. I think it is stupid to work with a string.
