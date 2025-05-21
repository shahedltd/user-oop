# 🧑‍💻 User Account Class in Python

A simple Python class to represent a user account system. This class demonstrates object-oriented programming concepts including encapsulation, property decorators, class variables, and string representation.

---

## 🔍 Features

- Create user accounts with a username, email, and password.
- Password encapsulation using private variables.
- Password update functionality via property setters.
- Login verification through a `pincode` check.
- Class-level user counter to track the number of user instances.
- Readable string representation using the `__str__` method.

---

## 🛠️ How It Works

The `User` class provides the following capabilities:

- When a user object is created, the username, email, and password are set.
- The password is stored privately and accessed via a `@property`.
- The user can update the password using a setter method.
- The `account_check(pincode)` method allows simple login verification.
- A class variable `user_count` keeps track of the number of users created.

---

## 🚀 Getting Started

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

    Run the script:

python3 user_account.py

    Replace your-username and your-repo-name with your actual GitHub username and repository name.

🧪 Example
Code:

user1 = User("shahedrahman", "shahed@xyz.com", 1127)

if user1.account_check(1127):  
    print("Login successful!")
    print(user1)
else:
    print("Invalid password, try again.")

Output:

Login successful!
Hello, I have an account and my account's username is: shahedrahman.
And here is my email: shahed@xyz.com

📁 File Structure

user_account.py   # Python file with the User class
README.md         # Project documentation

📚 Concepts Used

    Classes & Objects

    Class Variables

    Private Attributes

    Getters and Setters

    Encapsulation

    Magic Methods (__str__)

👨‍💻 Author

Shahed Rahman
📫 Reach out for collaboration or suggestions!
