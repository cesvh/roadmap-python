# **Funciones**

### **Funciones base:**
```py
def start():
	print("Hello world")

if __name__ == "__main__":
	start()
```

### **Resultado:**
```
Hello
```

### **Funciones con parámetros:**
```py
def main(msg):
	print(msg)

def start():
	msg = "Hello"
	main(msg)

if __name__ == "__main__":
	start()
```

### **Resultado:**
```
Hello world
```

### **Funciones con return:**
```py
def main(msg):
	return f"The message is: {msg}"

def start():
	msg = "Hello"
	new_msg = main(msg)
	print(new_msg)

if __name__ == "__main__":
	start()
```

### **Resultado:**
```
The message is: Hello
```
