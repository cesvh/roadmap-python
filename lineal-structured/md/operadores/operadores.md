# **Operadores**


## **Lógicos o boleanos**

### **Operador and:**
```py
# Operador and
result_and = 1 == 1 and "a" == "A"
print(result_and)
```

### **Resultado:**
```py
False
```

### **Operador or:**
```py
# Operador or
result_or = 1 == 1 or "a" == "A"
print(result_or)
```

### **Resultado:**
```py
True
```

### **Operador not:**
```py
# Operador not
result_or = not(1 == 1 or "a" == "A")
print(result_or)
```

### **Resultado:**
```py
False
```

---

## **Relacionales o de Comparación**

### **Igual a:**
```py
result = (1 == 1)
print(result)
```

### **Resultado:**
```py
True
```

### **Diferente a:**
```py
result = (1 != 1)
print(result)
```

### **Resultado:**
```py
False
```

### **Mayor que:**
```py
result = (1 > 1)
print(result)
```

### **Resultado:**
```py
False
```

### **Menor que:**
```py
result = (1 < 1)
print(result)
```

### **Resultado:**
```py
False
```

### **Mayor o igual a:**
```py
result = (1 >= 1)
print(result)
```

### **Resultado:**
```py
True
```

### **Menor o igual a:**
```py
result = (1 <= 1)
print(result)
```

### **Resultado:**
```py
True
```

---

## **Aritméticos**

### **Suma:**
```py
num1 = 299
num2 = 792
result = num1 + num2
print(result)
```

### **Resultado:**
```py
1091
```

### **Resta:**
```py
num1 = 299
num2 = 792
result = num1 - num2
print(result)
```

### **Resultado:**
```py
-493
```

### **Multiplicación:**
```py
num1 = 299
num2 = 792
result = num1 * num2
print(result)
```

### **Resultado:**
```py
236808
```

### **División exacta con resultado float:**
```py
num1 = 299
num2 = 792
result = num1 / num2
print(result)
```

### **Resultado:**
```py
0.37752525252525254
```

### **Operador módulo, entero residuo:**
```py
num1 = 299
num2 = 792
result = num1 % num2
print(result)
```

### **Resultado:**
```py
299
```

### **Entero Cociente de la división:**
```py
num1 = 299
num2 = 792
result = num1 // num2
print(result)
```

### **Resultado:**
```py
0
```

### **Potencia:**
```py
num1 = 299
num2 = 792
result = num1 ** num2
print(result)
```

### **Resultado:**
```py
53899055258415332295609974218752407774474715275499597628240691249518178371174356000880146752645491318427144761066411906998290465611074533844361123749415316489330216064555987716104787789606785256115091839577407273502984251606499406111602102325948933035784235887528531439281165981293948427460685742093155219001824635691793616489314703060504779853924328465025323417697252817523588592064192252803213168198965565641284856398002235918855129350573471168960196103012961327451725714762612237680783675194783491611132510095319890659833072559822443605347139459276106556739834447166928437952714427123836735632907998905745276921438817976886197485170656334639574761021657170785937471151427898842400832494402994703120936964933983340437983194508372604032941207413776409930645249583144866466031959056625672902568849867803445221332094458030577698175100453483093889465287505148576167505310585359158840496348789648772027666351509530108815124009780952516096120071839265706094500429864144502881993749836048485355320176973893403822724329266410853097102839398884063279614025604350312914329972465254592946851722657431743350633390308730931163369279247104386588725686462240236742342001715958647198019004950389153910550980943879620060727617992842682622563218190737980061774898494980549987525366169987920644704500521658660646254813450543274456261432950530658323082607708846781390279979699682150977126680522764792994315178472283509624790427396749892420987100634875615374984532151861829638560903249090580309045155683021120595555857854016262001841375740105286190984609110162833851036780440936928658874651267440555734879815295196744327446165569221149072047196247896336497902072939204194543630188819184377029440874180221316999400589701840201574198384977596938819340129054101811006588606076019726941866780629708106463202613029856852701388404739594762524133158866953989417775733267067286906824163383032966581580958608456218750708356522284900771939152632845868311126391232942640204348890213231002401
```

---

## **Asignación**

### **Suma:**
```py
num1 = 299
num1 += 1
print(num1)
```

### **Resultado:**
```py
300
```

### **Resta:**
```py
num1 = 299
num1 -= 1
print(num1)
```

### **Resultado:**
```py
298
```

### **Multiplicación:**
```py
num1 = 299
num1 *= 2
print(num1)
```

### **Resultado:**
```py
598
```

### **División:**
```py
num1 = 299
num1 /= 2
print(num1)
```

### **Resultado:**
```py
149.5
```

### **Residuo:**
```py
num1 = 299
num1 %= 2
print(num1)
```

### **Resultado:**
```py
1
```

### **Cociente:**
```py
num1 = 299
num1 //= 2
print(num1)
```

### **Resultado:**
```py
149
```

### **Potencia:**
```py
num1 = 299
num1 **= 2
print(num1)
```

### **Resultado:**
```py
89401
```

---

## **De pertenencia**

### **in:**
```py
x = [2, 9, 9, 7, 9, 2]
result = (9 in x)
print(result)
```

### **Resultado:**
```py
True
```

### **not in:**
```py
x = [2, 9, 9, 7, 9, 2]
result = (0 not in x)
print(result)
```

### **Resultado:**
```py
True
```

---

## **De identidad**

### **is:**
```py
x = 2
y = 9
my_list = [2, 9, 9, 7, 9, 2]
result = x is my_list
print(result)
```

### **Resultado:**
```py
False
```

### **is:**
```py
x = 2
y = 9
my_list = [2, 9, 9, 7, 9, 2]
result = (x is 2)
print(result)
```

### **Resultado:**
```py
main.py:4: SyntaxWarning: "is" with a literal. Did you mean "=="?
  result = (x is 2)
True
```
