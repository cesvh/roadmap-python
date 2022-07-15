class Person:
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type
    
    def changePassword(self, passw):
        self.password = passw
    
    def printData(self):
        self.type_access = "root" if self.type == 0 else "normal"
        print(f"User: {self.username}\nPassword: {self.password}\ntype: {self.type}, Access: {self.type_access}\n-------------------------")

class Employe:
    def __init__(self):
        self.employe1 = Person("cesar", "000", 0)
        self.employe2 = Person("angel", "000", 1)
        self.employe3 = Person("wendy", "000", 1)
    
    def updatePassword(self):
        self.employe1.changePassword("12345")
        self.employe2.changePassword("34567")
        self.employe3.changePassword("56789")
    
    def getDatas(self):
        self.employe1.printData()
        self.employe2.printData()
        self.employe3.printData()

employe = Employe()
employe.updatePassword()
employe.getDatas()
