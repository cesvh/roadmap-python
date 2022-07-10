# **Estructura de datos**
## **Lista**

### **base:**
```py
list = [2, 9, 9, 7, 9, 2]
print(type(list))
print(list)
print(list[0])
print(list[1])
print(list[len(list) - 1])
```

### **Resultado:**
```
<class 'list'>
[2, 9, 9, 7, 9, 2]
2
9
2
```

### **append:**
```py
list = [2, 9]
list.append(9)
list.append(7)
list.append(9)
list.append(2)
print(list)
```

### **Resultado:**
```
[2, 9, 9, 7, 9, 2]
```

### **pop:**
```py
list = [1, 2, 9, 9, 7, 9, 2]
print(list)
list.pop(0)
print(list)
list.pop(3)
print(list)
list.pop()
print(list)
```

### **Resultado:**
```
[1, 2, 9, 9, 7, 9, 2]
[2, 9, 9, 7, 9, 2]
[2, 9, 9, 9, 2]
[2, 9, 9, 9]
```

---

### **insert:**
```py
list = [9, 9, 9]
list.insert(0, 2)
print(list)
list.insert(3, 7)
print(list)
list.insert(5, 2)
print(list)
```

### **Result:**
```
[2, 9, 9, 9]
[2, 9, 9, 7, 9]
[2, 9, 9, 7, 9, 2]
```
