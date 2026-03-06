# Python Command-Line Password Manager

A secure **Command-Line Password Manager** built using Python that allows users to store and manage credentials safely using **encryption and master password authentication**.

This project demonstrates **secure password storage, encryption techniques, and modular Python application design**.

---

##  Features

*  **Master Password Authentication**

  * Uses **SHA-256 hashing** to securely store and verify the master password.

*  **Encrypted Password Storage**

  * Uses **Fernet symmetric encryption** from the `cryptography` library to encrypt credentials.

*  **Secure Password Generator**

  * Generates strong random passwords using Python's `secrets` module.

*  **Password Strength Checker**

  * Evaluates password strength based on length, digits, uppercase letters, and symbols.

*  **Search Stored Credentials**

  * Search for saved websites using partial keyword matching.

*  **Update Credentials**

  * Update website name, username, or password.

*  **Delete Passwords**

  * Remove credentials securely from the vault.

*  **Masked Password Viewing**

  * Passwords are masked by default with an option to reveal.

*  **Session Timeout**

  * Automatically logs out after inactivity.

---

##  Technologies Used

* Python
* Cryptography (Fernet Encryption)
* JSON File Storage
* SHA-256 Hashing
* CLI (Command-Line Interface)

---

Generated files (not uploaded to GitHub):

vault.json
master.hash

---

### Install Dependencies

pip install -r requirements.txt

---

###  Run the Application

python main.py

---

##  Example Usage

==== PASSWORD MANAGER ====

1. Add Password
2. View Password
3. Search Password
4. Update Password
5. Delete Password
6. Generate Strong Password
7. Exit

---

##  Security Concepts Implemented

* SHA-256 password hashing
* Symmetric encryption using Fernet
* Secure password generation
* Masked password display
* Session timeout handling
* Brute-force login protection

---

##  Future Improvements

* Export/import password vault
* Clipboard password copy feature
* GUI version using Tkinter or PyQt
* Database storage using SQLite

---

## 👨‍💻 Author

Developed as a **Python security-focused project** demonstrating encryption, authentication, and secure credential storage.
