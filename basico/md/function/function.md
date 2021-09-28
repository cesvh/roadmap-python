# **Funciones**

```py
def fncReturn(year):
    return f'ly: {year}'


def fncParam(name):
    print(f'{name}')
    ly = fncReturn(299)
    print(ly)


def start():
    print("Hello hell")
    fncParam('Pársec')


if __name__ == '__main__':
    start()
```

```sh
Hello hell
Pársec
ly: 299

Process finished with exit code 0
```
