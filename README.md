# ContactBook

This is my journey of learning python.

My goal is to make a simple contact book app. In the future, I want to make a simple messenger app that uses this contact book app. I will also learn Javascript, CSS, and HTML. When I get used to it, I want to learn React to make a good looking UI for these apps.

I'm keeping record of the stuff I learned here.

You can create a dictionary like this. A dictionary needs a key and a value.

```
contact = {
    "FirstName": "Minjun",
    "LastName": "Lee",
    "PhoneNum": "9206669262"
}
```

You can print the value in the dictionary by using the key. <dict_name>["<key>"]
Also, you can print multiple stuff with one print function like this.

```
x = contact["FirstName"]
y = contact["LastName"]
z = contact["PhoneNum"]
print(x,y,z)
```

You can get a input from user with input("<prompt>")
This is how you update your dictionary.

```
FN = input("Enter first name: ")
LN = input("Enter last name: ")
PN = input("Enter phone number: ")

contact.update({"FirstName": FN, "LastName": LN, "PhoneNum": PN})
```

This is when I was working with json without a json file.
Dump() method used to write Python serialized object as JSON formatted data into a file_name.json
Dumps() method is used to encode any Python object into JSON formatted String.
Indent is for visual appearance, =4 is a popular choice.

```
import json

json_object = json.dumps(contact,indent=4)
print(json_object)
```

'open()' is used to open files, takes two parameters file name(or path) and the mode.
'with' ensure that the file is properly closed after use

```
with open("contact.json", "w") as outfile:
    json.dump(contact, outfile)
```

Question: With this code, does the data load from json file as a string? dict?
Answer: I found out from an error that this was loaded as a 'dict' object and therefore I couldn't use append.
Question: Does ' or " matter?

```
contact = json.load(open("contact.json"))
```

This is how I converted dict object to list. After this, I could use contact.append()

```
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
