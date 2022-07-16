# **Clases y objetos**

### **Clase y objeto**
```py
class Person:
    def __init__(self, username, password, user_type):
        self.type_access = None
        self.username = username
        self.password = password
        self.user_type = user_type

    def changePassword(self, password):
        self.password = password

    def printData(self):
        self.type_access = "root" if self.user_type == 0 else "normal"
        print(f"User: {self.username}\nPassword: {self.password}\ntype: {self.user_type}, Access: {self.type_access}")
        print(f"\n-------------------------")


class Employee:
    def __init__(self):
        self.employee1 = Person("cesar", "000", 0)
        self.employee2 = Person("angel", "000", 1)
        self.employee3 = Person("wendy", "000", 1)

    def updatePassword(self):
        self.employee1.changePassword("12345")
        self.employee2.changePassword("34567")
        self.employee3.changePassword("56789")

    def getDatas(self):
        self.employee1.printData()
        self.employee2.printData()
        self.employee3.printData()


employee = Employee()
employee.updatePassword()
employee.getDatas()
```

### **Resultado:**
```sh
User: cesar
Password: 12345
type: 0, Access: root

-------------------------
User: angel
Password: 34567
type: 1, Access: normal

-------------------------
User: wendy
Password: 56789
type: 1, Access: normal

-------------------------
```
