import json
import os

if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
else:
    contacts = {}

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def menu():
    while True:
        clear_screen()
        print("~~~~~ Contact Book ~~~~~")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            update_contact()

        elif choice == "6":
            save_contacts()
            break

        else:
            print("Invalid choice!")
            input("\nPress Enter to continue...")


def add_contact():
    clear_screen()
    name = input("Enter your contact's name: ")

    if name in contacts:
        print("Contact already exists!")

    else:
        number = input("Enter your contact's phone number: ")
        contacts[name] = number
        print("Contact added successfully!")
        save_contacts()
        
    input("\nPress Enter to continue...")


def show_contacts():
    clear_screen()
    if not contacts:
        print("No contacts found!")

    else:
        for key, value in contacts.items():
            print(key, ":", value)
    input("\nPress Enter to continue...")


def search_contact():
    clear_screen()
    name = input("Enter a name for searching: ")

    if name in contacts:
        print(name, ":", contacts[name])

    else:
        print("Contact Not Found!")
    input("\nPress Enter to continue...")


def delete_contact():
    clear_screen()
    name = input("Enter a name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
        save_contacts()

    else:
        print("Contact Not Found!")
    input("\nPress Enter to continue...")


def update_contact():
    clear_screen()
    name = input("Enter contact name: ")

    if not contacts:
        print("No contacts available!")

    elif name in contacts:
        new_number = input("Enter new number: ")
        contacts[name] = new_number
        print("Contact successfully updated!")
        save_contacts()

    else:
        print("Contact Not Found!")
    input("\nPress Enter to continue...")


clear_screen()
menu()