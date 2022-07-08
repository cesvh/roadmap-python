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
### **Result:**
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

### **Result:**
```
else: Parsec
```
