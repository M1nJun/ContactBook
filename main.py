#just import, I need to do shit like contact.<function name>
from Contact import *
import os

if __name__=="main":
    user_name = input("Login: ")

    try:
        with open(f'{user_name}.json') as f:
            contacts = json.load(f)
    except:
        os.create(f'(user_name).json')

    user_choice = input("Choose operations you want:\n1. Show\n2. Add\n3. Remove\n4. Edit")
    if user_choice == 1:
        show_contact()
    if user_choice == 2:
        add_contact()
    if user_choice == 3:
        remove_contact()
    if user_choice == 4:
        edit_contact()

    

