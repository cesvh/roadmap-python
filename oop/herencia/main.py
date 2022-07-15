class Person:
    def __init__(self, username):
        self.username = username
    
    def printData(self):
        print("\n-----\n-----Datas")
        print(f"Username: {self.username}")


class Employee(Person):
    def __init__(self, username):
        super().__init__(username)
        self.level = "root"
    
    def printData(self):
        super().printData()
        print(f"Level: {self.level}")


class Customer(Person):
    def __init__(self, username):
        super().__init__(username)
        self.level = "normal"
    
    def printData(self):
        super().printData()
        print(f"Level: {self.level}")


if __name__ == "__main__":
    user_name = input("Username: ")
    key = input("Key: ")
    if key == "root":
        employee = Employee(user_name)
        employee.printData()
    else:
        customer = Customer(user_name)
        customer.printData()