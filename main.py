import time
from getpass import getpass
from storage import load_vault , save_vault
from crypto_utils import encrypt_data , decrypt_data
from password_utils import generate_password , check_strength
from auth import verify_master_password

def add_password(master):

    vault = load_vault()

    site = input("Website: ")

    if site in vault:
        choice = input("Website already exists. Overwrite? (y/n): ")

        if choice.lower() != "y":
            return

    username = input("Username: ")
    password = input("Password(leave blank to generate): ")


    if password == "":
        password = generate_password()
        print("Generated password:" , password)

    print("Password strength:", check_strength(password))

    encrypted = encrypt_data(password, master)

    vault[site] = {
    "username" : username,
    "password" : encrypted
    }

    save_vault(vault)

    print("Password saved!")



def view_password(master):

    vault = load_vault()

    site_input = input("Enter Website: ").lower()

    for site in vault:

        if site.lower() == site_input:

            username = vault[site]["username"]
            password = decrypt_data(vault[site]["password"], master)

            print("\nWebsite:", site)
            print("Username:", username)

            # show masked password
            print("Password:", "*" * len(password))

            reveal = input("Reveal password? (y/n): ")

            if reveal.lower() == "y":
                print("Actual Password:", password)

            print("Password strength:", check_strength(password))

            return

    print("Website not found.")

def search_password(master):

    vault = load_vault()

    keyword = input("Search website: ")

    found = False

    for site in vault:

        if keyword.lower() in site.lower():

            found = True

            print("\nSite:", site)
            print("Username:", vault[site]["username"])

            show = input("Show password? (y/n): ")

            if show.lower() == "y":
                password = decrypt_data(vault[site]["password"], master)
                print("Password:", password)
            else:
                print("Password hidden")

    if not found:
        print("No matching websites found.")



def update_password(master):

    vault = load_vault()

    site = input("Enter website to update: ")

    if site not in vault:
        print("Website not found.")
        return

    print("\nWhat do you want to update?")
    print("1. Website name")
    print("2. Username")
    print("3. Password")

    choice = input("Select option: ")

    if choice == "1":

        new_site = input("Enter new website name: ")

        vault[new_site] = vault.pop(site)

        save_vault(vault)

        print("Website name updated successfully!")

    elif choice == "2":

        new_username = input("Enter new username: ")

        vault[site]["username"] = new_username

        save_vault(vault)

        print("Username updated successfully!")

    elif choice == "3":

        new_password = input("Enter new password (leave blank to generate): ")

        if new_password == "":
            new_password = generate_password()
            print("Generated password:", new_password)

        print("Password strength:", check_strength(new_password))

        encrypted = encrypt_data(new_password, master)

        vault[site]["password"] = encrypted

        save_vault(vault)

        print("Password updated successfully!")

    else:
        print("Invalid option.")


def delete_password():

    vault = load_vault()

    site_input = input("Enter website to delete: ").lower()

    for site in vault:

        if site.lower() == site_input:

            confirm = input("Are you sure? (y/n): ")

            if confirm.lower() == "y":
                del vault[site]
                save_vault(vault)
                print("Password deleted.")

            return

    print("Website not found.")


def menu(master):

    TIMEOUT = 300

    while True:

        print("\n==== PASSWORD MANAGER ====")
        print("1. Add Password")
        print("2. View Password")
        print("3. Search Password")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Generate Strong Password")
        print("7. Exit")

        start_time = time.time()

        choice = input("Select option: ")

        end_time = time.time()

        # check inactivity
        if end_time - start_time > TIMEOUT:
            print("\nSession timed out. Please login again.")
            break

        if choice == "1":
            add_password(master)

        elif choice == "2":
            view_password(master)

        elif choice == "3":
            search_password(master)

        elif choice == "4":
            update_password(master)

        elif choice == "5":
            delete_password()

        elif choice == "6":
            print("Generated Password:", generate_password())

        elif choice == "7":
            print("Exiting Password Manager...")
            break

        else:
            print("Invalid option")

def main():

    print("==== PASSWORD MANAGER ====")

    master = getpass("Enter master password: ")

    if verify_master_password(master):
        menu(master)
    else:
        print("Wrong password")

if __name__ == "__main__":
    main()