"""
=================================================================================
Contact Manager - Python Assignment
=================================================================================
Name : Anshika
Roll No : 2501940028
Course : MCA (AI & Ml)
Date : 13 November 2025
Assignment : Contact Book - Contact Manager
"""

import csv
import json
from datetime import datetime

# ================================================================================
# Task 1: Setup & Project Initialization
# ================================================================================
print("Welcome to the contact book!")
print("This contact Book helps you to store, view, search, update, and delete contacts easily.")
print("Contacts are saved in CSV and can be exported to JSON Format.\n")

# ================================================================================
# Tasks 2: Create and save contacts 
# ================================================================================
def add_contact():
    """Adds a new contact and saves to contacts.csv"""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    contact = {"name": name, "phone": phone, "email": email}

    try:
        with open("contacts.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(contact)

        print("Contact saved successfully!")

    except Exception as e:
        log_error("saving contact", str(e))
        print("Error: Could not save contact.")

# ================================================================================
# Tasks 3: Read & Display Contacts
# ================================================================================
def display_contacts():
    """Reads and prints contacts in table format."""
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            contacts = list(reader)

            if not contacts:
                print("No contacts found!")
                return
            
            print("\n---- Contacts List ----")
            print(f"{'Name':<15}\t{'Phone':<15}\t{'Email'}")
            print("-" * 50)

            for c in contacts:
                print(f"{c['name']:<15}\t{c['phone']:<15}\t{c['email']}")

    except FileNotFoundError:
        log_error("Display Contacts", "contacts.csv file not found")
        print("Error: contacts.csv does not exist.")

    except Exception as e:
        log_error("Display Contacts", str(e))
        print("Error reading contact list.")

# ==============================================================================
# Tasks 4: Search, Update, Delete 
# ==============================================================================
def search_contact():
    name = input("Enter name to search: ")
    contacts = read_contacts()

    for c in contacts:
        if c["name"].lower() == name.lower():
            print("\nContact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['Phone']}")
            print(f"Email: {c['email']}\n")

    print("Contact not found.\n")
    return None

def update_contact():
    name = input("Enter name to update: ")
    contacts = read_contacts()

    found = False

    for c in contacts:
        if c["name"].lower() == name.lower():
            found = True
            print("Leave field blank to keep old value.")

            new_phone = input(f"New Phone ({c['phone']}): ")
            new_email = input(f"New Email ({c['email']}): ")

            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email

    if not found:
        print("Contacts not found.\n")
        return
    
    # Save updated list back to CSV
    try:
        with open("contact.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows(contacts)

        print("Contact updated successfully!\n")

    except Exception as e:
        print("Error updating contact.")
        log_error(str(e), "Update Contact")


def delete_contact():
    name = input("Enter name to delete: ")
    contacts = read_contacts()

    new_list = [c for c in contacts if c["name"].lower() != name.lower()]

    if len(new_list) == len(contact):
        print("Contact not found.\n")
        return
    
    try:
        with open("contacts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows(new_list)

        print("Contact deleted successfully!\n")


    except Exception as e:
        print("Error deleting contact.")
        log_error(str(e), "Delete Contact")


# ======================================================================================
# Tasks 5: JSON Export & Import
# ======================================================================================
def export_to_json():
    contacts = read_contacts()

    try:
        with open("contact.json", "w") as json_files:
            json.dump(contacts, json_files, indent=4) 

        print("Contacts exported to contacts.json successfully!\n")

    except Exception as e:
        print("Error exporting to JSON.")
        log_error(str(e), "Export JSON")


def load_from_json():
    try:
        with open("contacts.json", "r") as json_files:
            contacts = json.load(json_files)

            print("\nContacts Loaded from JSON:")
            print("Name\t\tPhone\t\tEmail")
            print("------------------------------------------------")

            for c in contacts:
                print(f"{c['name']:<15}\t{c['phone']:<12}\t{c['email']}")

            print()

    except FileNotFoundError:
        print("contacts.json not found.\n")
        log_error("contacts.json missing", "Load JSON")
    except Exception as e:
        print("Error loading JSON.")
        log_error(str(e), "Load JSON")


# =============================================== Main Menu =========================================== #
while True:
    print("1. Add COntact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Export to JSON")
    print("7. Load from JSON")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "i":
        save_contact_to_csv(add_contact()) 
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        export_to_json()
    elif choice == "7":
        load_from_json()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")                                                   
            