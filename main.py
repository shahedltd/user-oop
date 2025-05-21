class User:
    user_count = 0

    def __init__(self, username, email, password):
        self.username = username  
        self.email = email
        self.__password = password
        User.user_count += 1
    
    @property
    def password(self):
        return self.__password  
    
    @password.setter
    def password(self, new_password):
        self.__password = new_password

    def account_check(self, pincode):
        if self.__password == pincode:
            return True
        return False
    
    def __str__(self):
        return f"Hello, I have an account and my account's username is: {self.username}.\nAnd here is my email: {self.email}"


# Test the code
user1 = User("shahedrahman", "shahed@xyz.com", 1111)



if user1.account_check(1111):  
    print("Login successful!")
    print(user1)
else:
    print("Invalid password, try again.")
