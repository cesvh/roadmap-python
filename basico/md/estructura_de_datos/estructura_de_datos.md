# **Estructura de datos**

```py
list = [2, 9, 9]

list.append(7)
list.append(9)
list.append(2)
list.append(4)
list.append(5)
list.append(8)

print(list)

list.pop()
list.pop(3)

print(list)
```

```sh
[2, 9, 9, 7, 9, 2, 4, 5, 8]
[2, 9, 9, 9, 2, 4, 5]

Process finished with exit code 0
```

---

```py
list = [2, 9, 9]

list.append(7)
print(list)
list.append(9)
print(list)
list.append(2)
print(list)
list.append(4)
print(list)
list.append(5)
print(list)
list.append(8)
print(list)

list.pop()
print(list)
list.pop(3)
print(list)

list.insert(3, 7)
print(list)
list.insert(8, 8)
print(list)
```

```sh
[2, 9, 9, 7]
[2, 9, 9, 7, 9]
[2, 9, 9, 7, 9, 2]
[2, 9, 9, 7, 9, 2, 4]
[2, 9, 9, 7, 9, 2, 4, 5]
[2, 9, 9, 7, 9, 2, 4, 5, 8]
[2, 9, 9, 7, 9, 2, 4, 5]
[2, 9, 9, 9, 2, 4, 5]
[2, 9, 9, 7, 9, 2, 4, 5]
[2, 9, 9, 7, 9, 2, 4, 5, 8]

Process finished with exit code 0
```
