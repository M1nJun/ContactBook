#just import, I need to do shit like contact.<function name>
from Contact import *

if __name__=="main":
    user_choice = input("Choose operations you want:\n1. Show\n2. Add\n3. Remove\n4. Edit")
    match user_choice:
        case 1:
            show_contact()
        case 2:
            add_contact()
        case 3:
            remove_contact()
        case 4:
            edit_contact()

    

