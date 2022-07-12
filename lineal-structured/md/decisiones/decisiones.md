# **Decisiones**

## **Biburcaciones**

### **if:**
```py
username = "Parsec"
if username == "Parsec":
    print(f"if: {username}")
```
### **Resultado:**
```
if: Parsec
```

---

### **else:**
```py
username = "Parsec"
if username == "parsec":
    print(f"if: {username}")
else:
    print(f"else: {username}")
```
### **Resultado:**
```
else: Parsec
```

---

### **elif:**
```py
username = "Parsec"
if username == "parsec":
    print(f"if: {username}")
elif username == "parse":
    print(f"elif: {username}")
else:
    print(f"else: {username}")
```

### **Resultado:**
```
else: Parsec
```

---

### **Operador ternario:**
```py
x = 1
msg = "Mayor a 0" if x > 0 else "Menor o igual a 0"
print(msg)
```

### **Resultado:**
```
Mayor a 0
```
