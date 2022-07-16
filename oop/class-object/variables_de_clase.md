# **Clases y objetos**

### **Clase y objeto**
```py
class Person:
    created_objects = 9

    def __init__(self, username):
        self.username = username


person1 = Person("Cesar")
person2 = Person("Angel")
print(f"person1: {person1.created_objects}")
print(f"person2: {person2.created_objects}")
print("------------------------------------")
Person.created_objects = 0
print(f"Person: {Person.created_objects}")
print(f"person1: {person1.created_objects}")
print(f"person2: {person2.created_objects}")
print("------------------------------------")
person1.created_objects = 5
person2.created_objects = 3
print(f"Person: {Person.created_objects}")
print(f"person1: {person1.created_objects}")
print(f"person2: {person2.created_objects}")
```

### **Resultado:**
```sh
person1: 9
person2: 9
------------------------------------
Person: 0
person1: 0
person2: 0
------------------------------------
Person: 0
person1: 5
person2: 3
```
