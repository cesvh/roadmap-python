# **Ejercicios con los temas tratados hasta éste punto**

### **Números primos:**
```py
def is_prime(number):
    flag = True
    if number < 3:
        return flag
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    return flag


def main():
    number = int(input("Number:"))
    if number < 1:
        print("Only positives number ")
    else:
        result = is_prime(number)
        if result:
            print("Is prime")
        else:
            print("No is prime")


if __name__ == "__main__":
    main()
```

### **Resultado:**
```
Number: 13
Is prime
```
