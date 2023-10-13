class User:
    def __init__(self):
        self.data = {}
        self.entry = {}

    def store(self):
        name = input("Enter your name: ")
        password = input("Enter a password: ")
        self.entry.update({'password': password})
        address = input("Enter your address: ")
        self.entry.update({'address': address})
        self.data.update({name: self.entry})
        print(self.data)

    def search(self, name, password):
        if name in self.data:
            print(f"The username {name} is available")
        else:
            print("Invalid Username")
        if password in self.data[name]['password']:
            print("Correct password")
            print("Here are your details: ")
            print(f"Your Name: {name} \n Your address: {self.data[name]['address']}")
        else:
            print("Invalid password")
