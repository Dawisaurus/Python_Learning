"""Exercise: Simple Contact Book
Create a simple contact book program in Python that allows users to perform the following operations:
Add a new contact: Prompt the user to enter a name and phone number, then store this information in a dictionary.
View all contacts: Display all the contacts stored in the dictionary.
Search for a contact: Prompt the user to enter a name, then search for that name in the dictionary and 
display the corresponding phone number if found.
Delete a contact: Prompt the user to enter a name, then delete the corresponding contact from the dictionary if it exists."""

#0) Options to: add, delete, search and browse contacts
#1) I will use dictionary to store both key -> Contact Name and value -> Phone Number
#   so that you can get both number and name whenever you search for contact  
#2.1) "add" stores firstly name as a key and phone number as a value in dictionary
#2.2) "delete" removes the contact from dictionary by name
#2.3) "search" searches for contact by name and displays assigned phone number
#2.5) "contacts" browses all available contacts you stored 
#2.6) "exit" exits the program 

contactList = {} 

# I'll start a loop that will finish only when user enters 'exit'
while True:
    # Program will display all commands available to user
    print("Commands: contacts, add, delete, search, exit")
    Command = input("Command: ").lower()

    if Command == ("add"):
        # Adding a number
        addingName = input("Name: ")
        addingNumber = input("Number: ")
        contactList[addingName] = [addingNumber]
    if Command == ("contacts"):
        # Browsing all contacts
        print (contactList)
    if Command == ("delete"):
        # Deleting chosen contact by name
        deleteNumber = input("Name to delete: ")
        if deleteNumber in contactList:
            del contactList[deleteNumber]
            print (f"contact {deleteNumber} has been removed")
        else:
            print ("There's no such contact")
    if Command == ("search"):
        # Searching for chosen contact by name (That will display both name and phone number)
        searchName = input("Caller name: ")
        if searchName in contactList:
            print (contactList[searchName])
        else:
            print ("That number doesn't exist")
            # Search error
    if Command == ("exit"):
        # Program will shut down
        break