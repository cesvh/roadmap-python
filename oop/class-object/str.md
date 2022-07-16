# **Métodos nativos**

### **str**
```py
class Person:
    def __init__(self, name):
        self.name = name


person = Person("Cesar")
print(person)
```

### **Resultado:**
```sh
<__main__.Person object at 0x000002998B307DC0>
```

### **str**
```py
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Value Object: {self.name}"


person = Person("Cesar")
print(person)
```

### **Resultado:**
```sh
Value Object: Cesar
```
