# **Ejercicios con los temas tratados hasta éste punto**

```py
def fnc_is_prime(number):
    flag = True
    if 0 < number < 3:
        return flag
    for i in range(2, number):
        if (number % i) == 0:
            flag = False
            break
    return flag


def fnc_start():
    number = int(input('Enter a number: '))
    if fnc_is_prime(number):
        print('Is prime')
    else:
        print('Not is prime')


if __name__ == '__main__':
    fnc_start()
```
